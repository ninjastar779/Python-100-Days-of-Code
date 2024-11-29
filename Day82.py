from flask import Flask, request

app = Flask(__name__)

# Dictionary of greetings in different languages
greetings = {
    "wel": "Helo, a chroeso i'n gwefan wych!",
    "eng": "Hello, and welcome to our great website!",
    "esp": "¡Hola y bienvenidos a nuestro gran sitio web!"
}

@app.route('/language')
def hello():
    # Get the language parameter from the URL, default to English if not specified
    lang = request.args.get('lang', 'eng')
    
    # Return the greeting in the requested language, or English if language not found
    return f"""
    <!DOCTYPE html>
    <html lang="{lang}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Multilingual Greeting</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-size: 24px;
            }}
        </style>
    </head>
    <body>
        <h1>{greetings.get(lang, greetings['eng'])}</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)