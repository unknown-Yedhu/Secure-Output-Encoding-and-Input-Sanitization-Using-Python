import json
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Encoding Demo</title>
</head>
<body>
    <h1>JavaScript Output Encoding</h1>

    <form method="POST">
        <label>Enter your name:</label><br><br>
        <input type="text" name="name" required>
        <button type="submit">Submit</button>
    </form>

    <p id="welcome"></p>

    <script>
        const username = {{ encoded_name | safe }};

        document.getElementById("welcome").textContent =
            "Welcome, " + username + "!";
    </script>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    name = ""

    if request.method == "POST":
        name = request.form.get("name", "")

    # JSON serialization
    encoded_name = json.dumps(name)

    # Escape characters that could break out of a script context
    encoded_name = (
        encoded_name
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )

    return render_template_string(
        HTML_TEMPLATE,
        encoded_name=encoded_name
    )


if __name__ == "__main__":
    print("=" * 60)
    print("JAVASCRIPT OUTPUT ENCODING DEMONSTRATION")
    print("=" * 60)
    print("Starting Flask server...")
    print("Open: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(debug=True)