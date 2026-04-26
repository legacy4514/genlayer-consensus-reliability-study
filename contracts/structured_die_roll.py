# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import random
import json

class StructuredDieRoll(gl.Contract):
    result: str

    def __init__(self):
        self.result = "not rolled yet"

    @gl.public.write
    def roll(self) -> None:

        def nondet_fn():
            roll = random.randint(1, 6)
            return json.dumps({"roll": roll})

        def validator_fn(leader_result):
            try:
                raw = getattr(leader_result, "calldata", leader_result)
                parsed = json.loads(str(raw).strip())
                val = int(parsed["roll"])
                return 1 <= val <= 6
            except Exception:
                return False

        outcome = gl.vm.run_nondet_unsafe(nondet_fn, validator_fn)
        self.result = str(outcome)

    @gl.public.view
    def get_result(self) -> str:
        return self.result