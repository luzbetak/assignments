
# ASCII Policy Number Management System

This project manages policy numbers represented in ASCII format. It includes scripts for generating, validating, and correcting these ASCII numbers, ensuring data consistency and integrity through checks and corrections.

## Project Overview

The project contains four main Python scripts:

1. **1-write_policy_numbers.py**: Generates and writes random ASCII-encoded policy numbers to a file.
2. **2-read_validate_ascii_numbers.py**: Reads and validates the ASCII-encoded policy numbers, marking any that are unrecognizable or fail checksum validation.
3. **3-fix_ill_policy_numbers.py**: Attempts to correct ASCII policy numbers marked as "ILL" (illegible) or "ERR" (checksum error).
4. **checksum.py**: Provides utility functions for calculating checksums and reading/writing ASCII policy numbers.

## Requirements

- Python 3.x
- Basic understanding of ASCII encoding
- Standard Python libraries (e.g., `random`, `sys`, `re`)

## File Descriptions

### 1. 1-write_policy_numbers.py
- **Purpose**: Generates random 9-digit ASCII numbers and writes them to `ascii_numbers_bronze.txt`.
- **Key Features**:
  - Creates an ASCII representation of each digit.
  - Introduces occasional random errors for testing correction logic.

### 2. 2-read_validate_ascii_numbers.py
- **Purpose**: Reads ASCII numbers from `ascii_numbers_bronze.txt` and validates them.
- **Key Features**:
  - Converts ASCII representation back to numerical digits.
  - Marks numbers with unrecognized characters as "ILL" and those failing the checksum as "ERR".
  - Writes validated results to `ascii_numbers_silver.txt`.

### 3. 3-fix_ill_policy_numbers.py
- **Purpose**: Fixes ASCII numbers marked as "ILL" or "ERR".
- **Key Features**:
  - Attempts to replace unrecognized digits ("?") to fix "ILL" entries.
  - Corrects "ERR" entries by making single-character replacements and re-checking the checksum.
  - Outputs results to `ascii_numbers_gold.txt` and `ascii_numbers_platinum.txt`.

### 4. checksum.py
- **Purpose**: Provides utility functions for the project.
- **Key Functions**:
  - `calculate_checksum(ascii_number)`: Checks if an ASCII number passes the checksum.
  - `read_ascii_numbers(file_path)`: Reads numbers from a specified file.
  - `write_ascii_numbers(file_path, ascii_numbers)`: Writes corrected numbers to a file.

## How to Run the Project

1. **Generate ASCII Numbers**:
   ```bash
   python 1-write_policy_numbers.py <number_of_policies>
   ```

2. **Validate and Mark ASCII Numbers**:
   ```bash
   python 2-read_validate_ascii_numbers.py
   ```

3. **Fix Ill or Erroneous ASCII Numbers**:
   ```bash
   python 3-fix_ill_policy_numbers.py
   ```

## Example Workflow

1. Run `1-write_policy_numbers.py` to generate a file `ascii_numbers_bronze.txt` containing ASCII-encoded numbers.
2. Use `2-read_validate_ascii_numbers.py` to validate and create `ascii_numbers_silver.txt`, marking entries as "ILL" or "ERR" if needed.
3. Finally, execute `3-fix_ill_policy_numbers.py` to correct entries, resulting in updated files `ascii_numbers_gold.txt` and `ascii_numbers_platinum.txt`.

