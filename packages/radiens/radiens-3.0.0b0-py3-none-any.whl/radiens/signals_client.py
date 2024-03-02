from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
import radiens.api.api_allego as api_allego
import radiens.api.api_videre as api_videre
from radiens.grpc_radiens import common_pb2
from radiens.lib.dataset_metadata import DatasetMetadata
from radiens.lib.signals_snapshot import PSD, Signals
from radiens.utils.constants import (DEFAULT_HUB_ID,
                                     PRIMARY_CACHE_STREAM_GROUP_ID, SIG_SELECT,
                                     TIME_RANGE)
from radiens.utils.enums import (FftWindow, KeyIndex, PsdScaling,
                                 RadiensService, SignalType, TrsMode)
from radiens.utils.util import (make_time_range, sig_sel_to_protobuf,
                                time_range_to_protobuf)

# the following lines are to avoid circular imports and are only used for typing hints
# (TYPE_CHECKING always evaluates to false at runtime)
if TYPE_CHECKING:
    from radiens.allego_client import AllegoClient
    from radiens.videre_client import VidereClient


class SignalsClient:
    """
    Signals client object for Allego, Curate, and Videre
    """

    def __init__(self, parent_client):
        """
        """
        self.__parent: AllegoClient | VidereClient = parent_client

    def _is_allego(self) -> bool:
        return self.__parent.type.is_allego()

    def _is_curate(self) -> bool:
        return self.__parent.type.is_curate()

    def _is_videre(self) -> bool:
        return self.__parent.type.is_videre()

    def get_signals(self,
                    time_range: TIME_RANGE | list[float] | np.ndarray = None,
                    sel_mode: TrsMode = None,
                    sig_sel: SIG_SELECT = None,
                    dataset_metadata: DatasetMetadata = None,
                    hub_name=DEFAULT_HUB_ID) -> Signals:
        """
        Gets signals over the specified time range from a linked dataset.

        Parameters:
            time_range (TIME_RANGE): see :py:meth:`~radiens.utils.util.make_time_range`
            dataset_metadata: see :py:meth:`link_data_file` and :py:meth:`get_data_file_metadata`
            sel_mode: optional (default :py:attr:`TRS_MODE.SUBSET`)
            sig_sel: optional
            hub_name: optional


        Returns:
            signals (Signals)
        """
        if not self._is_allego() and not isinstance(dataset_metadata, DatasetMetadata):
            raise ValueError(
                'videre & curate: dataset_metadata must be provided')

        if isinstance(time_range, list) or isinstance(time_range, np.ndarray):
            time_range = make_time_range(
                time_range=time_range, fs=dataset_metadata.TR.fs)
        if not isinstance(time_range, TIME_RANGE):
            raise ValueError(
                'time_range must be TIME_RANGE, list, or np.ndarray')
        if not isinstance(sel_mode, TrsMode):
            sel_mode = TrsMode.SUBSET
        if sig_sel in [None]:
            sig_sel = SIG_SELECT(key_idx=KeyIndex.NTV,
                                 amp=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.AMP).ntv, dtype=np.int64),
                                 gpio_ain=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.AIN).ntv, dtype=np.int64),
                                 gpio_din=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.DIN).ntv, dtype=np.int64),
                                 gpio_dout=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.DOUT).ntv, dtype=np.int64),
                                 )
        elif not isinstance(sig_sel, SIG_SELECT):
            raise ValueError("sig_sel must be None or SIG_SELECT")
        elif sig_sel.key_idx not in [KeyIndex.NTV]:
            raise ValueError("sig_sel must use KeyIndex.NTV as the key index")
        req = common_pb2.HDSnapshotRequest2(
            tR=time_range_to_protobuf(time_range),
            selMode=int(sel_mode.value),
            sigSel=sig_sel_to_protobuf(sig_sel),
        )
        if self._is_allego():
            req.dsourceID = PRIMARY_CACHE_STREAM_GROUP_ID
            return api_allego.get_signals(RadiensService.CORE, req)
        else:
            req.dsourceID = dataset_metadata.attributes["dsource_id"]
            return api_videre.get_signals(
                self.__parent._server_address(
                    hub_name, RadiensService.CORE), req
            )

    def get_psd(
        self,
        time_range: TIME_RANGE = None,
        sel_mode: TrsMode = None,
        sig_sel: SIG_SELECT = None,
        samp_freq: float = 2000.0,
        freq_range: list | np.ndarray = [1, 300],
        collapse_freq: bool = False,
        scaling: PsdScaling = PsdScaling.SPECTRUM,
        window: FftWindow = FftWindow.HAMMING_p01,
        freq_resolution: float = None,
        file: str = None,
        data: bool = True,
        dataset_metadata=None,
        hub_name=DEFAULT_HUB_ID,
    ) -> PSD:
        """
        Gets the power spectral density (PSD) for the specified signals over the specified time range.

        Parameters:
            time_range (TIME_RANGE) : requested time range in seconds (required)
            sel_mode (TRS_MODE): time range selection mode (optional, default=TRS_MODE.SUBSET)
            sig_sel (SIG_SELECT): requested AMP signals (optional, default=all AMP signals)
            samp_freq (float): PSD sample frequency in Hz. None=dataset_metadata.TR.fs (optional, default=2000.0)
            freq_range (list, np.ndarray): requested frequency range.  (optional, default=[1, 300])
            collapse_freq (bool): True collapses `freq_range` into one frequency bin (optional, default=False)
            scaling (PSD_SCALING): sets the PSD scale (optional, default=PSD_SCALING.SPECTRUM)
            window (FFT_WINDOW): sets the FFT window(optional, default=FFT_WINDOW.HAMMING_p01)
            freq_resolution (float): requested frequency resolution in Hz (optional, default=None)
            file (string): save psd data to file (optional, default=None)
            data (bool): return PSD data if true (optional, default=True)
            dataset_metadata (DatasetMetadata): dataset metadata (required for Videre, optional for Allego, default=None)
            hub_name (str): Radiens hub name (optional, default=DEFAULT_HUB)


        Returns:
            psd (PSD): container object for PSD data.
        """
        if not self._is_allego() and not isinstance(dataset_metadata, DatasetMetadata):
            raise ValueError(
                'videre & curate: dataset_metadata must be provided')
        if not isinstance(time_range, TIME_RANGE):
            raise ValueError("time_range must be TIME_RANGE")
        if not isinstance(sel_mode, TrsMode):
            sel_mode = TrsMode.SUBSET
        if not isinstance(scaling, PsdScaling):
            scaling = PsdScaling.SPECTRUM
        if not isinstance(window, FftWindow):
            window = FftWindow.HAMMING_p01
        if sig_sel in [None]:
            sig_sel = SIG_SELECT(key_idx=KeyIndex.NTV,
                                 amp=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.AMP).ntv, dtype=np.int64),
                                 gpio_ain=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.AIN).ntv, dtype=np.int64),
                                 gpio_din=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.DIN).ntv, dtype=np.int64),
                                 gpio_dout=np.array(dataset_metadata.channel_metadata.index(
                                     SignalType.DOUT).ntv, dtype=np.int64),
                                 )
        elif not isinstance(sig_sel, SIG_SELECT):
            raise ValueError("sig_sel must be None or SIG_SELECT")
        elif sig_sel.key_idx not in [KeyIndex.NTV]:
            raise ValueError("sig_sel must use KeyIndex.NTV as the key index")
        samp_freq = time_range.fs if samp_freq is None else samp_freq
        req = common_pb2.PSDRequest(
            tR=time_range_to_protobuf(time_range),
            selMode=int(sel_mode.value),
            ntvIdxs=sig_sel.amp,
            stype=SignalType.AMP.value,
            resampleFs=samp_freq,
            wdwType=window.value,
            scaling=scaling.value,
            freqRange=freq_range,
            deltaFreq=freq_resolution,
            collapseFreq=collapse_freq,
            path=file,
            isReturnPSD=data,
        )
        if self._is_allego():
            req.dsourceID = PRIMARY_CACHE_STREAM_GROUP_ID
            return api_allego.get_psd(RadiensService.CORE, req)
        else:
            req.dsourceID = dataset_metadata.attributes["dsource_id"]
            return api_videre.get_psd(
                self.__parent._server_address(
                    hub_name, RadiensService.CORE), req
            )
