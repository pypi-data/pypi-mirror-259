import subprocess
import sys

def install_dependencies():
    """
    Install project dependencies using Poetry.
    """
    try:
        # Run 'poetry install' command
        subprocess.run(["poetry", "install", "--no-dev"], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install dependencies. {e}")
        sys.exit(1)

def main():
    # Check if dependencies are installed
    try:
        import requests
    except ImportError:
        print("Dependencies not found. Installing...")
        install_dependencies()
        import requests, typer

    from .cpf import app
    app()


if __name__ == "__main__":
    main()
