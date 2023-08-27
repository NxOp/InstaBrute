# InstaBrute

**Disclaimer:** This tool is intended for educational purposes only. Do not use it for malicious activities or unauthorized access. The developer is not responsible for any misuse.

## Description

The Instagram Password Testing Tool is a Python script designed to test a list of passwords against an Instagram account. It sends HTTP requests to the Instagram login endpoint for each password and analyzes the responses to determine if a password is correct or not. The tool provides a graphical banner, colored text output, and is designed to run in the terminal.

## Features

- ASCII art banner with colorful presentation.
- Different text colors for better visibility.
- Password testing against an Instagram account.
- Educational tool for learning about HTTP requests and responses.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/NxOp/InstaBrute
   cd InstaBrute
   ```

2. Run the script:

   ```bash
   python Instabrute.py
   ```

## Commands for Different Operating Systems

- **Linux / macOS:**

  Open a terminal and navigate to the directory where the script is located. Run the script using Python:

  ```bash
  python Instabrute.py
  ```

- **Windows:**

  Open Command Prompt or PowerShell and navigate to the directory where the script is located. Run the script using Python:

  ```bash
  python Instabrute.py
  ```

## Input

You will be prompted to provide the following information:

- Instagram username: Enter the username of the Instagram account you want to test.
- List of passwords: Provide the path to a file containing a list of passwords, with each password on a new line.
- You can make your own pass.txt ( Wordlist ) https://pwgen-win.sourceforge.io/

## Output

The tool will analyze the responses from Instagram's login endpoint for each password and display the results:

- If the password is correct, it will be displayed in green.
- If there is an issue with the request or the password is incorrect, it will be displayed in red.
- If there is an error with the response, it will be indicated in the output.


## ScreenShot
<img width="721" alt="image" src="https://github.com/NxOp/InstaBrute/assets/143170755/80eaa526-3374-4a22-b174-7d1d97418963">

## Disclaimer

This tool is provided for educational purposes only. The developer does not condone or support any malicious activities or unauthorized access.

---
