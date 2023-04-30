# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import math
import dip
from numpy import fft, array_equal, allclose
from dip import *

class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        forward_matrix = zeros((len(matrix), len(matrix[0])), dtype=complex)
        length = len(matrix[0])
        print(length)
        print(len(matrix))

        for u in range(length):
            for v in range(length):
                temp = 0
                for i in range(length):
                    for k in range(length):
                        angle = ((2*math.pi)/length)*(u*i + k*v)
                        temp += matrix[i][k] * (math.cos(angle) - (1j) * math.sin(angle))
                        
                forward_matrix[u][v] = temp
        ##
        dft = fft.fft2(matrix)
        truth = array_equal(forward_matrix, dft)
        truth2 = allclose(forward_matrix, dft)
        print(truth)
        print(truth2)


        return forward_matrix

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""

        inverse_matrix = zeros((len(matrix), len(matrix[0])), dtype=complex)
        length = len(matrix[0])
        print(length)

        for u in range(length):
            for v in range(length):
                temp = 0
                for i in range(length):
                    for k in range(length):
                        angle = ((2*math.pi)/length)*(k*v + i*u)
                        temp += matrix[i][k] * (math.cos(angle) + 1j * math.sin(angle))

                inverse_matrix[u][v] = temp/length**2
        inverse = fft.ifft2(matrix)
        truth = allclose(inverse_matrix, inverse)
        print(truth)

        return inverse_matrix

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""

        length = len(matrix[0])
        magnitude = zeros((length, length), dtype=int)

        for x in range(length):
            for y in range(length):
                real = matrix[x][y].real
                imaginary = matrix[x][y].imag
                dist = math.sqrt(real**2+imaginary**2)
                magnitude[x][y] = round(dist)

        return magnitude