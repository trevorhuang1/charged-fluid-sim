import numpy as np

# Define grid parameters
nx, ny = 100, 100        # number of cells in x and y directions
length_x, length_y = 1.0, 1.0  # physical length of domain (meters)

# Calculate grid spacing
dx = length_x / (nx - 1)
dy = length_y / (ny - 1)

# Create coordinate arrays
x = np.linspace(0, length_x, nx)
y = np.linspace(0, length_y, ny)

# Create 2D meshgrid for coordinates (optional, useful for plotting)
X, Y = np.meshgrid(x, y)

# Initialize fields on the grid:
charge_density = np.zeros((ny, nx))  # 2D array for ρ(x,y)
potential = np.zeros((ny, nx))       # 2D array for φ(x,y)

# Example: place a positive charge blob in the center
center_x, center_y = nx // 2, ny // 2
charge_density[center_y-5:center_y+5, center_x-5:center_x+5] = 1.0  # arbitrary units

print(f"Grid spacing dx={dx}, dy={dy}")
print(f"Charge density at center:\n{charge_density[center_y-6:center_y+6, center_x-6:center_x+6]}")
