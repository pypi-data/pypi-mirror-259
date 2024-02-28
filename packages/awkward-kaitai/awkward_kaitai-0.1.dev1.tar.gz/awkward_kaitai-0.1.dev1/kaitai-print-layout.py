from __future__ import annotations

import sys

sys.path.append("local")
import awkward_kaitai
import numpy as np

testcase = sys.argv[1]

reader = awkward_kaitai.Reader(f"test_artifacts/lib{testcase}.so")
awkward_array = reader.load(f"example_data/data/{testcase}.raw")
print(awkward_array.layout)
