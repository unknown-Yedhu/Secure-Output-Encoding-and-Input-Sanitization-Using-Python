from ldap3.utils.conv import escape_filter_chars

print("=" * 60)
print("LDAP INJECTION PREVENTION")
print("=" * 60)

# Test inputs containing LDAP special characters
test_inputs = [
    "Yedhu",
    "*",
    "(",
    ")",
    "\\",
    "admin*)(uid=*)",
    "user\x00name"
]

print("\nLDAP Filter Escaping Tests")
print("-" * 60)

for user_input in test_inputs:

    # Escape LDAP filter special characters
    escaped_input = escape_filter_chars(user_input)

    # Construct LDAP filter safely
    ldap_filter = f"(uid={escaped_input})"

    print("\nOriginal Input:")
    print(repr(user_input))

    print("Escaped Input:")
    print(repr(escaped_input))

    print("LDAP Filter:")
    print(ldap_filter)


print("\n" + "=" * 60)
print("SECURITY VERIFICATION")
print("=" * 60)
print("LDAP special characters have been escaped.")
print("User input cannot alter LDAP filter structure.")
print("=" * 60)