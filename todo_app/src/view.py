from dataclasses import dataclass
from typing import ClassVar, Literal

from .trello import Item


@dataclass
class ViewModel:
    items: list[Item]
    done_status: ClassVar[Literal["Done"]] = "Done"

    @property
    def done_items(self):
        return filter(lambda item: item.status == self.done_status, self.items)

    @property
    def to_do_items(self):
        return filter(lambda item: item.status != self.done_status, self.items)
