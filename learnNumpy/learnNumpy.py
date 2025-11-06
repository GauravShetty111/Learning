import numpy as np

array_1d = np.array([1,2,3,4,5])  # 1_D Array

print(type(array_1d))

array_2d = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(type(array_2d))

array_3d = np.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]])
print(type(array_3d))

# Suppose You have 2 dtypes int and float and u do some operation combining this two
#  then the output will be the type which both can be converted to without any loss 

int_arr = np.array([1,2,3],dtype=np.uint32)
float_arr = np.array([1.1,2.2,3.3],dtype=np.float32)
diff_result = float_arr-int_arr
print(array_3d.ndim)
# ndim is to find Dimensions

# 1D array Creations
range_arr = np.arange(0,11,1,dtype=float)
print(range_arr)

linear_space = np.linspace(0, 2, 5)  # linspace is use to divide two boundries into equal parts
print(linear_space)


# --------------2D Array ------------------

list_arr = [1,2]
identity_matrix = np.eye(3,3) #Create a 2D Identity Matrix
print(list_arr)
# print(list_arr.shape) 

diag_matrix =np.diag([1,2,3,4]) #Places this values into a Diagonal Matrix
print(diag_matrix)

vander_dec = np.vander(linear_space,5) # Decreasing 
print(vander_dec)
vander_inc = np.vander(linear_space,5,increasing=True) # Increasing
print(vander_inc)

zero_matrix = np.zeros((2,3)) #zero matrix of dim 2x3
print(zero_matrix)
ones_matrix = np.ones((2,3)) #ones matrix of dim 2x3
print(ones_matrix)

random_matrix = np.random.rand(2,3) 
print(random_matrix)

indices_grid = np.indices((3,3))
print(indices_grid)
block_a = np.ones((2, 2))
block_b = np.eye(2, 2)
block_c = np.zeros((2, 2))
block_d = np.diag((-3, -4))

block_matrix = np.block([[block_a,block_b],[block_c,block_d]])
print(block_matrix)


original_arr = np.array([1,2,3,4,5,6])
view_slice = original_arr[:3]
original_arr[1] = 10
print(original_arr)
print(view_slice)
view_slice+=1
print(view_slice)

copy_slice = original_arr[:3].copy()
original_arr[2] = 20
print(view_slice)
print(copy_slice)

float_converted =copy_slice.astype(np.float32)

print(float_converted.dtype)

string_bytes = np.array(['Hey','Gaurav'],dtype='S7').tobytes()
print(string_bytes)


flat_arr = np.array([1,2,3,4,5,6])
reshaped_arr = flat_arr.reshape((3,2))
print(reshaped_arr)
print("Nothing")