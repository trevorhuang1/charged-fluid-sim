import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_charge_density(charge_density, X, Y, title="Charge Density"):
    """Plot 2D charge density distribution"""
    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, charge_density, levels=20, cmap='RdBu_r')
    plt.colorbar(label='Charge Density (ρ)')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title(title)
    plt.axis('equal')
    plt.show()

def plot_potential(potential, X, Y, title="Electric Potential"):
    """Plot 2D electric potential distribution"""
    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, potential, levels=20, cmap='viridis')
    plt.colorbar(label='Potential (φ)')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title(title)
    plt.axis('equal')
    plt.show()

def plot_electric_field(Ex, Ey, X, Y, title="Electric Field"):
    """Plot electric field vectors"""
    plt.figure(figsize=(10, 8))
    
    # Skip some arrows for cleaner visualization
    skip = 5
    plt.quiver(X[::skip, ::skip], Y[::skip, ::skip], 
               Ex[::skip, ::skip], Ey[::skip, ::skip], 
               scale=50, alpha=0.7)
    
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title(title)
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_combined_view(charge_density, potential, X, Y):
    """Plot charge density and potential side by side"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Charge density
    im1 = ax1.contourf(X, Y, charge_density, levels=20, cmap='RdBu_r')
    ax1.set_xlabel('X (m)')
    ax1.set_ylabel('Y (m)')
    ax1.set_title('Charge Density')
    ax1.axis('equal')
    plt.colorbar(im1, ax=ax1, label='ρ')
    
    # Potential
    im2 = ax2.contourf(X, Y, potential, levels=20, cmap='viridis')
    ax2.set_xlabel('X (m)')
    ax2.set_ylabel('Y (m)')
    ax2.set_title('Electric Potential')
    ax2.axis('equal')
    plt.colorbar(im2, ax=ax2, label='φ')
    
    plt.tight_layout()
    plt.show()