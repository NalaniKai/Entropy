
import numpy as np

def entropy(probs):
    """Assumes input is numpy array and valid probability vector"""
    return -(probs * np.log(probs))


if __name__ == "__main__":
    pass
