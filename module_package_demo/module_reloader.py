"""
Demonstrate how to reload modules after making changes.
"""
import importlib
import time
import sys
import os

def monitor_and_reload(module_name, file_path, check_interval=1):
    """
    Monitor a module file for changes and reload it when changes are detected.
    
    Args:
        module_name (str): Name of the module to reload
        file_path (str): Path to the module file
        check_interval (int): How often to check for changes (seconds)
    """
    # Import the module initially
    if module_name not in sys.modules:
        try:
            __import__(module_name)
            print(f"Module {module_name} loaded successfully.")
        except ImportError:
            print(f"Error: Could not import {module_name}.")
            return
    
    last_modified = os.path.getmtime(file_path)
    
    print(f"Monitoring {file_path} for changes. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(check_interval)
            
            # Check if file has been modified
            current_modified = os.path.getmtime(file_path)
            if current_modified > last_modified:
                print(f"Changes detected in {file_path}. Reloading...")
                
                # Reload the module
                if module_name in sys.modules:
                    module = sys.modules[module_name]
                    importlib.reload(module)
                    print(f"Module {module_name} reloaded.")
                    
                    # Example: Print a value from the module
                    if hasattr(module, 'MODULE_VERSION'):
                        print(f"New version: {module.MODULE_VERSION}")
                
                last_modified = current_modified
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python module_reloader.py <module_name>")
        print("Example: python module_reloader.py my_custom_module")
        sys.exit(1)
        
    module_to_monitor = sys.argv[1]
    module_file = f"{module_to_monitor}.py"
    
    # Check if the module file exists
    if not os.path.exists(module_file):
        module_file = os.path.join(os.path.dirname(__file__), f"{module_to_monitor}.py")
        if not os.path.exists(module_file):
            print(f"Error: Could not find {module_to_monitor}.py")
            sys.exit(1)
    
    monitor_and_reload(module_to_monitor, module_file)
