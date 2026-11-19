from urllib.parse import urlencode, quote

print("=" * 60)
print("URL ENCODING DEMONSTRATION")
print("=" * 60)

# Sample user input containing special characters
user_input = "Hello World & name=Yedhu? Python@2026"

print("\nOriginal User Input:")
print(user_input)

# Encode using urlencode()
encoded_parameters = urlencode({"input": user_input})

print("\nEncoded Query Parameters:")
print(encoded_parameters)

# Encode using quote()
encoded_text = quote(user_input)

print("\nEncoded Using quote():")
print(encoded_text)

# Construct a URL
url = "https://example.com/search?" + encoded_parameters

print("\nFinal URL:")
print(url)

print("\nVerification:")
print("Spaces, &, =, ?, and special characters are encoded.")

print("\n" + "=" * 60)
print("RESULT: URL encoding completed successfully.")
print("=" * 60)