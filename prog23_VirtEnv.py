#A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work
# on multiple projects with different dependencies and packages without conflicts. This can be especially useful when
# working on projects that have conflicting package versions or packages that are not compatible with each other.

# To create a virtual environment in Python, you can use the venv module that comes with Python. Here's an example of
# how to create a virtual environment and activate it:

# Create a virtual environment named "myenv" in the current directory
# python -m venv myenv

#  Activate the virtual environment (Linux/macOS)
# source myenv/bin/activate

#  Activate the virtual environment named "myenv" (Windows)
# .\myenv\Scripts\activate

#To deactivate the virtual environment, you can simply run the following command:
# deactivate

#You can see the version of python and the installed packages in the virtual environment using the following commands:
# python --version
# Or you can use pip to list the installed packages:
# pip list