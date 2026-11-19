import subprocess
import sys

print("=" * 60)
print("OS COMMAND INJECTION PREVENTION")
print("=" * 60)


def process_filename(filename):
    """
    Safely process user input using subprocess.
    shell=False ensures input is treated as an argument.
    """

    print("\nInput Filename:")
    print(filename)

    # Execute Python safely with an argument list
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys; print('Processed filename:', sys.argv[1])",
            filename
        ],
        capture_output=True,
        text=True,
        shell=False
    )

    print("\nCommand Output:")
    print(result.stdout.strip())

    if result.stderr:
        print("Error:", result.stderr)

    print("Return Code:", result.returncode)


# Test 1: Normal filename
print("\nTEST 1: Normal Filename")
print("-" * 40)

process_filename("document.txt")


# Test 2: Filename containing shell metacharacters
print("\nTEST 2: Filename with Shell Metacharacters")
print("-" * 40)

malicious_filename = "file.txt & echo INJECTION"

process_filename(malicious_filename)


print("\n" + "=" * 60)
print("SECURITY VERIFICATION")
print("=" * 60)
print("subprocess.run() used with an argument list.")
print("shell=False prevents shell interpretation.")
print("User input is treated as data, not as a command.")
print("=" * 60)