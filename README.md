# getconnectedwifipasswords

A simple Python script to display saved Wi-Fi passwords for networks that your system has previously connected to.

## Features

- **Lists Wi-Fi passwords** for all networks that your computer has been connected to in the past.
- **Does NOT retrieve passwords** for unknown or nearby Wi-Fi networks your device has never connected to.
- Compatible with most Windows systems (for Linux/Mac support, additional scripting may be required).

## How It Works

This script queries your system for known Wi-Fi profiles and displays their saved passwords, if available. It does **not** hack or guess passwords for networks that your device has never connected to.

## Usage

1. **Clone or download** this repository.
2. Make sure you have **Python 3** installed on your system.
3. Open a terminal or command prompt.
4. Run the script:

   ```bash
   python getconnectedwifipasswords.py
   ```

5. The script will display a list of Wi-Fi network names (SSIDs) along with their saved passwords.

## Important Notes

- This script only works for Wi-Fi networks that have been previously connected and whose credentials are stored on your system.
- You must have appropriate permissions to access network configuration information.
- **Do not use this script for malicious purposes.** It is intended for personal recovery and educational use only.

## Example Output

```
Wi-Fi Name: MyHomeNetwork
Password: mysecretpassword

Wi-Fi Name: OfficeNet
Password: office2021!
```
