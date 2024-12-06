from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Serve the HTML calculator page
@app.route("/")
def calculator():
    return render_template_string(open("index.html").read())

# API to evaluate mathematical expressions
@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.json
        expression = data.get("expression", "")
        # Safely evaluate the expression
        result = eval(expression)
        return jsonify({"result": result})
    except Exception:
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run(debug=True)