import numpy as np 
array1 = np.random.randint(1,11,size=(2,3))
print ("o arxikos pinakas ths askhshs einai \n " + str(array1) )
array_multiplied_by2 = 2*array1
print ( "epi 2 to arxiko mhtrwo einai \n" + str(array_multiplied_by2))
total_sum = np.sum(array_multiplied_by2)
print (total_sum)
mean_value= np.mean(array_multiplied_by2)
minimum_value = np.min(array_multiplied_by2)
maximum_value = np.max(array_multiplied_by2)
print(f"max is {maximum_value}, min is {minimum_value}, mean is { mean_value}")
