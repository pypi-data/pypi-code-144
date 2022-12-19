from dataclasses import dataclass

from telebox.bot.types.type import Type


@dataclass(unsafe_hash=True)
class MaskPosition(Type):
    point: str
    x_shift: float
    y_shift: float
    scale: float
