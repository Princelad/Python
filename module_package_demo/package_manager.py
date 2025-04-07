"""
Utility script for package management operations.
"""
import sys
import subprocess
import argparse

def run_pip_command(command_parts):
    """Run a pip command and return its output."""
    cmd = [sys.executable, "-m", "pip"] + command_parts
    print(f"Running: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def list_packages():
    """List all installed packages."""
    return run_pip_command(["list"])

def check_version(package_name):
    """Check the version of an installed package."""
    return run_pip_command(["show", package_name])

def install_package(package_name):
    """Install a package using pip."""
    return run_pip_command(["install", package_name])

def uninstall_package(package_name):
    """Uninstall a package using pip."""
    return run_pip_command(["uninstall", "-y", package_name])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package Management Utility")
    parser.add_argument("action", choices=["list", "check", "install", "uninstall"], 
                        help="Action to perform")
    parser.add_argument("--package", help="Package name for check/install/uninstall")
    
    args = parser.parse_args()
    
    if args.action == "list":
        output = list_packages()
        print(output)
    elif args.action in ["check", "install", "uninstall"]:
        if not args.package:
            print(f"Error: Package name required for {args.action}")
            sys.exit(1)
            
        if args.action == "check":
            output = check_version(args.package)
        elif args.action == "install":
            output = install_package(args.package)
        else:  # uninstall
            output = uninstall_package(args.package)
            
        if output:
            print(output)
