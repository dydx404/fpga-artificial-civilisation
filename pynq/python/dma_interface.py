"""Frame packing and DMA interface scaffolding."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np


def pack_strategy_frame(strategies: np.ndarray) -> np.ndarray:
    """Pack strategy IDs into MVP 8-bit agent words.

    Only bits [1:0] are populated for now. Energy and age classes remain zero.
    """

    strategies = np.asarray(strategies, dtype=np.uint8)
    return strategies & np.uint8(0b11)


def unpack_strategy_frame(agent_words: np.ndarray, height: int, width: int) -> np.ndarray:
    """Extract strategy IDs from a flat or 2D packed agent-word frame."""

    words = np.asarray(agent_words, dtype=np.uint8).reshape((height, width))
    return words & np.uint8(0b11)


@dataclass
class DmaFrameInterface:
    """Thin wrapper around PYNQ DMA objects.

    In dry-run mode, `transfer_frame` returns a copy of the input frame. This is
    useful for frontend and integration development before a bitstream exists.
    """

    dma: Any | None = None
    dry_run: bool = True

    def transfer_frame(self, packed_frame: np.ndarray) -> np.ndarray:
        """Transfer one frame through DMA or dry-run loopback."""

        packed_frame = np.asarray(packed_frame, dtype=np.uint8)
        if self.dry_run or self.dma is None:
            return packed_frame.copy()

        # TODO: allocate PYNQ buffers and call dma.sendchannel/recvchannel.
        raise NotImplementedError("real DMA transfer requires board-specific buffer setup")

