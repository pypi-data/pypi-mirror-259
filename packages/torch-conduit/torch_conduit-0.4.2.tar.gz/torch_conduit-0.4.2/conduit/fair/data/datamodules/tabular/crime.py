"""Crime Dataset."""

from dataclasses import dataclass

from ethicml.data import Crime, Dataset
from ethicml.data import CrimeSplits as CrimeSens

from conduit.fair.data.datamodules.tabular.base import EthicMlDataModule

__all__ = ["CrimeDataModule", "CrimeSens"]


@dataclass(kw_only=True)
class CrimeDataModule(EthicMlDataModule):
    """Data Module for the Crime Dataset."""

    sens_feat: CrimeSens = CrimeSens.RACE_BINARY
    disc_feats_only: bool = False

    @property
    def em_dataset(self) -> Dataset:
        return Crime(
            split=self.sens_feat, discrete_only=self.disc_feats_only, invert_s=self.invert_s
        )
