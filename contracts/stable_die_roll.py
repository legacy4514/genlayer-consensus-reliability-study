# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import random

class StableDieRoll(gl.Contract):
    result: str

    def __init__(self):
        self.result = "not rolled yet"

    @gl.public.write
    def roll(self) -> None:
        def nondet_fn():
            return str(random.randint(1, 6))

        def validator_fn(leader_result):
            try:
                # handle Return-like object or plain value
                value = getattr(leader_result, "calldata", leader_result)
                val = int(str(value).strip())
                return 1 <= val <= 6
            except (ValueError, TypeError):
                return False

        outcome = gl.vm.run_nondet_unsafe(nondet_fn, validator_fn)
        self.result = str(outcome)

    @gl.public.view
    def get_result(self) -> str:
        return self.result