# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import random
import json

class BrokenSchemaRoll(gl.Contract):
    result: str
    breach_count: u256
    accept_count: u256

    def __init__(self):
        self.result = "not rolled yet"
        self.breach_count = 0
        self.accept_count = 0

    @gl.public.write
    def roll(self) -> None:

        def nondet_fn():
            roll = random.randint(1, 6)
            # 50% chance of producing wrong schema key
            if random.random() < 0.5:
                return json.dumps({"value": roll})   # ❌ wrong key — should be "roll"
            else:
                return json.dumps({"roll": roll})    # ✅ correct schema

        def validator_fn(leader_result):
            try:
                raw = getattr(leader_result, "calldata", leader_result)
                parsed = json.loads(str(raw).strip())
                # Strictly enforce the schema — only "roll" key is valid
                val = int(parsed["roll"])
                return 1 <= val <= 6
            except Exception:
                return False

        outcome = gl.vm.run_nondet_unsafe(nondet_fn, validator_fn)
        self.result = str(outcome)

    @gl.public.view
    def get_result(self) -> str:
        return self.result