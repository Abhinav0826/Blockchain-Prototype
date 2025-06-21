# Simple Blockchain Prototype in Python

This is a lightweight, blockchain prototype built from scratch in Python. It simulates the core principles of a blockchain such as block creation, block headers,  mining (proof of work), and persistent storage using a local JSON file.

## Features

- Genesis block creation on startup
- Proof-of-work mining logic
- Block linking via previous block hash
- Simulated transactions and Merkle root hashing
- Real-time block appending
- Persistent storage using a local JSON file (no external DB)
- Code is organized into separate modules for blockchain logic, file storage, and helper functions.

## Block Output
<img width="1383" alt="Screenshot 2025-06-21 at 12 10 28 AM" src="https://github.com/user-attachments/assets/cc78de4f-f853-4bd7-89a0-2e5a5d9d4234" />


## Tech Stack

- Python 3.12
- `hashlib`, `json`, `os`, `time`, `sys`
- File-based JSON storage
