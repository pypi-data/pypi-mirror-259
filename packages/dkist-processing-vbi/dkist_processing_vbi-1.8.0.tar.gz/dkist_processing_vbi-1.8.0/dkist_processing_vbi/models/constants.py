"""VBI additions to common constants."""
from enum import Enum

from dkist_processing_common.models.constants import ConstantsBase


class VbiBudName(Enum):
    """Names to be used in VBI buds."""

    num_mosaics_repeats = "NUM_MOSAIC_REPEATS"
    num_spatial_steps = "NUM_SPATIAL_STEPS"
    gain_exposure_times = "GAIN_EXPOSURE_TIMES"
    observe_exposure_times = "OBSERVE_EXPOSURE_TIMES"


class VbiConstants(ConstantsBase):
    """VBI specific constants to add to the common constants."""

    @property
    def num_mosaic_repeats(self) -> int:
        """Return the number of times the full mosaic is repeated."""
        return self._db_dict[VbiBudName.num_mosaics_repeats.value]

    @property
    def num_spatial_steps(self) -> int:
        """Spatial steps in a raster."""
        return self._db_dict[VbiBudName.num_spatial_steps.value]

    @property
    def gain_exposure_times(self) -> [float]:
        """Exposure times of gain frames."""
        return self._db_dict[VbiBudName.gain_exposure_times.value]

    @property
    def observe_exposure_times(self) -> [float]:
        """Exposure times of observe frames."""
        return self._db_dict[VbiBudName.observe_exposure_times.value]
