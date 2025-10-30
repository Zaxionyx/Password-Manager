Password Manager (CLI)

A minimal command-line password helper written in Python.
It does two things well:
	1.	Generate strong random passwords using Python’s secrets module.
	2.	Check if a user-entered password meets basic strength rules.

No external dependencies. Works on any system with Python 3.

⸻

✨ Features
	•	Cryptographically secure generation via secrets.choice
	•	Custom length (≥ 5 characters)
	•	Strength checker requires:
	•	at least 5 characters
	•	at least one uppercase letter (A-Z)
	•	at least one lowercase letter (a-z)
	•	at least one digit (0-9)
	•	at least one special character from: !@#$%^&*()-+_=,
	•	Simple interactive CLI menu

Note: The generator uses string.punctuation (a broader set) while the checker validates against the subset above.

⸻

📦 Requirements
	•	Python 3.x (standard library only)

⸻

🚀 Quick Start
	1.	Clone the repository:

git clone https://github.com/zaxionynx/Password-Manager.git
cd Password-Manager


	2.	Run the script:

python3 main.py



You’ll see a menu:

Welcome to password manager!
This is where you can generate a strong password, check your password strength, and more to come!
Input 1: Generate Password
Input 2: Check Password Strength


⸻

🧑‍💻 Usage

1) Generate a password
	•	Choose 1
	•	Enter a length (integer ≥ 5)
	•	The app prints a random password composed of:
	•	lowercase, uppercase, digits, and punctuation

Example

Random String Length: 16
Generated Password String for the length of 16: dJ8?m9V... (example)

2) Check password strength
	•	Choose 2
	•	Enter a username (for the final echo)
	•	Enter a password; the program will tell you what’s missing until it’s strong

Strength rules
	•	length ≥ 5
	•	contains uppercase, lowercase, digit
	•	contains at least one of: !@#$%^&*()-+_=,

⸻

📁 Project Structure

Password-Manager/
└─ main.py


⸻

🔒 Security Notes
	•	This is a learning/demo tool. It prints passwords to the console.
	•	It does not store or encrypt passwords yet.
	•	For real-world use, consider:
	•	masking input via getpass
	•	hashing/Encrypting storage (e.g., cryptography/argon2-cffi)
	•	adding clipboard integration with timeout
	•	avoiding printing secrets to stdout

⸻

🛣️ Roadmap (Ideas)
	•	Save credentials to an encrypted local vault
	•	Add clipboard copy with auto-clear
	•	Configurable allowed special characters
	•	Unit tests for validation rules
	•	Packaging with pipx for easy install

⸻

🤝 Contributing

Issues and PRs are welcome!
Please open an issue describing the change you propose.

⸻



⸻

🙌 Acknowledgments
	•	Python standard library: secrets, string

⸻
