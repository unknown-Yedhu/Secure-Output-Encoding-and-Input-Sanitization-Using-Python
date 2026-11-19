import html

# XSS test payload
user_input = "<script>alert('XSS Attack')</script>"

print("=" * 60)
print("HTML ENCODING USING html.escape()")
print("=" * 60)

print("\nOriginal Input:")
print(user_input)

# Escape HTML special characters
encoded_output = html.escape(user_input)

print("\nEncoded Output:")
print(encoded_output)

print("\nVerification:")
print("Original input contains HTML tags.")
print("Encoded output converts HTML characters into safe entities.")

print("\n" + "=" * 60)
print("RESULT: XSS payload safely encoded.")
print("=" * 60)