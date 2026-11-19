import html

# Sample user input containing special HTML characters
user_input = '<script>alert("XSS Attack")</script> & "Hello"'

print("=" * 60)
print("SECURE OUTPUT ENCODING USING PYTHON HTML LIBRARY")
print("=" * 60)

print("\nOriginal User Input:")
print(user_input)

# Encode special HTML characters
encoded_output = html.escape(user_input, quote=True)

print("\nEncoded Output:")
print(encoded_output)

print("\nVerification:")
print("Original input contains HTML special characters.")
print("Encoded output converts special characters into HTML entities.")

print("\n" + "=" * 60)
print("RESULT: HTML encoding successfully prevents HTML interpretation.")
print("=" * 60)