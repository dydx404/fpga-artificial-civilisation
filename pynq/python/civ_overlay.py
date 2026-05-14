"""PYNQ overlay wrapper for the civilisation engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from config import OverlayConfig
from dma_interface import DmaFrameInterface, pack_strategy_frame, unpack_strategy_frame

try:
    from pynq import Overlay  # type: ignore
except ImportError:  # pragma: no cover - expected on non-PYNQ machines
    Overlay = None  # type: ignore


@dataclass
class CivOverlay:
    """Control-plane wrapper for the future FPGA engine."""

    config: OverlayConfig = field(default_factory=OverlayConfig)
    dry_run: bool = True
    overlay: Any | None = None
    dma_interface: DmaFrameInterface = field(init=False)

    def __post_init__(self) -> None:
        self.dma_interface = DmaFrameInterface(dry_run=self.dry_run)

    def load(self) -> None:
        """Load the bitstream when running on a PYNQ board."""

        if self.dry_run:
            return
        if Overlay is None:
            raise RuntimeError("pynq is not installed; use dry_run=True off-board")
        self.overlay = Overlay(self.config.bitstream_path)
        # TODO: bind self.dma_interface.dma to the overlay DMA IP.

    def configure_registers(self) -> None:
        """Write control registers once the IP wrapper exists."""

        if self.dry_run:
            return
        # TODO: write AXI-lite registers for dimensions, payoff, and mutation.
        raise NotImplementedError("register map is not implemented yet")

    def step_frame(self, strategies: np.ndarray) -> np.ndarray:
        """Run one frame through the FPGA path or dry-run loopback."""

        packed = pack_strategy_frame(strategies)
        result = self.dma_interface.transfer_frame(packed)
        return unpack_strategy_frame(result, self.config.height, self.config.width)

