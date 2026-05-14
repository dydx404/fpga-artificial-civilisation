"""Agent encodings used by Python and mirrored by the RTL scaffold."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class Strategy(IntEnum):
    """Strategy IDs shared with the FPGA packed word format."""

    COOPERATE = 0
    DEFECT = 1
    TIT_FOR_TAT = 2
    RANDOM = 3


STRATEGY_NAMES = {
    Strategy.COOPERATE: "cooperate",
    Strategy.DEFECT: "defect",
    Strategy.TIT_FOR_TAT: "tit_for_tat",
    Strategy.RANDOM: "random",
}


@dataclass(frozen=True)
class AgentSnapshot:
    """Debug-friendly single-cell view of the vectorised world state."""

    strategy: Strategy
    payoff: float
    energy: float
    age: int


def strategy_name(strategy: int) -> str:
    """Return a stable display name for a strategy integer."""

    try:
        return STRATEGY_NAMES[Strategy(int(strategy))]
    except ValueError:
        return f"unknown_{strategy}"


def pack_agent_word(
    strategy: int,
    energy_class: int = 0,
    age_class: int = 0,
    flags: int = 0,
) -> int:
    """Pack a compact 8-bit agent word for the MVP RTL format.

    Layout:
        bits [1:0] strategy
        bits [3:2] flags/reserved
        bits [5:4] energy class
        bits [7:6] age class
    """

    return (
        (int(strategy) & 0b11)
        | ((int(flags) & 0b11) << 2)
        | ((int(energy_class) & 0b11) << 4)
        | ((int(age_class) & 0b11) << 6)
    )


def unpack_agent_word(word: int) -> dict[str, int]:
    """Unpack the 8-bit MVP agent word into named fields."""

    value = int(word) & 0xFF
    return {
        "strategy": value & 0b11,
        "flags": (value >> 2) & 0b11,
        "energy_class": (value >> 4) & 0b11,
        "age_class": (value >> 6) & 0b11,
    }

