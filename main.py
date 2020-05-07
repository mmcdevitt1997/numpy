import numpy as np

# insert print statement to see the output of a command

# creating numpy array

my_list = [1,2,3]

x = np.array(my_list)

type(x)

my_matrix = [[1,2,3], [1,2,3], [1,2,3]]

np.array(my_matrix)

np.arange(1,11,2)

np.zeros(2)

np.linspace(0,10,30)

np.eye(4)

np.random.rand(1)

np.random.randn(3)

np.random.randint(1, 1000)

arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

arr.reshape(5,5)

ranarr.max()