from dataclasses import dataclass

from .localns_a import AA  # would like to keep AA import as global


@dataclass
class BB:
    name: str

    @classmethod
    def shared_function(cls):
        AA.shared_function()  # need to use AA in multiple places of bb.py

    @classmethod
    def config(
        cls,
    ):
        return {"x": "y"}
