# Practice Problems for Research 
# Learning numpy and sklearn
# Step 1: Install and import sklearn/numpy packages
import numpy as np
import sklearn
import math

def main():
    # Step 2: Create an array of integers from 1 to 10
    array1 = np.arange(1, 11) # Creates a one dimensional array from 0 to 9
    print(array1)

    # Step 3: Create a 3-by-3 array of 1's
    array2 = np.ones(9).reshape(3,3)
    print(array2)

    # Step 4: Extract all odd numbers from an array
    # Using array1 from above
    condition = np.mod(array1, 2) != 0 # mod just does modulus %
    new_array = np.extract(condition, array1) # Extract uses a condition, and input array
    print(new_array)

    # Step 5: Replace all numbers in an array with -1
    # Using array2 from above
    array2[array2 != -1] = -1 # Uses numpy built in subscript to replace all numbers with -1
    print(array2)

    # Step 6: Convert a 1-D array of integers from 1 to 10 into a 2-b-5 matrix
    # Using array1 from above
    rearranged_array = array1.reshape(2,5)
    print(rearranged_array)

    # Step 7: Create two 2-by-5 matrices and "stack" them into on 4-by-5 matrix
    arr1 = np.arange(1, 11).reshape(2,5)
    arr2 = np.arange(1, 11).reshape(2,5)
    stacked_array = np.concatenate((arr1, arr2), axis=0) # The axis is for how they are stacked
    print(stacked_array)

    # Step 8: Create two 2-by-5 matrices and "stack" them into a 2-by-10 matrix
    # Using arr1 and arr2 from above
    other_stacked_array = np.concatenate((arr1, arr2), axis=1)
    print(other_stacked_array)

    # Step 9: Create two different arrays and find all common elements
    arr3 = np.arange(1, 11)
    arr4 = np.arange(5, 16)
    arr5 = np.intersect1d(arr3, arr4)
    print(arr5)

    # Step 10: Create two different arrays and find the indices of common elements
    # Using arr3 and arr4 from above
    arr6 = np.intersect1d(arr3, arr4, return_indices=True)
    print(arr6) # Intersect returns (arr3 U arr4, ind_arr3, ind_arr4)

    # Step 11: Create two different arrays and find all elements which appear in
    # at most one of them
    # Using arr3 and arr4 from above
    arr7 = np.setdiff1d(arr3, arr4)
    print(arr7)

    # Step 12: Extract all numbers which lie in the range(a,b) from an array
    # Using arr3 from above
    new_arr1 = arr3[(arr3 > 1) & (arr3 < 5)] # Extracting all elements between 1 and 5 exclusive
    print(new_arr1)

    # Step 13: Extract a whole column from a numpy matrix 
    array3 = np.arange(1, 10).reshape(3,3)
    first_column = array3[:, 0] # Just takes the first column but flattens it
    first_third_column = array3[:, [0, 2]] # Takes the first and third columns in column format
    print(first_column)
    print(first_third_column)

    # Step 14: Extract a whole row from a numpy matrix
    # Using array3 from above
    first_row = array3[0,:] # Takes the first row of the matrix
    second_third_row = array3[[1, 2],:] # Takes the second and third row in row format
    print(first_row)
    print(second_third_row)

    # Step 15: Swap two columns in a numpy matrix
    # Using array3 from above
    array4 = np.arange(10, 19).reshape(3,3)
    print('Before:')
    print(array3, array4)
    temp = np.copy(array3[:, 0]) # Need to use copy here because the basic numpy slicing
    array3[:, 0] = array4[:, 0]  # doesnt create copies of the actual data, just a view
    array4[:, 0] = temp
    print('After')
    print(array3, array4)

    # Step 16: Create an array of 100 random floats drawn from a standard normal 
    # Gaussian distribution
    random_array = np.random.rand(100)
    print(random_array)

    # Step 17: Find the empirical mean, median, and standard deviation of an array of 
    # 100 random floats drawn from a standard normal (Gaussian) distribution
    # Using random_array from above
    mean = np.mean(random_array)
    median = np.median(random_array)
    standard_deviation = math.sqrt(np.mean(abs(random_array - np.mean(random_array))**2))
    print(f'Mean: {mean}\nMedian: {median}\nStandard Deviation: {standard_deviation}')

    # Step 18: Find the 5th and 95th percentiles in the random array
    # Using random_array from above
    print('5th percentile is ' + str(np.percentile(random_array, 5)))
    print('95th percentile is ' + str(np.percentile(random_array, 95)))

    # Step 19: Normalize the array so that all values lie in the range [0,1]
    # In this case the array is already normalized

    # Step 20: Bouncy Number problem

if __name__ == '__main__':
    main()
