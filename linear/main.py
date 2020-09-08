from gauss import Seidel

if __name__ == "__main__":
    
    exercise = [[10, 2, 1, 7],
                [1, 5, 1, -8],
                [2, 3, 10, 6]]

    Seidel(exercise, 0.0001)
    