"""PYNQ-side configuration helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OverlayConfig:
    """Runtime configuration for the FPGA spatial game dynamics overlay."""

    bitstream_path: str = "spatial_game_engine.bit"
    width: int = 128
    height: int = 128
    mutation_probability: float = 0.001
    payoff_r: int = 3
    payoff_s: int = 0
    payoff_t: int = 5
    payoff_p: int = 1

    @property
    def mutation_threshold_u16(self) -> int:
        """Convert probability to a 16-bit hardware threshold."""

        probability = min(max(self.mutation_probability, 0.0), 1.0)
        return int(round(probability * 65535))
