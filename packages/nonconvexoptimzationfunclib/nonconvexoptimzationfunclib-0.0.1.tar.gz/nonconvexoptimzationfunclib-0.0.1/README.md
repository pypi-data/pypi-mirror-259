# Non-Convex Optimization Library (nonconvex_optimizationlib)
* The Non-Convex Optimization Library is a comprehensive Python package providing a collection of non-convex functions for testing and benchmarking optimization algorithms. 
* This library includes a variety of well-known functions in the field of optimization, such as the Sphere, Booth, Rastrigin, and many more, catering to both continuous and non-continuous optimization problems.

# Installation
- You can install the Non-Convex Optimization Library directly from PyPI:

    - **pip install nonconvex_optimizationlib**

- Note: Ensure you have Python and pip already installed on your system.
    

# Usage
- To use the library, simply import it into your Python script and access the desired optimization functions:

```python 
    from nonconvexoptimizationlib import nonconvexfunctions
    continuous_obj = nonconvexfunctions.NonconvexFunctions.ContinuousFunctions()
    non_continuous_obj=nonconvexfunctions.NonconvexFunctions.NoncontinuousFunctions()
    print(continuous_obj.rastrigin([-5.12,5.12]))
    print(non_continuous_obj.rastrigin([-5.12,5.12]))

    # Example: Using the Sphere function
    result = continuous_obj.sphere([1, 2])
    print(f"Sphere function result: {result}")
            
    # Example: Using the Booth function
    result = continuous_obj.booth(1, 3)
    print(f"Booth function result: {result}")
            
    # Example: Using the Step function
    result = non_continuous_obj.step_fun([0, 0.99, -0.99])
    print(f"Step function result: {result}")
```

# Available Functions
-   The library includes a range of functions under two main categories:

### Continuous Functions:

1. sphere(xvals) : Sphere function, n-dimension 
2. booth(x, y)   : Booth function, 3-dimension 
3. rastrigin(xvals, A=10) : Rastrigin function, n-dimension 
4. ackley(xvals) : Ackley function, n-dimension 
5. schwefel(xvals) : Schwefel function, n-dimension 
6. holdertable(xvals) : Holdertable function, 3-dimension 
7. langermann(xvals) : Langermann function, 3-dimension 
8. shubert(xvals) : Shubert function, 3-dimension 
9. dropwave(xvals) : Dropwave function, 3-dimension 
10. beale(x, y) : Beale function, 3-dimension  
11. mcCormick(x, y) : McCormick function, 3-dimension 
12. eggholder(xvals) : Eggholderfunctions, 3-dimension 

### Non-Continuous Functions:

1. step_fun(xvals) : Step Function
2. rastrigin(xvals) : Rastrigin function, n-dimension 
3. xin_she_yang_n2(xvals) : Xin-She-Yang-N2 function, n-dimension 
4. rosenbrock(xvals) : Rosenbrock function, n-dimension 
5. quadric(xvals) : Quadric function, n-dimension 
6. ellipsoid(xvals) : Ellipsoid function, n-dimension 

# Documentation
* For detailed documentation on each function, including parameters, return values, and example usage, refer to the docstrings provided within the library.

# Contributing
* Contributions to the Non-Convex Optimization Library are welcome! please contact on satyam101905@gmail.com
 
#Why we designed this package? 
* During my MS thesis(CSU Fresno) in metaheuristics algorithm design and optimization, I searched for several complex non-convex testbeds to test the newly designed algorithm.
    So, I came across several optimziation problems and some of them are mentioned here in this package as open source contribution
    Thesis Topic: Titled "Blindfolded Spider-Man Optimization: A Single-Point Metaheuristic Suitable for Continuous and Discrete Spaces", is now publicly available @
    Link: https://www.proquest.com/docview/2901409934
    
* ThankYou to Vasileios Lymperakis (author Buggy Pinball-a novel single point metaheuristic algorithm) for doing an amazing work in Buggy-Pinball which I was able to extended and explored further.
* Thank you to Dr. Thanos{CSU Fresno, Computer Science} my advisor who guided me.