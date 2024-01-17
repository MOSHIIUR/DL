import numpy as np
import matplotlib.pyplot as plt

def grad_checker(f, weight, analytical_grad):
    
    actual_loss = f(weight)
    numerical_grad = np.zeros_like(weight)
    error = np.zeros_like(weight)
    
    h = 1e-5

    for i in range(weight.size):

        old_val = weight.flat[i] #allows you to iterate through all the array index
        weight.flat[i] = old_val + h
        new_loss = f(weight)

        numerical_grad.flat[i] = (new_loss - actual_loss) / h
        weight.flat[i] = old_val
        
        error.flat[i] = abs(analytical_grad.flat[i] - numerical_grad.flat[i])
                
    arrays = [analytical_grad, numerical_grad, error]
    title = ['Analytical Gradient', 'Numerical Gradient', 'Error']

    fig, axs = plt.subplots(1, len(arrays))

    for i, array in enumerate(arrays):
        axs[i].imshow(array, cmap='Blues', interpolation='nearest')  # Use 'Blues' colormap

        for row in range(array.shape[0]):
            for col in range(array.shape[1]):
                axs[i].text(col, row, f'{array[row, col]:.2f}', color='black',  # Use black text
                            ha='center', va='center', fontsize=10)

        axs[i].axis('off')
        axs[i].set_title(title[i])

    # Adjust layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()

    

