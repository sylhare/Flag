import os

from PIL import Image

catchat = os.path.join(os.getcwd(), "/FLAG-bXlyZXBvc2l0b3J5dG9maW5kZmxhZ3M/NSEC2019/catchat")

i1 = Image.open(os.path.join(catchat, "samples/animals/dog6.png"))
i2 = Image.open(os.path.join(catchat, "samples/animals/dog6-bis.png"))
assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."

pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1 - p2) for p1, p2 in pairs)
else:
    dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

ncomponents = i1.size[0] * i1.size[1] * 3

if __name__ == '__main__':
    print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)