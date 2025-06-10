#!/bin/bash
cd /home/trevor/nighthawk/charged-fluid-sim

# Verify the installation and check the Python version
python3.12 --version

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3.12 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install the required Python packages
if [ -f "requirements.txt" ]; then
    echo "Installing requirements from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found, installing basic packages..."
    pip install numpy matplotlib scipy
fi

echo "Virtual environment activated with all requirements!"
echo "Run 'python basic2d.py' to execute your script"