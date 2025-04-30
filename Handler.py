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
import subprocess, os, shutil
from Utility import utility
from rich.console import Console

# Required Instances
console = Console()


# Main Class
class Handler:
    def __init__(self):
        self.__utility = utility()
        self.__process_status_code = None

    def check_requirements(self) -> None:
        try:
            if self.__utility.is_arch_based():
                console.print("✅ [bold green]Arch-based[/bold green] system detected")
                console.print(
                    ":arrow_heading_down: Installing [bold green]dev tools[/bold green]"
                )
                self.__process_status_code = subprocess.run(
                    ["sudo", "pacman", "-Syu", "base-devel"], check=True
                ).returncode
                if self.__process_status_code == 0:
                    console.print(
                        "✅ [bold green]dev tools[/bold green] installed successfully"
                    )

                # if self.__utility.is_yay_installed():
                #     console.print("✅ [bold green]yay[/bold green] is installed")

                # else:
                # console.print("❌ [bold red]yay[/bold red] is not installed")
                # console.print(
                #     ":arrow_heading_down: Installing [bold green]yay[/bold green]"
                # )
                # self.__process_status_code = subprocess.run(
                #     ["sudo", "pacman", "-Syu", "yay"], check=True
                # ).returncode
                # if self.__process_status_code == 0:
                #     console.print(
                #         "✅ [bold green]yay[/bold green] installed successfully"
                #     )

                if self.__utility.is_git_installed():
                    console.print("✅ [bold green]git[/bold green] is installed")
                else:
                    console.print("❌ [bold red]git[/bold red] is not installed")
                    console.print(
                        ":arrow_heading_down: Installing [bold green]git[/bold green]"
                    )
                    self.__process_status_code = subprocess.run(
                        ["sudo", "pacman", "-Syu", "git"], check=True
                    ).returncode
                    if self.__process_status_code == 0:
                        console.print(
                            "✅ [bold green]git[/bold green] installed successfully"
                        )
        except subprocess.CalledProcessError as e:
            console.print(f"❌ [bold red]Error:[/bold red] {e}")

    def install_vsc(self) -> None:
        try:
            console.print(
                f":information: Home Directory: [bold green]{self.__utility.get_home_directory()}[/bold green]"
            )
            os.chdir(f"{self.__utility.get_home_directory()}/Downloads")
            console.print(
                f":arrow_forward: Using for downloads [bold green]{self.__utility.get_current_directory()}[/bold green]"
            )
            if os.path.exists("visual-studio-code-bin"):
                console.print(
                    ":arrow_heading_down: Removing Older Version of [bold green]visual-studio-code-bin[/bold green]"
                )
                shutil.rmtree("visual-studio-code-bin")
                console.print(
                    "✅ [bold green]visual-studio-code-bin[/bold green] removed successfully"
                )
            self.__utility.__process_status_code = subprocess.run(
                [
                    "git",
                    "clone",
                    "https://aur.archlinux.org/visual-studio-code-bin.git",
                ],
                check=True,
            ).returncode
            console.print(
                f":information: Current Directory: [bold green]{self.__utility.get_current_directory()}[/bold green]"
            )
            if self.__process_status_code == 0:
                os.chdir("visual-studio-code-bin")
                self.__process_status_code = subprocess.run(
                    ["makepkg", "-sri"], check=True
                )

        except subprocess.CalledProcessError as e:
            console.print(f"❌ [bold red]Error:[/bold red] {e}")
        except Exception as e:
            console.print(f"❌ [bold red]Error:[/bold red] {e}")

        finally:
            if self.__process_status_code == 0:
                console.print(
                    ":arrow_heading_down: Cleaning up [bold green]visual-studio-code-bin[/bold green]"
                )
                os.chdir(f"{self.__utility.get_home_directory()}/Downloads")
                shutil.rmtree("visual-studio-code-bin")
                console.print("✅ [bold green]Done[/bold green]")
