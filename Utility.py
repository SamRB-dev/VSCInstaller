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
import platform
import shutil
import subprocess

# Main Class
class utility:
    def __init__(self):
        self.__os_type = platform.system()
        self.__os_version = platform.release()
        self.__home_directory = os.path.expanduser("~")

    
    def get_os_type(self) -> str:
        return self.__os_type
    
    def get_os_version(self) -> str:
        return self.__os_version
    
    def is_arch_based(self) -> bool:
        "Written for Arch-based systems"
        return shutil.which("pacman") is not None
    
    def is_git_installed(self) -> bool:
        "Required for Arch-based systems"
        return shutil.which("git") is not None
    
    def get_home_directory(self) -> str:
        return self.__home_directory
    
    def get_current_directory(self) -> str:
        return os.getcwd()

    def is_root_user(self) -> bool:
        return os.geteuid() == 0
    
    def is_yay_installed(self) -> bool:
        "Required for Arch-based systems"
        return shutil.which("yay") is not None