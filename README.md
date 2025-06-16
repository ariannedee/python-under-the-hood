# Python Under the Hood Live Training

This is the code for the *O'Reilly Live Training* - **Python Under the Hood** presented by Arianne Dee

Before the class, please follow these instructions:
1. [Install Python](#1-ensure-python-39-or-higher-is-installed)
2. [Use an appropriate code editor](#2-use-an-appropriate-code-editor)
3. [Download the code](#3-download-the-course-files)
4. [Install package dependencies](#4-install-package-dependencies)
5. [Download the resources](#5-at-the-beginning-of-class-download-the-resources)

## Set up instructions
### 1. Ensure Python 3.9 or higher is installed
Install the latest version here: https://www.python.org/downloads/

In *PowerShell* on Windows or *Terminal* on Mac or Linux,
make sure you can access Python from the command line.

1. `$ python --version`
2. `$ python3 --version`
3. `$ python3.13 --version` (replace 3.13 with your target version number)
4. `$ py --version` on Windows
5. `$ py -3.13 --version` (replace 3.13 with your target version number)

One or more of those commands should print 
a Python version of 3.9 or higher.

### 2. Use an appropriate code editor
The instructor will demo using PyCharm: https://www.jetbrains.com/pycharm/download/

The example code requires being able to run Python scripts (.py files)
and commands in the terminal (e.g. `$ python -m <module>`).

### 3. Download the course files
GitHub repository: https://github.com/ariannedee/python-under-the-hood

#### If you know git:
Clone the repository.

#### If you don't know git:
1. Click the "< > Code" (green) button at the top-right of the page
2. Click "Download ZIP"
3. Unzip it and move the **python-under-the-hood-main** folder to a convenient location

### 4. Install package dependencies
Optional: set up a new virtual environment

Then install dependencies in `requirements.txt`.

`$ pip install -r requirements.txt`

Or use one of PyCharm's many package installer features.

### 5. At the beginning of class, download the resources
When you have signed in to the class,
the **Resources** widget will have PDFs for the slides.

## FAQs

### PyCharm can't find Python 3

On a Mac:
- Go to **PyCharm** > **Preferences**

On a PC:
- Go to **File** > **Settings**

Once in Settings:
1. Go to **Project: oop-python** > **Project Interpreter**
2. Look for your Python version in the Project Interpreter dropdown
3. If it's not there, click **gear icon** > **Add...**
4. In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
5. If it's not there, click the **...** button and navigate to your Python location
   - To find where Python is located, [look in these directories](docs/PYTHON-LOCATIONS.md)
   - You may have to search the internet for where Python gets installed by default on your operating system
