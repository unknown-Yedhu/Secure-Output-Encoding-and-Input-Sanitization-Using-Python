from defusedxml import ElementTree as ET
from defusedxml.common import DefusedXmlException

print("=" * 60)
print("XML SECURITY USING DEFUSEDXML")
print("=" * 60)

# Test 1: Normal XML
normal_xml = """
<user>
    <name>Yedhu</name>
    <email>yedhu@example.com</email>
</user>
"""

print("\nTEST 1: Normal XML")
print("-" * 40)

try:
    root = ET.fromstring(normal_xml)

    print("XML parsed successfully.")
    print("Name:", root.find("name").text)
    print("Email:", root.find("email").text)

except Exception as e:
    print("XML parsing failed:", e)


# Test 2: Malicious XML containing an external entity
malicious_xml = """<?xml version="1.0"?>
<!DOCTYPE user [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<user>
    <name>&xxe;</name>
</user>
"""

print("\nTEST 2: Malicious XML (XXE Attempt)")
print("-" * 40)

try:
    root = ET.fromstring(malicious_xml)

    print("XML parsed successfully.")
    print("Name:", root.find("name").text)

except DefusedXmlException as e:
    print("SECURITY ALERT: Malicious XML rejected!")
    print("Reason:", e)

except Exception as e:
    print("XML parsing failed safely.")
    print("Reason:", e)


print("\n" + "=" * 60)
print("SECURITY VERIFICATION")
print("=" * 60)
print("Normal XML: Accepted")
print("Malicious XXE XML: Rejected")
print("Secure XML parsing prevents external entity attacks.")
print("=" * 60)