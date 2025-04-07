import math
import datetime
import sys
import importlib
import subprocess

# 1. Import a module and use one of its functions (math.sqrt)
print("1. Using math module to find square root:")
number = 16
square_root = math.sqrt(number)
print(f"The square root of {number} is: {square_root}")

# 2. Use a module to work with dates and times
print("\n2. Working with datetime module:")
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%A, %B %d, %Y at %I:%M %p")
print(f"Current date and time: {formatted_time}")

# 3. Create and use a custom module
print("\n3. Using a custom module:")
try:
    import my_custom_module
    print(f"Sum of 5 and 7 is: {my_custom_module.add_numbers(5, 7)}")
    print(f"Is 17 prime? {my_custom_module.is_prime(17)}")
except ImportError:
    print("Custom module not found. Please create my_custom_module.py first.")

# 4. Work with a package in Python
print("\n4. Working with a custom package:")
try:
    import my_package.calculations
    print(f"Area of circle with radius 5: {my_package.calculations.calculate_circle_area(5)}")
    from my_package.string_utils import reverse_string
    print(f"Hello reversed: {reverse_string('Hello')}")
except ImportError:
    print("Custom package not found. Please create the package first.")

# 5. Check if a package is installed and use it
print("\n5. Checking if numpy is installed:")
try:
    import numpy as np
    print(f"NumPy is installed (version {np.__version__})")
    print(f"Random array: {np.random.rand(3)}")
except ImportError:
    print("NumPy is not installed.")

# 6. Use sys module to manipulate the module search path
print("\n6. Manipulating module search path:")
print(f"Current search paths: {sys.path[:3]}...")  # Show first 3 paths
custom_path = "/home/plad/Documents/Python/module_package_demo/custom_modules"
if custom_path not in sys.path:
    sys.path.append(custom_path)
    print(f"Added path: {custom_path}")
print(f"Updated search paths: {sys.path[:3]}...")

# 7. Reload a module after making changes
print("\n7. Reloading a module:")
try:
    print("Before reload:", my_custom_module.MODULE_VERSION)
    print("Simulating module change (in real usage, you would edit the file)")
    # In real usage, you would edit the file here
    importlib.reload(my_custom_module)
    print("After reload:", my_custom_module.MODULE_VERSION)
except (ImportError, AttributeError):
    print("Module reloading demonstration skipped.")

# 8. Using pip commands via subprocess
print("\n8. Package management with pip:")

def run_pip_command(command):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip"] + command.split(),
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

# Check version of a package
print("\nChecking version of installed package:")
print(run_pip_command("show requests")[:200] + "...")  # Showing just the beginning

# List all installed packages
print("\nListing first few installed packages:")
all_packages = run_pip_command("list")
print("\n".join(all_packages.split("\n")[:5]) + "...")

print("\nDemo of installing a package (commented out for safety):")
print("# run_pip_command('install requests')")

print("\nDemo of uninstalling a package (commented out for safety):")
print("# run_pip_command('uninstall requests -y')")

print("\nComplete! Check the rest of the files to learn about custom modules and packages.")
