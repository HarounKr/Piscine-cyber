# Stockholm.py

**Stockholm.py** is an educational tool designed to provide insight into ransomware attacks. Through its implementation, users can gain an understanding of how ransomware operates, all within a controlled and harmless environment.

## What is a Ransomware Attack?

Ransomware is a type of malicious software (malware) that encrypts the victim's data, making it inaccessible. The attacker then demands a ransom from the victim in exchange for the decryption key to restore their data. These attacks can target individuals, businesses, and even public institutions, leading to significant data loss, financial costs, and other severe consequences.

## Directory Structure:

├── create_files.py - Generates template files for testing the program.  
├── generate_key.py - Produces an encryption key and stores it in key.key.  
├── stockholm.py - Main executable of the program.  
│ ├── (no options) - Encrypts files in the directory, appending a .ft extension.  
│ ├── -v - Displays the version of the program.  
│ ├── -s - Silent mode: No output displayed.  
│ └── -r '<file.key>' - Decrypts files using the provided key.  
└── Makefile - Installs necessary dependencies.  

## Usage:

1. Clone the repository
2. Navigate to the repository's directory
3. Install the dependencies: execute command make
4. Move to the `~/infection` directory: cd  ~/infection
5. Execute the program: python3 stockholm.py


## Disclaimer:

**Warning**: This project is for educational purposes only. You should never use this type of program for malicious purposes.

