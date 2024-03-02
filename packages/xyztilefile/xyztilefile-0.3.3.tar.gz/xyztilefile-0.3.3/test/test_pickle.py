import pprint
import numpy as np
from xyztilefile import *

pp = pprint.PrettyPrinter(indent=3)

x, y, z = calc_xyz_from_lonlat(135.0,35.0,15)
xyz = calc_xyz_from_lonlat

data = {"var":[1,2,3]}
print("Initial")
try:
    test = XYZTileFile("./tile_sample2/{z}/{x}/{y}.pkl")#, allow_pickle=True)
    pp.pprint(test)

    print()
    print("Set data")
    test.set(x,y,z,data)
    pp.pprint(test)

    print()
    print("Save & clear cache")
    test.save(x,y,z)
    test.clc()
    pp.pprint(test)

    print()
    print("Load the saved data")
    data2 = test.get(*xyz(135.0,35.0,15))
    pp.pprint(data2)
    pp.pprint(test)
except RuntimeError as e:
    print(f"RuntimeError is detected as expected: {e}")

print()
print("Testing HTTP npy")
try:
    test_http = XYZTileFile("https://raw.githubusercontent.com/aDAVISk/xyztilefile/dev/tile_sample/{z}/{x}/{y}.pkl")
    pp.pprint(test_http)
except NotImplementedError as e:
    print(f"NotImplementedError is detected as expected: {e}")
