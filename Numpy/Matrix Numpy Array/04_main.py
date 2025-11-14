import numpy as np
np.set_printoptions(precision=2)

Value_1 = np.matrix([[20, 47], [2, 100]])
Value_2 = np.matrix([[96, 45], [10, 4]])

result = Value_1 / Value_2
print(f"Division Value_1 / Value_2: \n{result}")