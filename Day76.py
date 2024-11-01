from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/portfolio")
def portfolio():
    return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Day74.css">
    <title>Day74</title>
</head>

<body>
    <h1>My First Website (Updated to Add CSS)</h1>
    <h2>How I first got into STEM</h2>
    <div>
        <p>When I was in middle school, I loved robotics. I was in a Lego Robotics team after school and I liked to
            build things.</p>
        <p>After a while, I decided to do some coding. During the summer, I took a coding bootcamp on YouTube.</p>
        <p>This is one of the playlists that I used to learn how to code: <a
                href="https://www.youtube.com/playlist?list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0">https://www.youtube.com/playlist?list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0</a>
        </p>
    </div>
</body>

</html>"""


@app.route("/index")
def index_project():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day75Project</title>
    <style>
        body {
            background-color: black;
            color: white;
        }

        h1 {
            text-align: center;
            color: skyblue;
        }

        p {
            text-align: center;
            color: lightgreen;
        }

        div {
            text-align: center;
            border: 2px solid white;
        }

        a {
            color: white;
        }
    </style>
</head>
<body>
    <h1>Neel Debnath</h1>
    <p>Bangladeshi-American Programmer</p>

    <div>
        <a href="https://github.com/ninjastar779">Github (@ninjastar779)</a>
    </div>
</body>
</html>"""


app.run(host="0.0.0.0", port=81)
