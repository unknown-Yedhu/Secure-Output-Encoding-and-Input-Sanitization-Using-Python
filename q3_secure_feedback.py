from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Feedback Application</title>
</head>
<body>
    <h1>Secure Feedback Application</h1>

    <form method="POST">
        <label for="feedback">Enter your feedback:</label><br><br>

        <textarea id="feedback" name="feedback" rows="5" cols="50"></textarea>

        <br><br>

        <button type="submit">Submit Feedback</button>
    </form>

    {% if feedback %}
        <h2>Submitted Feedback</h2>
        <p>{{ feedback }}</p>
    {% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    feedback = ""

    if request.method == "POST":
        feedback = request.form.get("feedback", "")

    return render_template_string(
        HTML_TEMPLATE,
        feedback=feedback
    )


if __name__ == "__main__":
    print("=" * 60)
    print("SECURE FEEDBACK DISPLAY APPLICATION")
    print("=" * 60)
    print("Starting Flask server...")
    print("Open: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(debug=True)