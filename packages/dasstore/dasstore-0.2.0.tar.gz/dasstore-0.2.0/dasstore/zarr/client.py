import logging
from datetime import datetime

import zarr

from ..utils.credential import get_credential


class Client:
    def __init__(
        self,
        bucket,
        endpoint,
        region="",
        anon=False,
        role_assigned=False,
        credential_path="~/.dasstore/credentials",
        secure=True,
    ):
        self.backend = "Zarr"
        if "s3://" in bucket:
            self.bucket = bucket.replace("s3://", "")
        else:
            self.bucket = bucket
        self.anon = anon
        self.role_assigned = role_assigned
        self.secure = secure

        self.config = {}
        self.config["region"] = region
        self.config["endpoint"] = endpoint.rstrip("/")

        if self.role_assigned:
            self.credential = None
        elif not anon:
            self.credential = get_credential(endpoint, credential_path)
            self.config["key"] = self.credential["aws_access_key_id"]
            self.config["secret"] = self.credential["aws_secret_access_key"]

        if "https://" in endpoint:
            self.secure = True
            self.config["secure"] = "https"
        elif "http://" in endpoint:
            self.secure = False
            self.config["secure"] = "http"
        else:
            if self.secure:
                self.config["endpoint"] = "https://" + self.config["endpoint"]
            else:
                self.config["endpoint"] = "http://" + self.config["endpoint"]
            logging.warning(f'Endpoint overwrited: {self.config["endpoint"]}')

        self.storage_options = self.get_storage_options()
        self.meta = self.get_metadata()

        self._t0 = datetime.strptime(
            self.meta["acquisition.acquisition_start_time"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        self._t1 = datetime.strptime(
            self.meta["acquisition.acquisition_end_time"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        self._fs = self.meta["acquisition.acquisition_sample_rate"]

        for i in self.__str__().split("\n"):
            logging.info(i)

    def get_data(self, channels, starttime, endtime, attr="RawData"):
        if isinstance(starttime, str):
            if "." in starttime:
                starttime = datetime.strptime(starttime, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                starttime = datetime.strptime(starttime, "%Y-%m-%dT%H:%M:%S")
        if isinstance(endtime, str):
            if "." in endtime:
                endtime = datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                endtime = datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S")

        try:
            assert starttime >= self._t0
        except AssertionError:
            raise ValueError(
                f"starttime [{starttime}] earlier than acquisition start time [{self._t0}]"
            )

        try:
            assert endtime <= self._t1
        except AssertionError:
            raise ValueError(
                f"endtime [{endtime}] later than acquisition end time [{self._t1}]"
            )

        istart = int((starttime - self._t0).total_seconds() * self._fs)
        iend = int((endtime - self._t0).total_seconds() * self._fs)

        A = zarr.open(
            f"s3://{self.bucket}/RawData", "r", storage_options=self.storage_options
        )

        return A.oindex[channels, istart:iend]  # allowing list or numpy.array

    def get_channel(self):
        try:
            import pandas as pd
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Install pandas to read cable file.")

        return pd.read_csv(
            f"s3://{self.bucket}/cable.csv", storage_options=self.storage_options
        )

    def get_metadata(self):
        A = zarr.open_array(
            f"s3://{self.bucket}/RawData", "r", storage_options=self.storage_options
        )
        return dict(A.attrs)

    def get_storage_options(self):
        storage_options = {"client_kwargs": {"endpoint_url": self.config["endpoint"]}}
        if not self.role_assigned:
            if self.anon:
                storage_options["anon"] = True
            else:
                storage_options["key"] = self.config["key"]
                storage_options["secret"] = self.config["secret"]
        return storage_options

    def __str__(self):
        s = ""
        s += f"Endpoint:  \t {self.config['endpoint']}\n"
        s += f"Path:      \t s3://{self.bucket} \n"
        s += f"Anonymous: \t {self.anon} \n"
        s += f"Backend:   \t {self.backend}"

        return s

    def _repr_pretty_(self, p, cycle):  # pragma: no cover
        p.text(self.__str__())
