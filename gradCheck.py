import numpy as np

def grad_checker(f, weight, analytical_grad):
    
    actual_loss = f(weight)
    numerical_grad = np.zeros_like(weight)
    
    h = 1e-5

    for i in range(weight.size):

        old_val = weight.flat[i] #allows you to iterate through all the array index
        weight.flat[i] = old_val + h
        new_loss = f(weight)

        numerical_grad.flat[i] = (new_loss - actual_loss) / h

        weight.flat[i] = old_val
        
        print(f'Index {i}: Analytical Gradient: {analytical_grad.flat[i]:.8f}, Numerical Gradient: {numerical_grad.flat[i]:.8f}, Error: {abs(analytical_grad.flat[i] - numerical_grad.flat[i]):.8f}')
