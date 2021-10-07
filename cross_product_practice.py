import numpy as np
import random

while True:
    nums = random.sample(range(10), 6)
    u = np.array(nums[:3])
    v = np.array(nums[3:])

    product = np.cross(u, v)

    print(f"{list(u)} x {list(v)}\n")

    input("X coordinate: ")
    print(f"({u[1]})({v[2]}) - ({u[2]})({v[1]}) = {product[0]}\n")

    input("Y coordinate: ")
    print(f"({u[2]})({v[0]}) - ({u[0]})({v[2]}) = {product[1]}\n")

    input("Z coordinate: ")
    print(f"({u[0]})({v[1]}) - ({u[1]})({v[0]}) = {product[2]}\n")

    print(f"Answer:\n{list(product)}")

    input("\n\n\nSee next problem:   ")
