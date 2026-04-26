# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import random
import json

class StorageConsensusRoll(gl.Contract):
    last_roll: str
    roll_count: u256
    last_status: str

    def __init__(self):
        self.last_roll = "never rolled"
        self.roll_count = 0
        self.last_status = "no attempt"

    @gl.public.write
    def roll_stable(self) -> None:
        """Always produces valid schema — should commit state."""

        def nondet_fn():
            return json.dumps({"roll": random.randint(1, 6)})

        def validator_fn(leader_result):
            try:
                raw = getattr(leader_result, "calldata", leader_result)
                parsed = json.loads(str(raw).strip())
                val = int(parsed["roll"])
                return 1 <= val <= 6
            except Exception:
                return False

        outcome = gl.vm.run_nondet_unsafe(nondet_fn, validator_fn)
        parsed = json.loads(str(outcome))
        self.last_roll = str(parsed["roll"])
        self.roll_count = self.roll_count + 1
        self.last_status = "success"

    @gl.public.write
    def roll_broken(self) -> None:
        """Always produces wrong schema key should fail consensus, no state commit."""

        def nondet_fn():
            return json.dumps({"value": random.randint(1, 6)})  # wrong key always

        def validator_fn(leader_result):
            try:
                raw = getattr(leader_result, "calldata", leader_result)
                parsed = json.loads(str(raw).strip())
                val = int(parsed["roll"])  # will always raise KeyError
                return 1 <= val <= 6
            except Exception:
                return False

        outcome = gl.vm.run_nondet_unsafe(nondet_fn, validator_fn)
        parsed = json.loads(str(outcome))
        self.last_roll = str(parsed["roll"])
        self.roll_count = self.roll_count + 1
        self.last_status = "success"

    @gl.public.view
    def get_state(self) -> str:
        return json.dumps({
            "last_roll": self.last_roll,
            "roll_count": str(self.roll_count),
            "last_status": self.last_status
        })
