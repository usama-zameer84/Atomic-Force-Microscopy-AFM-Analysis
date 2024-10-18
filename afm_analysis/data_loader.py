import numpy as np

def load_heights(file_path):
    """ Load the AFM heights data from a .npy file. """
    try:
        heights = np.load(file_path)
        return heights
    except Exception as e:
        raise ValueError(f"Failed to load heights data: {e}")

def load_force_data(file_path):
    """ Load the AFM force data from a pickled file. """
    try:
        with open(file_path, 'rb') as f:
            force_data = pickle.load(f)
        return force_data
    except Exception as e:
        raise ValueError(f"Failed to load force data: {e}")
