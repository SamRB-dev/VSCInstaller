# -*- coding: utf-8 -*-
__author__ = "SamRB-dev"
__copyright__ = "Copyright 2025, SamRB-dev"
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "Development"
__all__ = ["VSCInstaller"]
__description__ = "Visual Studio Code Installer"
__file__name__ = "VSCInstaller.py"

# Importing necessary libraries
import os
import sys
import subprocess
import platform

# Custom Imports
from Handler import Handler

# Main function
def main():
    handler = Handler()
    handler.check_requirements()
    handler.install_vsc()


if __name__ == "__main__":
    main()