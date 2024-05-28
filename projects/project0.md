# Project 0: Setup

Due: May 31, 2024 at 11:59 PM

This project is simply to get your system ready. Although you will "submit" this project on Gradescope, it is not counted towards your final grade.  The good-faith attempt (GFA) rule **does not apply** to this project.

**Start with the [Instructions](#instructions)!**

## Table of Contents

- [Languages and Packages](#languages-and-packages)
- [Instructions](#instructions)
  - [Linux (NOT WSL)](#linux-not-wsl)
  - [Windows](#windows)
  - [macOS](#macos)
- [Verifying Setup](#verifying-setup)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Troubleshooting `gradescope-submit`](#troubleshooting-gradescope-submit)
  - [Incorrect Passwords](#incorrect-passwords)
  - [HTTP Errors](#http-errors)
- [Special macOS Instructions](#special-macos-instructions)
  - [Do you have a Mac running an older version of macOS?](#do-you-have-a-mac-running-an-older-version-of-macos)


## Languages and Packages

In this course, we will be programming in Python, OCaml and Rust.  Below is a summary of the packages that need to be installed.  You do not need to use these links, they are just for reference or learning more about the languages and/or packages.  You can skip below to the instructions.

- [Git](https://git-scm.com/)
- [Python](https://www.python.org)
    - [pytest](https://docs.pytest.org/en/7.3.x)
    - [hypothesis](https://pypi.org/project/hypothesis/)
- [OCaml](http://ocaml.org)
    - [OPAM](https://opam.ocaml.org)
    - [OUnit](https://opam.ocaml.org/packages/ounit)
    - [dune](https://opam.ocaml.org/packages/dune)
    - [utop](https://opam.ocaml.org/packages/utop)
    - [qcheck](https://opam.ocaml.org/packages/qcheck/)
- [Rust](https://www.rust-lang.org)

## Instructions

First, you will need to clone this repository to your local filesystem. To do this, you will first need to make a github token. See [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github) for how to do this. 

Then run:

```
git clone https://github.com/cmsc330summer24/project-0-<github-username>
```

The files in the `project-0` folder will be used for the [Verifying Setup](#verifying-setup) section at the bottom.

The following sections will help you install the necessary packages and programs on your operating system.  Some steps may take a long time. Please be patient.  **Read all instructions very carefully.**

The output of each command is important, so please pay careful attention to what each one prints.  If you encounter an error message, do not ignore it.  We will be available in office hours to help you get set up if you run into problems.  As a general rule, no output means the command executed successfully.

**NOTE:** You may wish to install the python dependencies in a virtual environment so as to not mess with any current versions you have installed. If so, please follow the [virtual environment setup](#virtual-environment-setup) first, then go to your OS-specific instructions.

**Please skip to the section below that corresponds with your operating system.**


### Linux (NOT WSL)

These instructions assume you have a Debian-based system (e.g. Ubuntu).  If you have a different distribution, you will have to find and download the corresponding packages in your native package manager.  Note that the packages there may have slightly different names.

1. Firstly, install the basic dependencies:
    - Run `sudo apt update` to update your local package listing
    - Run `sudo apt install python3 python3-dev python3-pip ocaml ocaml-native-compilers camlp4 make m4 curl libssl-dev pkg-config`
2. Install some Pip packages for testing
    - Run `python3 -m pip install pytest hypothesis`
3. Install and initialize the OCaml package manager
    - Run `sh <(curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh)` (when prompted for the installation location, just hit enter to select the default)
        - Run `opam --version`.  You should be on version 2 (followed by some versions, just make sure the major version is 2).  Check out [the manual](https://opam.ocaml.org/doc/Install.html) if this is not the case, you may have to follow special directions for your particular operating system and version.
        - If you encounter any issues, or are running a different flavor of linux, check out [the manual](https://opam.ocaml.org/doc/Install.html)
    - Run `opam init`
    - If it hangs at "Fetching repository information" press Enter. (This may take a while. Please be patient)
    - When prompted to modify `~/.profile` (or another file), type "n", but remember the filename
    - Open `~/.profile` (or the file mentioned above) in your text editor
    - Add the line `` eval `opam config env` `` (these are backticks, not single quotes)
    - Save the file
    - Run `source ~/.profile` (or the file you just edited)
4. Initialize OCaml
    - Run `opam update`
    - We will be using OCaml version 4.14.X. Run `ocaml -version` to check which version is currently installed
    - If you are already on version 4.14.X, you can skip to #5
    - If you are on another version, run `opam switch 4.14.0`.  If you get an error saying that switch is not currently installed, run `opam switch create 4.14.0`. (This may take a while. Please be patient)
    - Run `eval $(opam env)`
    - Ensure you are now on the correct version by running `ocaml -version`
    - Add the line `eval $(opam env --switch=4.14.0)` to your shell. First, run `echo $SHELL`
        - If `echo $SHELL` gives `/bin/zsh`, open the `~/.zshrc` file and add the line above to the bottom line 
      - If `echo $SHELL` gives `/bin/bash`, open the `~/.bashrc` file and add the line above to the bottom line 
5. Install OCaml packages
    - Run `opam install gradescope_submit ocamlfind ounit utop dune qcheck`
6. Install Rust
    - Go to [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) and run the installation command provided
    - If prompted, just select the defaults
    - Append `~/.cargo/bin` to the `PATH` environment variable. First, do `echo $SHELL`.
      - If `echo $SHELL` gives `/bin/zsh`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.zshrc`
      - If `echo $SHELL` gives `/bin/bash`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.bashrc`

### Windows

*This will only work on Windows 10 and newer.  If you are on an older version, you will probably need to set up a Linux VM.*

1. Follow the directions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to install the Windows Subsystem for Linux
2. Install the basic dependencies:
    - Run `sudo apt update && sudo apt upgrade` to update your local package listing
    - Run `sudo apt install python3 python3-dev python3-pip ocaml ocaml-native-compilers camlp4 make m4 curl libssl-dev pkg-config`
3. Install some Pip packages for testing
    - Run `python3 -m pip install pytest hypothesis`
4. Install and initialize the OCaml package manager
    - Run `sh <(curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh)` (when prompted for the installation location, just hit enter to select the default)
        - Run `opam --version`.  You should be on version 2 (followed by some versions; just make sure the major version is 2).  Check out [the manual](https://opam.ocaml.org/doc/Install.html) if this is not the case. You may have to follow special directions for your particular operating system and version.
        - If you encounter any issues, or are running a different flavor of linux, check out [the manual](https://opam.ocaml.org/doc/Install.html)
    - Run `opam init --disable-sandboxing`
    - If it hangs at "Fetching repository information", press Enter. This may take a while. Please be patient
    - When prompted to modify `~/.profile` (or another file), type "n", but remember the filename
    - Open `~/.profile` (or the file mentioned above) in your text editor
    - Add the line `` eval `opam config env` `` (these are backticks, not single quotes)
    - Save the file
    - Run `source ~/.profile` (or the file you just edited)
5. Initialize OCaml
    - Run `opam update`
    - We will be using OCaml version 4.14.X. Run `ocaml -version` to check which version is currently installed
    - If you are already on 4.14.X, you can skip to #6
    - If you are on another version, run `opam switch 4.14.0`
    - If you get an error saying that switch is not currently installed, run `opam switch create 4.14.0`. (This may take a while. Please be patient)
      - While installing the new switch, if you get an error for `bwrap`, first remove the `.opam` directory using `rm -r ~/.opam` and then reinitialize opam by **disabling sanboxing** using `opam init --disable-sandboxing`. Type "n" when prompted to modify `~/.profile`. Once opam has been initialized, rerun `opam switch create 4.14.0`
    - Run `eval $(opam env)`
    - Add the line `eval $(opam env --switch=4.14.0)` to your shell. First, run `echo $SHELL`
        - If `echo $SHELL` gives `/bin/zsh`, open the `~/.zshrc` file and add the line above to the bottom line 
        - If `echo $SHELL` gives `/bin/bash`, open the `~/.bashrc` file and add the line above to the bottom line 
    - Ensure you are now on the correct version by running `ocaml -version`
6. Install OCaml packages
    - Run `opam install gradescope_submit ocamlfind ounit utop dune qcheck`
7. Install Rust
    - Go to [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) and run the installation command provided
    - If prompted, just select the defaults
    - Append `~/.cargo/bin` to the `PATH` environment variable. First, do `echo $SHELL`.
      - If `echo $SHELL` gives `/bin/zsh`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.zshrc`
      - If `echo $SHELL` gives `/bin/bash`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.bashrc`

### macOS

Check the [Special macOS Instructions](#special-macos-instructions) to check if you need to follow any special steps. Then, come back here.

1. Install the Homebrew package manager (Updated in Fall 2021)
    - Run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Check your Python version by running `python3 --version`.  If it's older than 3.8,
   you'll need to install a newer version using `brew install python3`. Otherwise, skip to step 3.
    - If you needed to install a newer version, restart your terminal after the installation has completed and type `python3 --version` again to confirm that you now have a newer version.
3. Install the basic dependencies
    - Run `brew install ocaml opam openssl`
4. Install some Pip packages for testing
    - Run `python3 -m pip install pytest hypothesis`
5. Initialize the OCaml package manager
    - Run `opam init`
    - When prompted to modify `~/.zshrc` or `~/.bash_profile` (or similar file), type "y"
    - Run  `source ~/.zshrc` or `source ~/.bash_profile` (or the file mentioned above)
6. Initialize OCaml
    - Run `opam update`
    - We will be using OCaml version 4.14.X.  Run `ocaml -version` to check
      which version is currently installed
    - If you are already on 4.14.X, you can skip to #7
    - If you are on another version, run `opam switch 4.14.0`.  If you get an
      error saying that switch is not currently installed, run `opam switch
      create 4.14.0`. (This may take a while. Please be patient)
    - Run `eval $(opam env)`
    - Add the line `eval $(opam env --switch=4.14.0)` to your shell. First, run `echo $SHELL`
        - If `echo $SHELL` gives `/bin/zsh`, open the `~/.zshrc` file and add the line above to the bottom line 
        - If `echo $SHELL` gives `/bin/bash`, open the `~/.bashrc` file and add the line above to the bottom line 
    - Ensure you are now on the correct version by running `ocaml -version`
7. Install OCaml packages
    - Run `opam install gradescope_submit ocamlfind ounit utop dune qcheck`
8. Install Rust
    - Go to [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) and run the installation command provided
    - If prompted, just select the defaults
    - Append `~/.cargo/bin` to the `PATH` environment variable. First, do `echo $SHELL`.
      - If `echo $SHELL` gives `/bin/zsh`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.zshrc`
      - If `echo $SHELL` gives `/bin/bash`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.bashrc`

## Link Github to Gradescope

Log into your gradescope account and go to your account settings. Scroll down to the `Linked Accounts` section. If you do not already
have your Github account linked here, click the `Link a GitHub account` button and log into your Github account.
  
## How to Submit

Whenever you want to submit your project to gradescope, you will need to push your latest version to your repo. Follow these steps to do so:

First, make sure all your changes are pushed to github using the `git add`, `git commit`, and `git push` commands. We will teach you basic git usage in the first few days of the course, but you can refer to [my notes](https://bakalian.cs.umd.edu/assets/notes/git.pdf) for assistance. Additionally you can refer to a [testing repo](https://github.com/CliffBakalian/git-basics) I made, but it's recommended you make your own.

Next, to submit your project, you can run `submit` from your project directory.

The `submit` command will pull your code from GitHub, not your local files. If you do not push your changes to GitHub, they will not be uploaded to gradescope.

## Verifying Setup

To verify that you have the correct versions installed, run 
`pytest` in this directory.  You should not get any errors.  
This will create a file called p0.report.  Push your changes onto github. Then, submit this file by running `submit` in 
the project folder.  You will have to enter your credentials.  Alternatively, you can manually submit 
the file to Gradescope by uploading the p0.report file to the appropriate assignment.

## Virtual Environment Setup

Python docs instructions can be found [here](https://docs.python.org/3/library/venv.html#how-venvs-work).

In the folder that you want to keep all your 330 stuff, run the command `python -m venv myenv`, replacing `myenv` with the name you want.

Then, to activate this virtual environment that you just created, run `source myenv/bin/activate` in the same folder that you created it in (again replacing myenv with the name you chose).

To deactivate, run `deactivate` or restart your terminal

Now, you should see the name you chose in parenthesis next to your shell user, and can continue installing all your python dependencies. 

## Troubleshooting `gradescope-submit`

### Incorrect Passwords 

Make sure that the email address and password you entered is of the account
where your CMSC 330 course enrollment shows up. (If you login through "school
credentials" option and don't remember your **Gradescope** password, please
reset it.) Many people have multiple Gradescope accounts, and
we suggest you to merge them before trying to submit by the program.


### HTTP Errors

Remove the `gradescope-submit` config file by doing
`rm -r ~/.gradescope-submit`. Then, refer to the troubleshooting for incorrect
passwords and try it again.


## Special macOS Instructions

Check to see if you're running an older version of macOS. Either click the Apple button in the menubar in the top-left and click "About This Mac", or else run `sw_vers` from the terminal. You should only need the special section if your macOS version is less than 10.15

If your macOS version is less than 10.15, follow [the directions for macOS](#macos), but with the changes listed below. Otherwise, ignore the following section.

- If you have run the special instructions in previous classes or semesters, undo by uninstalling homebrew:
  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"`
  - You will probably have leftover files in `/opt/homebrew` or `/usr/local`. We will *try* to help you delete them in OH.
- Afterwards, run `brew install` INDIVIDUALLY on each of ocaml, opam, openssl.
  - so `brew install ocaml`, `brew install opam`, etc.
