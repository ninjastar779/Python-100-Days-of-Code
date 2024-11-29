from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template with the form
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Robot Verification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        select, input[type="text"], button {
            padding: 5px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <form method="POST">
        <div class="form-group">
            <label>Are you made of metal?</label><br>
            <input type="radio" name="metal" value="yes" required> Yes<br>
            <input type="radio" name="metal" value="no"> No
        </div>
        
        <div class="form-group">
            <label>What is infinity + 1?</label><br>
            <input type="text" name="infinity" required>
        </div>
        
        <div class="form-group">
            <label>Which is your favorite food?</label><br>
            <select name="food" required>
                <option value="">Select food...</option>
                <option value="human_food">Human food</option>
                <option value="electricity">Electricity</option>
                <option value="oil">Oil</option>
                <option value="data">Data</option>
            </select>
        </div>
        
        <button type="submit">I am not a robot</button>
    </form>
    
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        metal = request.form.get("metal")
        infinity = request.form.get("infinity").lower()
        food = request.form.get("food")
        
        # Check if answers indicate a robot
        if metal == "yes" or infinity == "error" or food in ["electricity", "oil", "data"]:
            message = "Nice try, robot! 🤖"
        else:
            message = "Verification successful! You seem human! 👋"
    
    return render_template_string(template, message=message)

if __name__ == "__main__":
    app.run(debug=True)