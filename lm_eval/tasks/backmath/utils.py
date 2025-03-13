from typing import Dict, List
import re

try:
    from math_verify import parse, verify
except (ModuleNotFoundError, AssertionError) as e:
    raise type(e)(
        "`sympy`, `math_verify` and `antlr4-python3-runtime==4.11` are required for generating translation task prompt templates. "
        "Please install the required packages via pip install lm-eval[math] or pip install -e .[math]"
    ) from e

import datasets



def process_results(doc: dict, results: List[str]) -> Dict[str, int]:
    candidates = results[0][0]

    # math_verify
    out = doc["reverse_solution"]
    # out = re.sub(r"\\\\\\\\", r"\\", out).replace("\\\\end", "\\end")

    # print(out, candidates)
    res = verify(parse(out), parse(candidates))
    mathval = 1 if res else 0

    results = {
        "math_verify": mathval,
    }
    return results