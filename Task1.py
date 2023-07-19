class Matrix:
    def __init__(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise ValueError("Размеры матрицы должны быть положительными числами.")
        
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]
    
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Нельзя сложить матрицу с объектом другого типа.")
        
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        
        return result
    
    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Нельзя умножить матрицу на объект другого типа.")
        
        if self.columns != other.rows:
            raise ValueError("Число столбцов первой матрицы должно совпадать с числом строк второй матрицы.")
        
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        
        return result

class MatrixSizeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MatrixAdditionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MatrixMultiplicationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]
    
    matrix2 = Matrix(2, 3)  
    
    matrix3 = Matrix(2, 3)
    matrix3.data = [[7, 8, 9], [10, 11, 12]]
    
    matrix4 = Matrix(3, 2)
    matrix4.data = [[1, 2], [3, 4], [5, 6]]
    
    matrix5 = Matrix(2, 3)
    matrix5.data = [[1, 2, 3], [4, 5, 6]]
    
    print(matrix1)
    print(matrix2)
    print(matrix3)
    print(matrix4)
    print(matrix5)
    
    print(matrix1 == matrix2)  
    
    result = matrix1 + matrix3  
    
    result = matrix4 * matrix5  
    
except MatrixSizeError as e:
    print("Ошибка с размерами матрицы:", e.message)
except MatrixAdditionError as e:
    print("Ошибка при сложении матриц:", e.message)
except MatrixMultiplicationError as e:
    print("Ошибка при умножении матриц:", e.message)