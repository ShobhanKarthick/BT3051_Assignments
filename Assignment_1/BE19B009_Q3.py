import numpy as np

def pascals_triangle(n):
    # Elements of triangle can be calculated using combinations
    for i in range(n):
        for j in range(i):
            print(int(np.math.factorial(i)/((np.math.factorial(i-j)*np.math.factorial(j)))), end=" ")
        print(int(1), end=" ")
        print()

if __name__ == "__main__":
    fin = open("q3_test.txt")
    n = int(fin.read().splitlines()[0])
    fin.close()

    a = pascals_triangle(n)
