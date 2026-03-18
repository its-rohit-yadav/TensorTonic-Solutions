def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Writ code here
    
    return (np.dot(X,W)+b).tolist()