# Python Modules and Packages Demo

This folder contains examples demonstrating various aspects of Python modules and packages.

## Files Included

- **modules_demo.py**: Main demonstration script covering various module/package concepts
- **my_custom_module.py**: Example of a custom module with utility functions
- **my_package/**: Example package with:
  - **__init__.py**: Package initialization file
  - **calculations.py**: Module for mathematical calculations
  - **string_utils.py**: Module for string operations
- **package_manager.py**: Utility for package management with pip
- **module_reloader.py**: Demonstration of module reloading

## How to Use

1. Run the main demonstration:
   ```
   python modules_demo.py
   ```

2. Try the module reloader:
   ```
   python module_reloader.py my_custom_module
   ```
   (Then edit my_custom_module.py in another window to see reloading in action)

3. Use the package management utility:
   ```
   python package_manager.py list
   python package_manager.py check --package requests
   ```

## Topics Covered

- Importing and using built-in modules
- Creating and using custom modules
- Working with packages
- Package installation and management with pip
- Module search path manipulation
- Module reloading
