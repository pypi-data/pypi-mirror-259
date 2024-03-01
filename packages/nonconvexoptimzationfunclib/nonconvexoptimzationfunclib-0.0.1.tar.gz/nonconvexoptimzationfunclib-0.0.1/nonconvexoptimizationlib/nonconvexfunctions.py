import math
import numpy as np

class NonconvexFunctions:
    class ContinuousFunctions:
        @staticmethod
        def sphere(xvals):
            """
                    The Sphere function calculates the sum of the squares of its input variables.
                    It's a simple, smooth, and convex function used as a benchmark in optimization.

                    Parameters:
                    - xvals (list[float]): A list of float values representing the input variables.

                    Returns:
                    - float: sum of the squares of the input variables.
                    Source: https://www.sfu.ca/~ssurjano/optimization.html
                    Example usage:
                    >>> ContinuousFunctions.sphere([1, 2, 3])
                    14
                    """
            result = 0
            for x in xvals:
                result += x ** 2
            return result

        @staticmethod
        def booth(x, y):
            """
                    The Booth function is a two-dimensional test function for optimization algorithms.
                    It's known for its simplicity and has a single global minimum.

                    Parameters:
                    - x (float): The x-coordinate, typically within the range of -10 to 10.
                    - y (float): The y-coordinate, typically within the range of -10 to 10.

                    Returns:
                    - float: The Booth function value at the point (x, y).
                    Source: https://www.sfu.ca/~ssurjano/optimization.html
                    Example usage:
                    >>> ContinuousFunctions.booth(1, 3)
                    1
                    """
            return (x + 2*y - 7)**2 + (2*x + y - 5)**2

        @staticmethod
        def rastrigin(xvals, A=10):
            """
                    The Rastrigin function is a non-convex function characterized by a large number of local minima,
                    making it difficult to find the global minimum. It's defined by the sum of squared variables
                    minus a cosine term for each variable, creating a complex landscape.

                    Parameters:
                    - xvals (list[float]): A list of float values representing the input variables.
                    - A (float, optional): The amplitude of the cosine component. Defaults to 10.

                    Returns:
                    - float: The calculated value of the Rastrigin function for the given inputs.
                    Source: https://www.sfu.ca/~ssurjano/optimization.html
                    Example usage:
                    >>> ContinuousFunctions.rastrigin([0, 0])
                    0
                    """
            result = len(xvals) * 10
            for x in xvals:
                result += x ** 2 - 10 * math.cos(2 * math.pi * x)
            return result

        @staticmethod
        def ackley(xvals):
            """
                 The Ackley function is used for testing optimization algorithms, known for its complex landscape with many local minima.
                 It combines an exponential term, a cosine term, and constants to create a challenging optimization problem.

                 Parameters:
                 - xvals (list[float]): A list of float values representing the input variables.

                 Returns:
                 - float: The Ackley function value for the given inputs.
                Source: https://www.sfu.ca/~ssurjano/optimization.html
                 Example usage:
                 >>> ContinuousFunctions.ackley([0, 0])
                 0
                 """
            sum1 = 0
            sum2 = 0
            for x in xvals:
                sum1 += x ** 2
                sum2 += math.cos(2 * math.pi * x)
            return -20 * math.exp(-0.2 * math.sqrt((1 / len(xvals)) * sum1)) - math.exp(
                (1 / len(xvals)) * sum2) + 20 + math.exp(1)

        @staticmethod
        def schwefel(xvals):
            """
                The Schwefel function is a benchmark problem in optimization, known for its large number of local minima
                and a global minimum that is difficult to locate. It involves a sine term and is challenging for optimization algorithms.

                Parameters:
                - xvals (list[float]): A list of float values representing the input variables.

                Returns:
                - float: The Schwefel function value for the given inputs.
                Source: https://www.sfu.ca/~ssurjano/optimization.html
                Example usage:
                >>> ContinuousFunctions.schwefel([420.9687, 420.9687])
                0
            """
            result = len(xvals) * 418.9829
            for x in xvals:
                result += x * math.sin(math.sqrt(abs(x)))
            return result

        @staticmethod
        def holdertable(xvals):
            """
                   The Holder Table function is a two-dimensional function known for its multiple global minima.
                   It combines sine, cosine, exponential, and absolute value operations to create a complex landscape.

                   Parameters:
                   - xvals (list[float]): A list containing two float values representing the x and y coordinates.

                   Returns:
                   - float: The Holder Table function value at the point (x, y).
                    Source: https://www.sfu.ca/~ssurjano/optimization.html
                   Example usage:
                   >>> ContinuousFunctions.holdertable([8.05502, 9.66459])
                   -19.2085
            """
            return -abs(math.sin(xvals[0]) * math.cos(xvals[1]) * math.exp(abs(1 - math.sqrt(xvals[0] ** 2 + xvals[1] ** 2) / math.pi)))

        @staticmethod
        def langermann(xvals):
            """
                   The Langermann function is a benchmark function in optimization characterized by several local minima.
                   It involves a cosine term modulated by an exponential term, making it challenging for optimization algorithms.

                   Parameters:
                   - xvals (list[float]): A list of float values representing the input variables.

                   Returns:
                   - float: The Langermann function value for the given inputs.
                   Source: https://www.sfu.ca/~ssurjano/optimization.html
                    Example usage:
                   >>> ContinuousFunctions.langermann([2, 3])
                   -5.1621259
            """
            m = 5
            c = [1, 2, 5, 2, 3]
            # 3D
            A = {0: {0: 3, 1: 5}, 1: {0: 5, 1: 2}, 2: {0: 2, 1: 1}, 3: {0: 1, 1: 4}, 4: {0: 7, 1: 9}}
            res = 0
            for i in range(0, m):
                sum1 = 0
                sum2 = 0
                for j in range(len(xvals)):
                    sum1 += (xvals[j] - A[i][j]) ** 2
                    sum2 += (xvals[j] - A[i][j]) ** 2
                res += c[i] * math.exp((-1 / math.pi) * sum1) * math.cos(math.pi * sum2)
            return res

        @staticmethod
        def shubert(xvals):
            """
                   The Shubert function is a multi-modal function with several local minima and global minima, used as a test case for optimization algorithms.
                   It's defined by the product of two sums, each involving a cosine term.

                   Parameters:
                   - xvals (list[float]): A list containing two float values representing the x and y coordinates.

                   Returns:
                   - float: The Shubert function value at the point (x, y).
                   Source: https://www.sfu.ca/~ssurjano/optimization.html
                   Example usage:
                   >>> ContinuousFunctions.shubert([-7.0835, 4.8580])
                   -186.7309
            """
            xval = 0
            yval = 0
            for i in range(1, 6):
                xval += i * math.cos((i + 1) * xvals[0] + i)
                yval += i * math.cos((i + 1) * xvals[1] + i)
            return xval * yval

        @staticmethod
        def dropwave(xvals):
            """
                    The Drop-Wave function is a two-dimensional function used in optimization challenges,
                    known for its large, flat areas separated by a steep "drop" and a single global minimum.

                    Parameters:
                    - xvals (list[float]): A list containing two float values representing the x and y coordinates.

                    Returns:
                    - float: The Drop-Wave function value at the point (x, y).
                    Source: https://www.sfu.ca/~ssurjano/optimization.html
                    Example usage:
                    >>> ContinuousFunctions.dropwave([0, 0])
                    -1
            """
            return -(1 + math.cos(12 * math.sqrt(xvals[0] ** 2 + xvals[1] ** 2))) / (0.5 * (xvals[0] ** 2 + xvals[1] ** 2) + 2)

        @staticmethod
        def beale(x, y):  # limits -4.5 <= x,y <= 4.5
            """
                    The Beale function is a two-dimensional benchmark problem for optimization,
                    known for its challenging landscape with many local minima.

                    Parameters:
                    - x (float): The x-coordinate.
                    - y (float): The y-coordinate.

                    Returns:
                    - float: The Beale function value at the point (x, y).
                    Source: https://www.sfu.ca/~ssurjano/optimization.html
                    Example usage:
                    >>> ContinuousFunctions.beale(3, 0.5)
                    0
            """
            return (1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2

        @staticmethod
        def mcCormick(x, y):  # limits -1.5 <= x <= 4, -3 <= y <= 4
            """
              The McCormick function is a two-dimensional benchmark problem for optimization algorithms,
              featuring a simple yet challenging landscape with a global minimum.

              Parameters:
              - x (float): The x-coordinate.
              - y (float): The y-coordinate.

              Returns:
              - float: The McCormick function value at the point (x, y).
              Source: https://www.sfu.ca/~ssurjano/optimization.html
              Example usage:
              >>> ContinuousFunctions.mcCormick(-0.54719, -1.54719)
              -1.9133
            """
            return math.sin(x + y) + (x - y) ** 2 + -1.5 * x + 2.5 * y + 1

        @staticmethod
        def eggholder(xvals):  # limits -512 <= x <= 512, -512 <= y <= 512
            """
                The Eggholder function is a two-dimensional benchmark problem known for its large number of local minima,
                making it a challenging problem for optimization algorithms. It involves sine and square root operations.

                Parameters:
                - xvals (list[float]): A list containing two float values representing the x and y coordinates.

                Returns:
                - float: The Eggholder function value at the point (x, y).
                Source: https://www.sfu.ca/~ssurjano/optimization.html
                Example usage:
                >>> ContinuousFunctions.eggholder([512, 404.2319])
                -959.6407
            """
            res = 0
            for i in range(len(xvals) - 1):
                res += -(xvals[i + 1] + 47) * math.sin(math.sqrt(abs(xvals[i] / 2 + xvals[i + 1] + 47))) - xvals[i] * math.sin(
                    math.sqrt(abs(xvals[i] - xvals[i + 1] - 47)))
            return res


    class NoncontinuousFunctions:
        @staticmethod
        def step_fun(xvals):
            """
                The Step function is a simple, piecewise function that introduces discontinuities by flooring the absolute value of each input component.
                It is used as a benchmark for optimization algorithms, especially for testing their ability to handle discontinuous landscapes.

                Parameters:
                - xvals (list[float]): A list of float values representing the coordinates of a point in n-dimensional space. Each coordinate should be within the range of [-100, 100].

                Returns:
                - float: The sum of the floored absolute values of the input components, representing the Step function's value at the point defined by `xvals1`. The function has a global minimum value of 0 at the origin (0, ..., 0) and a secondary minimum value of 1.
                Source: M. Jamil and X. S. Yang, “A literature survey of benchmark functions for global
                        optimisation problems,” International Journal of Mathematical Modelling and
                        Numerical Optimisation, vol. 4, no. 2, p. 150, 2013,
                        doi:10.1504/ijmmno.2013.055204
                Example usage:
                >>> step_fun([0, 0.99, -0.99])  # Close to the global minimum
                0
                >>> step_fun([1.01, -1.01, 2])  # Example input within the valid range
                3
            """
            fun_val=0;
            for x in xvals:
                fun_val += (np.floor(abs(x)))
            return fun_val

        @staticmethod
        def rastrigin(xvals):
            """
                The non-continuous Rastrigin function is a modified version of the classic Rastrigin function, designed to test optimization algorithms on non-continuous landscapes.
                This version introduces discontinuities by rounding input values to the nearest half-integer if their absolute value is greater than or equal to 0.5.


                Parameters:
                - xvals (list[float]): A list of float values representing the coordinates of a point in n-dimensional space. Each coordinate should be within the range of [-5.12, 5.12].

                Returns:
                - float: The value of the non-continuous Rastrigin function at the point defined by `xvals`. The function has a global minimum value of 0 at the origin (0, ..., 0).

                Notes:
                - The rounding introduces discontinuities into the landscape, making the optimization problem more challenging by preventing straightforward gradient-based approaches and requiring more sophisticated global optimization strategies.

                - Source: https://www.researchgate.net/publication/347268116_Weighted_Fuzzy_Production_Rule_Extraction_Using_Modified_Harmony_Search_Algorithm_and_BP_Neural_Network_Framework
                Example usage:
                >>> rastrigin([0, 0, 0])  # Global minimum
                0
                >>> rastrigin([0.1, -0.25, 0.75])  # Example input within the valid range
            """
            fun_val = len(xvals) * 10
            for i in xvals:
                yi = i
                if (np.abs(i) >= 0.5):
                    yi = round(2 * i) / 2
                fun_val += yi ** 2 - 10 * (np.cos(2 * np.pi * yi))
            return fun_val

        @staticmethod
        def xin_she_yang_n2(xvals):
            """
                The Xin-She Yang N. 2 function is a benchmark problem for testing optimization algorithms.
                This function is part of a family of functions proposed by Xin-She Yang which are used to simulate the complex, multi-modal landscapes typical of real-world optimization problems.
                The function is characterized by its oscillatory behavior and multiple local minima.

                Parameters:
                - xvals (list[float]): A list of float values representing the coordinates of a point in n-dimensional space. Each coordinate xi should be within the range of [-2π, 2π], where i ranges from 1 to the dimensionality of the input vector (d).

                Returns:
                - float: The value of the Xin-She Yang N. 2 function at the point defined by `xvals`. The function has a global minimum value of 0 at the origin (0, ..., 0) and a notable secondary minimum value of approximately 0.430.

                Notes:
                - The function combines an absolute value term with an exponential term dependent on the sine of the squared components, creating a challenging landscape for optimization algorithms due to its oscillatory nature and multiple local minima.

                - Source: https://towardsdatascience.com/optimization-eye-pleasure-78-benchmark-test-functions-for-single-objective-optimization-92e7ed1d1f12

                Example usage:
                >>> xin_she_yang_n2([0, 0, 0])  # Global minimum
                0
                >>> xin_she_yang_n2([np.pi, np.pi])  # Example input within the valid range
            """
            fst_val = 0
            scnd_val = 0
            for i in range(0, len(xvals)):
                fst_val += np.abs(xvals[i])

            for i in range(0, len(xvals)):
                scnd_val += np.sin(xvals[i] ** 2)

            return fst_val * (np.exp(-scnd_val))

        @staticmethod
        def rosenbrock(xvals):
            """
                This modified version of the Rosenbrock function introduces non-continuity by applying conditional modifications based on the sine of twice the absolute value of each input component.

                The function iterates over pairs of input values, applying different conditional modifications to the classic Rosenbrock formula based on the sine condition, thereby creating a non-continuous landscape with varying difficulty levels.

                Parameters:
                - xvals (list[float]): A list of float values representing the coordinates of a point in n-dimensional space, where n is even. The valid range for each value is -1 <= xval <= 1.

                Returns:
                - float: The value of the modified non-continuous Rosenbrock function at the point defined by `xvals`. The function has a global minimum value of 0 and a notable secondary minimum value of 1 under certain conditions.

                Notes:
                - The function's landscape is influenced by the sine of twice the absolute value of the input components, introducing non-linearity and conditional scaling.
                - Source: https://repository.up.ac.za/bitstream/handle/2263/39764/Wilke_Gradient_2013.pdf;sequence=1
                Example usage:
                >>> rosenbrock([0, 0, 0, 0])  # Global minimum
                0
                >>> rosenbrock([1, -1, 1, -1])  # Example input within the valid range
            """
            res = 0
            n = len(xvals) // 2
            for i in range(0, n):
                if (0 <= np.sin(2 * (np.abs(xvals[i]))) and np.sin(2 * (np.abs(xvals[i]))) < (2 / 3)):
                    val1 = (xvals[i] * (2 * i) - (xvals[i] ** 2 * (2 * i - 1))) ** 2
                    val2 = (1 - xvals[i] * (2 * i - 1)) ** 2
                    res += (1 / 1.2) * (100 * val1 + val2)

                if ((-2 / 3) <= np.sin(2 * (np.abs(xvals[i]))) and np.sin(2 * (np.abs(xvals[i]))) < 0):
                    val1 = (xvals[i] * (2 * i) - (xvals[i] ** 2 * (2 * i - 1))) ** 2
                    val2 = (1 - xvals[i] * (2 * i - 1)) ** 2
                    res += 1.2 * (100 * val1 + val2)

                if ((-2 / 3) > np.sin(2 * (np.abs(xvals[i]))) and np.sin(2 * (np.abs(xvals[i]))) >= (2 / 3)):
                    val1 = (xvals[i] * (2 * i) - (xvals[i] ** 2 * (2 * i - 1))) ** 2
                    val2 = (1 - xvals[i] * (2 * i - 1)) ** 2
                    res += (100 * val1 + val2)

            return res


        @staticmethod
        def quadric(xvals):
            """
                The Quadric function is designed to test optimization algorithms by introducing a condition-dependent scaling factor based on the sine of eight times the absolute value of each element in the input vector.


                The function iteratively calculates the sum of the squared values of all elements up to the current element, with a scaling factor that changes based on a sine condition.
                This creates a complex landscape with a global minimum and a notable secondary minimum.

                Parameters:
                - xvals (list[float]): A list of float values representing the coordinates of a point in n-dimensional space. The valid range for each value is -1 <= xval <= 1.

                Returns:
                - float: The value of the Quadric function at the point defined by `xvals`. The function has a global minimum value of 0 and a secondary minimum value of approximately 0.0744 under certain conditions.

                Notes:
                - The Quadric function's landscape is influenced by the sine of eight times the absolute value of the input components, which introduces non-linearity and conditional scaling.
                - Source:https://repository.up.ac.za/bitstream/handle/2263/39764/Wilke_Gradient_2013.pdf;sequence=1
                         https://link.springer.com/article/10.1007/s11081-011-9178-7
                Example usage:
                >>> quadric([0, 0, 0])  # Global minimum
                0
                >>> quadric([0.1, -0.1, 0.05])  # Example input within the valid range
            """
            res = 0
            n = len(xvals)
            for i in range(0, n):
                for j in range(0, i):
                    if (np.sin(8 * np.abs(xvals[i])) > 0.5):
                        res += xvals[j]
                    if (np.sin(8 * np.abs(xvals[i])) < -0.5):
                        res += 1.2 * (xvals[j])
                    if (np.sin(8 * np.abs(xvals[i])) >= -0.5 and np.sin(8 * np.abs(xvals[i])) <= 0.5):
                        res += (1 / 1.2) * (xvals[j])

                res = res ** 2

            return res

        @staticmethod
        def ellipsoid(xvals):
            """
                The Ellipsoid function is a type of scalable test function for optimization algorithms, characterized by its ellipsoidal contours.
                It is particularly used to test algorithms on their ability to handle problems with a large condition number and variable scaling.

                The function's value is modified based on the sum of the input vector's components, introducing a condition that affects the scaling of the function's output.

                Parameters:
                - xvals (list[float]): A list of float values representing the coordinates of a point in n-dimensional space. The recommended range for each value is -2 <= xval <= 2.

                Returns:
                - float: The value of the Ellipsoid function at the point defined by `xvals`. The function returns 0 for the global minimum at the origin and has a secondary minimum value of 0.85 under certain conditions.

                Notes:
                - The function scales the contribution of each dimension differently, which can make optimization more challenging as the number of dimensions increases.

                -Source: https://repository.up.ac.za/bitstream/handle/2263/39764/Wilke_Gradient_2013.pdf;sequence=1
                         https://link.springer.com/article/10.1007/s11081-011-9178-7
                Example usage:
                >>> ellipsoid([0, 0, 0])  # Global minimum
                0
                >>> ellipsoid([1, 1, 1])  # Example input within the recommended range
            """
            res = 0
            n = len(xvals)
            # for i in range(0,n):
            limit_sum = 0
            for j in range(n):
                limit_sum += xvals[j]

            if (np.sin(2 * limit_sum) > 0.5):
                for i in range(0, n):
                    res += (1 / 1.1) * (2 ** (i - 1)) * (xvals[i] ** 2)
                res += 1 / n
            elif (np.sin(2 * limit_sum) < -0.5):
                for i in range(0, n):
                    res += (1.1) * (2 ** (i - 1)) * (xvals[i] ** 2)
                res += 1 / n
            else:
                for i in range(0, n):
                    res += (2 ** (i - 1)) * (xvals[i] ** 2)

            return res