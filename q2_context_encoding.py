from flask import Flask, request, render_template_string
from urllib.parse import urlencode

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Context-Specific Encoding Demo</title>
</head>
<body>
    <h1>Context-Specific Output Encoding</h1>

    <h2>1. HTML Context</h2>
    <p>User input: {{ user_input }}</p>

    <h2>2. JavaScript Context</h2>
    <p id="js-output"></p>

    <script>
        const username = {{ user_input | tojson }};
        document.getElementById("js-output").textContent =
            "JavaScript safely received: " + username;
    </script>

    <h2>3. URL Context</h2>
    <p>
        Encoded URL:
        <a href="{{ encoded_url }}">
            {{ encoded_url }}
        </a>
    </p>

</body>
</html>
"""


@app.route("/")
def home():
    user_input = request.args.get(
        "name",
        '<script>alert("XSS Attack")</script> & Hello'
    )

    # URL encoding
    query_string = urlencode({"name": user_input})
    encoded_url = "/?" + query_string

    return render_template_string(
        HTML_TEMPLATE,
        user_input=user_input,
        encoded_url=encoded_url
    )


if __name__ == "__main__":
    print("=" * 60)
    print("CONTEXT-SPECIFIC OUTPUT ENCODING DEMONSTRATION")
    print("=" * 60)
    print("Starting Flask server...")
    print("Open: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(debug=True)