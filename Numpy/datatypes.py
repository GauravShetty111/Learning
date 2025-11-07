import numpy as np

# Creating arrays of different dimensions
array_1d = np.array([1,2,3,4,5])  # 1D Array - single row
print(type(array_1d))  # All NumPy arrays are ndarray type

array_2d = np.array([[1,2,3,4,5],[1,2,3,4,5]])  # 2D Array - matrix
print(type(array_2d))

array_3d = np.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]])  # 3D Array - cube
print(type(array_3d))

# Data type promotion: combining int and float results in float (no data loss)
int_arr = np.array([1,2,3],dtype=np.uint32)  # 32-bit unsigned integers
float_arr = np.array([1.1,2.2,3.3],dtype=np.float32)  # 32-bit floats
diff_result = float_arr-int_arr  # Result is float32 (higher precision wins)

print(array_3d.ndim)  # ndim shows number of dimensions (3 for 3D array)

# 1D array creation methods
range_arr = np.arange(0,11,1,dtype=float)  # Creates [0,1,2...10] with step=1
print(range_arr)

linear_space = np.linspace(0, 2, 5)  # Creates 5 evenly spaced points from 0 to 2
print(linear_space)


# 2D Array creation methods
list_arr = [1,2]  # Regular Python list (no shape attribute)
identity_matrix = np.eye(3,3)  # 3x3 identity matrix (1s on diagonal, 0s elsewhere)
print(list_arr)
# print(list_arr.shape)  # Would error - lists don't have shape

diag_matrix = np.diag([1,2,3,4])  # Creates diagonal matrix with these values
print(diag_matrix)

vander_dec = np.vander(linear_space,5)  # Vandermonde matrix: powers decrease left to right
print(vander_dec)
vander_inc = np.vander(linear_space,5,increasing=True)  # Powers increase left to right
print(vander_inc)

zero_matrix = np.zeros((2,3))  # 2x3 matrix filled with zeros
print(zero_matrix)
ones_matrix = np.ones((2,3))  # 2x3 matrix filled with ones
print(ones_matrix)

random_matrix = np.random.rand(2,3)  # 2x3 matrix with random values [0,1)
print(random_matrix)

indices_grid = np.indices((3,3))  # Creates coordinate grids for 3x3 shape
print(indices_grid)  # Returns [row_indices, col_indices] arrays

# Creating 2x2 blocks for matrix construction
block_a = np.ones((2, 2))      # Top-left: all ones
block_b = np.eye(2, 2)         # Top-right: identity
block_c = np.zeros((2, 2))     # Bottom-left: all zeros
block_d = np.diag((-3, -4))    # Bottom-right: diagonal with -3, -4

block_matrix = np.block([[block_a,block_b],[block_c,block_d]])  # Combines into 4x4 matrix
print(block_matrix)


# Views vs Copies demonstration
original_arr = np.array([1,2,3,4,5,6])
view_slice = original_arr[:3]  # Creates view (shares memory with original)
original_arr[1] = 10  # Changes original, affects view too
print(original_arr)
print(view_slice)  # Shows the change from original
view_slice+=1  # Modifying view also changes original
print(view_slice)

copy_slice = original_arr[:3].copy()  # Creates independent copy
original_arr[2] = 20  # Changes original, but copy is unaffected
print(view_slice)  # View reflects original changes
print(copy_slice)  # Copy remains unchanged

float_converted = copy_slice.astype(np.float32)  # Convert to float32 type
print(float_converted.dtype)  # Shows new data type

string_bytes = np.array(['Hey','Gaurav'],dtype='S7').tobytes()  # Convert strings to bytes
print(string_bytes)  # Shows byte representation with null padding


# Array reshaping
flat_arr = np.array([1,2,3,4,5,6])  # 1D array with 6 elements
reshaped_arr = flat_arr.reshape((3,2))  # Reshape to 3x2 matrix (same data)
print(reshaped_arr)
print("Array operations complete")