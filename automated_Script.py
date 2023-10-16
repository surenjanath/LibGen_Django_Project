import subprocess
import sys
import os

# Replace with your preferred venv name
venv_name = "venv"

# List of required Python libraries
required_libraries = [
    "django",
    'requests',
    'bs4',
    'djangorestframework',
    'pandas',
    'lxml'
    # Add other libraries you need here
]

# Function to create and activate a virtual environment
def create_and_activate_venv():
    subprocess.run([sys.executable, "-m", "venv", venv_name])
    print('[*] Activating Virtual Environment ... ' )
    # if sys.platform == "win32":
    activate_script = os.path.join(os.getcwd(), venv_name, "Scripts", "activate")
    print(activate_script)
    if not os.path.exists(activate_script):
            # Specify the activation script for Windows 64-bit
            activate_script = os.path.join(venv_name, "Scripts", "activate.ps1")
    else:
        activate_script = os.path.join(venv_name, "bin", "activate")

    subprocess.run([activate_script], shell=True)

# Function to install required libraries
def install_libraries():
    print('[*] Install Necessary Libraries ... ' )
    for library in required_libraries:
        subprocess.run([f"{venv_name}\\Scripts\\pip", "install", library], shell=True)

# Function to make migrations and migrate
def make_migrations_and_migrate():
    print('[*] Migrating Database Information ... ' )
    subprocess.run([f"{venv_name}\\Scripts\\python", "manage.py", "makemigrations"], shell=True)
    subprocess.run([f"{venv_name}\\Scripts\\python", "manage.py", "migrate"], shell=True)

# Function to run the development server
def run_server():
    print('[*] Running Python Project ... ' )
    subprocess.run([f"{venv_name}\\Scripts\\python", "manage.py", "runserver"], shell=True)

if __name__ == "__main__":
    try:
        # Create and activate the virtual environment
        create_and_activate_venv()

        # Install required libraries inside the virtual environment
        install_libraries()

        # Assuming you have a Django project directory with a manage.py file
        # Navigate to the directory containing your Django project before running this script

        # Make migrations and migrate inside the virtual environment
        make_migrations_and_migrate()

        # Run the development server inside the virtual environment
        run_server()
    except Exception as e :
        print(f'[*] Sorry an Error Occurred : {str(e)}')
