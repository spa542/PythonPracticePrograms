from sklearn.decomposition import fastica # FastICA algorithm
import numpy as np # Numpy Arrays
import matplotlib.pyplot as plt # Used for plotting numpy arrays
from numpy import linalg as la # Used for finding the eigen values and vectors of a numpy array
import matplotlib.pyplot as plt # Used for graphing
import math # Using math function
from itertools import permutations # For finding permutations of a matrix
import csv # Writes output to a csv file

# Function used to normalize the columns to unit length so they can be compared easily
def normalize_cols(A):
    '''
    Normalizes the columns of a matrix to be unit length
    '''
    norms = la.norm(A,axis=0)
    return A / np.tile(norms,(2,1))

# calc_difference function using the frobenius distance
def calc_difference(A, B):
    '''
    Calculates the difference between two matrices by using the Frobenius norm
    formula
    '''
    first = np.subtract(A, B)
    second = np.subtract(A, B).conj().T
    inner = np.dot(first, second) # first @ second
    trace = inner.trace()
    return math.sqrt(trace)

# Creating a function to reduce the error between the estimated matrix and the original matrix
def reduce_error(original, fix):
    '''
    Uses a permutation to find the correct format for fix to calculate the smallest
    distance between fix and original
    '''
    min_fix = np.arange(1)
    identity = np.eye(len(original[:,0]))
    permList = list(permutations(identity))
    minimum_error = 100000
    for item in permList:
        matrix = np.array(item)
        orig_mat = matrix
        for num in range(2**len(original[:,0])):
            matrix = np.copy(orig_mat)
            bi = "{:02b}".format(num) # Is a string that needs to be parsed
            if (bi[0] == '1'):
                matrix[:,0] *= -1
            if (bi[1] == '1'):
                matrix[:,1] *= -1

            matrix[matrix == -0] = 0 # Fix -0

            check = fix @ matrix
            difference = calc_difference(original, check)
            if (difference < minimum_error):
                minimum_error = difference
                min_fix = np.copy(matrix @ fix)

    return (minimum_error, min_fix)

def write_to_csv(testCases, errorAverage):
    '''
    Takes each test case and the each average corresponding error value and
    puts them into a csv file to be graphed
    --Must enter two lists of the same size
    '''
    with open('grapherror.csv', mode='w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Test Cases","Error Averages"])
        for index, item in enumerate(testCases):
            errorVal = errorAverage[index]
            testVal = item
            csv_writer.writerow([testVal,errorVal])

    print('CSV file created successfully')



def main():
    testCases = [1000, 5000, 10000, 20000, 35000, 50000, 65000, 80000, 100000]
    errorAverage = [] # Parallel list that corresponds to each number of test cases
    errorList = []

    for testSize in testCases:
        for i in range(25):
            N = testSize # Amount of instances

            # Uncomment one to use a different distribution!!
            S = np.random.gamma(1, scale=1.0, size=(2,N)) # Matrix consisting of a random gamma distribution from [0,1)
            #S = np.random.laplace(loc=0.0, scale=1.0, size=(2,N)) # Matrix consisting of a laplace random distribution from [0,1)
            #S = np.random.logistic(loc=0.0, scale=1.0, size=(2,N)) # Matrix consisting of a logistic random distribution from [0,1)
            #S = np.random.gumbel(loc=0.0, scale=1.0, size=(2,N)) # Matrix consisting of a gumbel random distribution from [0, 1)
            #S = np.random.uniform(low=-1.0, high=1.0, size=(2,N)) # Matrix consisting of a uniform random distribution from [0, 1)

            A = normalize_cols(np.random.normal(loc=0.0, scale=1.0, size=(2,2))) # Matrix consisting of a 2 by 2 Matrix, the mixing matrix

            X = np.matmul(normalize_cols(A), S) # 2 by N matrix that we are given and need to solve for 

            # First step: Subtract off the mean of the data in each dimension to make it a zero mean variable
            X = np.subtract(X, np.mean(X)) # Subtracting the mean from every value of X

            # Compute the Covariance of X
            covX = (1/N) * np.matmul(X, X.transpose())

            # Second step: Whiten the data by calculating the eigenvectors and eigenvalues of the covariance of the data
            eigvals, eigvecs = la.eig(covX) # Unpacking the tuple returned
            eigVec1 = eigvecs[:,0].reshape(2,1)
            eigVec2 = eigvecs[:,1].reshape(2,1)
            E = np.concatenate((eigVec1, eigVec2), axis=1) # Creating the E matrix of corresponding eigen vectors
            Einv = la.inv(E) # Create the Inverse of the eigen vector matrix
            Etrans = E.transpose() # Create the Transpose matrix of the eigen vector matrix
            D = np.diag(eigvals) # Create the Diagonal matrix of eigen values

            # Continued... Applying the full calculation with all metadata calculated
            presWhite = np.matmul(np.sqrt(la.inv(D)), Etrans)
            Xwhite = np.matmul(presWhite, X)

            # Third step: Identify final rotation matrix that optimizes statistical independence
            _, W, Sest = fastica(Xwhite.T, fun='cube', whiten=False)
            # Recall that X = AS; ica computes K and W (whitening and de-rotating, resp.) so that 
            # S = W K X => Winv S = K X => Kinv Winv S = X = AS => Kinv Winv = A => (W K)inv = A

            # Printing out the comparison between A and W * Wpres
            graphW = normalize_cols(la.inv(W @ presWhite))
            graphA = normalize_cols(A)

            final_error, min_fix = reduce_error(graphA, graphW)

            errorList.append(final_error)

        sum = 0
        for item in errorList:
            sum += item

        errorAverage.append(sum / 25)
        errorList[:] = []

    for i in range(9):
        print(f'{testCases[i]} --> {errorAverage[i]}')

    print('Creating CSV file with printed values')
    write_to_csv(testCases, errorAverage)
    print('X-axis: Test Values Y-axis: Error Averages')



if __name__ == '__main__':
    main()
