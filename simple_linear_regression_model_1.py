# Simple Linear Regression Model
# Using scipy

# numpy library: scientific computing in Python, multidimensional array object, derived objects,
# routines for fast operations in arrays
# scipy library: algorithms for optimizatin, integration, interpolation, eigenvalue problems, 
# algebraic equations, differential equations, statistics, etc.
import numpy as np
import scipy.stats as st

x_dependent_variable = np.array([40, 100, 99, 150])
y_independent_variable = np.array([1, 3, 2, 5])

simple_linear_regression_model = st.linregress(x_dependent_variable,y_independent_variable)

print(simple_linear_regression_model)
