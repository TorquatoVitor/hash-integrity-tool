# Hash Integrity Tool

A command-line tool built with Python for generating cryptographic hashes and verifying file integrity.

The project supports multiple SHA algorithms and can generate hashes from both text and files.

## Features

- Generate hashes from text
- Generate hashes from files
- Verify file integrity
- SHA-256 support
- SHA-512 support
- SHA3-256 support
- File validation
- Basic error handling
- Interactive CLI menu

## Supported Algorithms

| Algorithm | Description |
|---|---|
| SHA-256 | Produces a 256-bit hash |
| SHA-512 | Produces a 512-bit hash |
| SHA3-256 | SHA-3 algorithm with a 256-bit output |

## How It Works

Hash functions transform input data into a fixed-size hexadecimal value.

For example:

```text
hello
```

Using SHA-256 produces:

```text
2cf24dba5fb0a30e26e83b2ac5b9e29e...
```

Even a small modification to the original data produces a completely different hash.

This makes hashes useful for checking whether a file has been modified.

## File Integrity Verification

The tool can compare the current hash of a file with an expected hash.

```text
Original file
     ↓
SHA-256
     ↓
Expected Hash
```

When verifying the file:

```text
Current Hash == Expected Hash
```

If they match, the file has the same content used to generate the expected hash.

If they do not match, the file content has changed.

## Installation

Clone the repository:

```bash
git clone https://github.com/TorquatoVitor/hash-integrity-tool.git
```

Enter the project directory:

```bash
cd hash-integrity-tool
```

Run the application:

```bash
python main.py
```

No external dependencies are required.

## Usage

After starting the application, the following menu is displayed:

```text
=====================
    HASH GENERATOR
=====================

1 - Hash text
2 - Hash file
3 - Verify file integrity
4 - Exit
```

### Hash Text

Select:

```text
1
```

Enter the text and choose the hashing algorithm.

Example:

```text
Text: hello

Choose algorithm:
1 - SHA-256
2 - SHA-512
3 - SHA3-256
```

The generated hash will then be displayed.

### Hash File

Select:

```text
2
```

Enter the path of the file and choose an algorithm.

The application reads the file in binary mode and processes it in chunks instead of loading the entire file into memory.

### Verify File Integrity

Select:

```text
3
```

Provide:

- File path
- Expected hash
- Hashing algorithm

If the hashes match:

```text
[OK] File integrity verified.
The file matches the expected hash.
```

If they do not match:

```text
[WARNING] Integrity check failed.
The file does not match the expected hash.
```

## Technical Concepts

This project demonstrates concepts such as:

- Python functions
- Loops
- Conditional statements
- File handling
- Binary file reading
- Exception handling
- Hash functions
- Cryptographic algorithms
- Data encoding
- CLI applications
- Code organization

## Technologies

- Python 3
- hashlib
- pathlib

## Project Purpose

This project was created to practice Python while exploring basic cybersecurity and cryptography concepts, especially cryptographic hashing and file integrity verification.

## Disclaimer

Hashing is not encryption.

Hash functions are one-way transformations and are commonly used for integrity verification, password storage systems, digital signatures, and other security-related applications.
