import random
import math
from typing import Self

class Vec:

    def __init__(self, src=None) -> Self:
        """
        The constructor that instanciates the Vector instance.
        
        Args;
            src (Iterable[int | float]): The iterable numeric values
        """
        if not src:
            raise TypeError("Vector connot be empty!!")
        else:
            elements = tuple(src)

            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be of type int or float: {type(x)}")
        self.elements = elements

    def __repr__(self) -> str:
        """
        String representation of the vector

        Returns:
            str (str): String representation of the elements tuple
        """
        return repr(self.elements)

    def __len__(self) -> int:
        """
        The dimention of the vector

        Returns:
            dimention (int): The dimention of the vector
        """
        return len(self.elements)

    def __neg__(self) -> Self:
        """
        The negation of the Vector

        Returns:
            Self: A vector instance with thw negated value
        """
        neg = []
        for x in self.elements:
            neg.append(-x)
        return Vec(neg)

    def __add__(self, t: Self) -> Self:
        """
        Addition of 2 vectors of the same dimentions.

        Args:
            t (Self): A vector to add to the instance.

        Returns:
            Self: A new Vector that has element wise sums.
        """
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")

        if len(self.elements) != len(t.elements):
            raise TypeError(f"The vectors must be for the same dimentions")

        result = []
        for x, y in zip(self.elements, t.elements):
            rounded = round(x + y, 5)
            result.append(rounded)
        return Vec(result)
    
    def __sub__(self, t: Self) -> Self:
        """
        Substraction of 2 vectors of the same dimentions.

        Args:
            t (Self): A vector to substract to the instance.

        Returns:
            Self: A new Vector that has element wise substraction.
        """
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")

        if len(self.elements) != len(t.elements):
            raise TypeError(f"The vectors must be for the same dimentions")

        result = []
        for x, y in zip(self.elements, t.elements):
            rounded = round(x - y, 5)
            result.append(rounded)
        return Vec(result)

    def __rmul__(self, scalar: int | float) -> Self:
        """
        Multiplies the each element of the vector by a given scalar numeric value.

        Args:
            scalar (int | float): The scalar value.

        Returns:
            Self: A new Vector that has been multiplied by the scalar value.
        """
        if not isinstance(scalar, int | float):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        result = []
        for x in self.elements:
            rounded = round(x * scalar, 5)
            result.append(rounded) 
        return Vec(result)

    def __imul__(self, scalar: int | float) -> Self:
        """
        Multiplies and mutates the each element of the vector by a given scalar numeric value.

        Args:
            scalar (int | float): The scalar value.

        Returns:
            Self: A mutated Vector that has been multiplied by the scalar value.
        """
        if not isinstance(scalar, int | float):
            raise TypeError(f"Vector multiplication with invalid types: {type(scalar)}")

        result = []
        for x in self.elements:
            rounded = round(x * scalar, 5)
            result.append(rounded)
        self.elements = tuple(result)
        return self

    def __radd__(self, scalar: int | float) -> Self:
        """
        Adds the each element of the vector by a given scalar numeric value.

        Args:
            scalar (int | float): The scalar value.

        Returns:
            Self: A new Vector that has been added by the scalar value.
        """
        if not isinstance(scalar, int | float):
            raise TypeError(f"Vector multiplication with invalid types: {type(scalar)}")

        result = []
        for x in self.elements:
            rounded = round(x + scalar, 5)
            result.append(rounded)
        return Vec(result)

    def __iadd__(self, scaler: int | float) -> Self:
        """
        Adds and mutates the each element of the vector by a given scalar numeric value.

        Args:
            scalar (int | float): The scalar value.

        Returns:
            Self: A mutated Vector that has been added by the scalar value.
        """
        if not isinstance(scaler, int | float):
            raise TypeError(f"Vector multiplication with invalid types: {type(scalar)}")

        result = []
        for x in self.elements:
            rounded = round(x + scaler, 5)
            result.append(rounded)
        self.elements = tuple(result)
        return self

    @staticmethod
    def zeros(n: int) -> Self:
        """
        Static method that generates a n-dimention vector of zeros.

        Args:
            n (int): The dimention the the zeros vector.

        Returns:
            Vec: zero vector of n-dimention.
        """
        if n <= 0:
            raise ValueError("The value of the dimention must be positive")
        return Vec([0] * n)


    @staticmethod
    def ones(n: int) -> Self:
        """
        Static method that generates a n-dimention vector of ones.

        Args:
            n (int): The dimention of the ones vector.

        Returns:
            Vec: ones vector of n-dimention.
        """
        if n <= 0:
            raise ValueError("The value of the dimention must be positive")
        return Vec([1] * n)

    @staticmethod
    def uniform(n: int) -> Self:
        """
        Static method that generates a n-dimention vector of uniformly distributed numbers in [0, 1].

        Args:
            n (int): The dimention of the ones vector.

        Returns:
            Vec: n-dimention vector Uniformly distributed numbers in [0, 1].
        """
        if n <= 0:
            raise ValueError("The value of the dimention must be positive")
        result = []
        for i in range(n):
            result.append(round(random.uniform(0, 1), 5))
        return Vec(result)

    @staticmethod
    def norm(self: Self) -> float:
        """
        Static method that calculates the Euclidean norm (L2 norm) of the vector.
        sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)

        Args:
            Vec: The vector to calculate the Eucildean norn(L2 Norm).

        Returns:
            L2Norm (float): sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
        """
        sumSquare = 0
        for x in self.elements:
            sumSquare += x**2
        return math.sqrt(sumSquare)

if __name__ == "__main__":
    v1 = Vec([1, 2, 3])
    v2 = Vec([3, 5, 6])

    print(v1)
    print(v2)

    v3 = -v1
    print(v3)

    print(type(v1))
    print(type(v2.elements))

    v4 = v1 + v2
    print(v4)

    v5 = v1 - v2
    print(v5)

    v6 = 5 * v5
    print(v6)

    v6 *= 67
    print(v6)

    v7 = 5 + v6
    print(v7)

    v7 += 67
    print(v7)

    print(Vec.zeros(6))
    print(Vec.ones(7))
    print(Vec.uniform(3))

    v8 = Vec([-3, 2, -1, 1, -1])
    print(Vec.norm(v8))

    v9 = Vec(67)
    print(v9)
