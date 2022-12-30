import numpy as np

a = np.arange(25).reshape((5, 5))
print(a)

for row in a:
    nums = ",".join([str(v) for v in row])
    print("{" + nums + "}")