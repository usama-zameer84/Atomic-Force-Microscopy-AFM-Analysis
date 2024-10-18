
import matplotlib.pyplot as plt

def plot_force_distance_curve(curve, slope):
    """ Plot the force-distance curve with slope annotation. """
    plt.plot(curve)
    plt.title(f"Force-Distance Curve (Slope: {slope})")
    plt.show()

def generate_heatmap(heights):
    """ Generate heatmap from AFM height data. """
    plt.imshow(heights, cmap='hot', interpolation='nearest')
    plt.title("Height Data Heatmap")
    plt.colorbar()
    plt.show()
