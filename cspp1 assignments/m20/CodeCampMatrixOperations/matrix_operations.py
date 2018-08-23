def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    final_list1 = []
    rows_m1 = len(m1)
    rows_m2 = len(m2)
    columns_m1 = len(m1[0])
    columns_m2 = len(m2[0])
    if columns_m1 == rows_m2:
        for i in range(rows_m1):
            result_mult = []
            for j in range(columns_m1):
                sum_a = 0
                for k in range (rows_m2):
                    sum_a += int(m1[i][k]) * int(m2[k][j])
                result_mult.append(sum_a)
            final_list1.append(result_mult)
        return final_list1

    else:
        print("Error: Matrix shapes invalid for mult")





def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
    final_list = []
    rows_m1 = len(m1)
    rows_m2 = len(m2)
    columns_m1 = len(m1[0])
    columns_m2 = len(m2[0])
    if rows_m1 == rows_m2 and columns_m1 == columns_m2:
        for i in range(rows_m1):
            result_add = []
            for j in range(columns_m1):
                result_add.append(int(m1[i][j]) + int(m2[i][j]))
            final_list.append(result_add)
    else:
        print("Error: Matrix shapes invalid for addition")

    return final_list
    # print(result_add)

    

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    try:
        dimensions_matrix = input().split(",")
        row = int(dimensions_matrix[0])
        columns = int(dimensions_matrix[1])
        list_matrix = []
        for i in range(row):
            # print("entered")
            row_input = input().split(' ')
            list_matrix.append(row_input)
        return list_matrix
    # print(list_matrix)
    except:
        print("Error: Invalid input for the matrix")

def main():
    # read matrix 1
    matrix_1 = read_matrix()
    # print(matrix_1)
    # read matrix 2
    matrix_2 = read_matrix()
    # print(matrix_2)
    # add matrix 1 and matrix 2
    print(add_matrix(matrix_1, matrix_2))


    # multiply matrix 1 and matrix 2
    print(mult_matrix(matrix_1, matrix_2))

if __name__ == '__main__':
    main()
