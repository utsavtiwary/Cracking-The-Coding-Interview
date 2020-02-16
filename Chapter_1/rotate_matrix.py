# Given an N x N image matrix, rotate the image by 90 degrees

import numpy as np

def rotate_matrix(matrix):
    N = matrix.shape[0]

    # Loop through top, right, bottom, left layer by layer till inner most
    for i in range(N // 2):
        for j in range(i, N-i-1):
            # Intuitive reasoning behind mapping of top -> right -> bottom -> left -> top
            top_i, top_j = i, j
            right_i, right_j = j, N-i-1
            bottom_i, bottom_j = N-i-1, N-j-1
            left_i, left_j = N-j-1, i

            # Make use of Python's multiple assignments functionality and update values in place
            matrix[top_i, top_j], matrix[right_i, right_j], matrix[bottom_i, bottom_j], matrix[left_i, left_j] = \
                matrix[left_i, left_j], matrix[top_i, top_j], matrix[right_i, right_j], matrix[bottom_i, bottom_j]

    return matrix

if __name__ == "__main__":
    # TEST
    input_matrix = np.arange(1, 122).reshape(11, 11)
    print("INPUT:\n", input_matrix)

    output_matrix = rotate_matrix(input_matrix)
    print("OUTPUT\n", output_matrix)