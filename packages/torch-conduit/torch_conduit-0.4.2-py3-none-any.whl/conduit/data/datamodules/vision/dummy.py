"""Dummy data-module."""

from dataclasses import dataclass
from pathlib import Path
from typing import Union
from typing_extensions import override

from conduit.data import TrainValTestSplit
from conduit.data.datamodules.vision import CdtVisionDataModule
from conduit.data.datasets.vision.dummy import DummyVisionDataset, SampleType


@dataclass(kw_only=True)
class DummyVisionDataModule(CdtVisionDataModule[SampleType]):
    num_samples: int = 1_000
    seed: int = 8
    root: Union[str, Path] = ""
    height: int = 32
    width: int = 32
    channels: int = 3
    batch_size: int = 32
    s_card: int | None = 2
    y_card: int | None = 2

    @override
    def _get_image_splits(self) -> TrainValTestSplit[DummyVisionDataset]:
        # Split the data randomly according to val- and test-prop
        data = DummyVisionDataset(
            channels=self.channels,
            height=self.height,
            width=self.width,
            num_samples=self.num_samples,
            s_card=self.s_card,
            y_card=self.y_card,
        )
        val_data, test_data, train_data = data.random_split(props=(self.val_prop, self.test_prop))
        return TrainValTestSplit(train=train_data, val=val_data, test=test_data)
