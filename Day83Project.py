from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Template styles
templates = {
    "default": """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Blog</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <h2>{date}</h2>
        <p>{content}</p>
    </body>
    </html>
    """,
    "fancy": """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Blog</title>
        <style>
            body {{
                font-family: 'Georgia', serif;
                margin: 0;
                padding: 40px;
                background-color: #90EE90;
                color: #333;
            }}
            h1 {{
                font-size: 48px;
                color: #006400;
                margin-bottom: 20px;
            }}
            h2 {{
                font-size: 36px;
                color: #006400;
                margin-bottom: 30px;
            }}
            p {{
                font-size: 24px;
                line-height: 1.6;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <h2>{date}</h2>
        <p>{content}</p>
    </body>
    </html>
    """
}

@app.route('/hello')
def hello():
    # Get template style from URL parameter, default to 'default' if not specified
    template_style = request.args.get('template', 'default')
    
    # Get the template (use default if specified template doesn't exist)
    template = templates.get(template_style, templates['default'])
    
    # Format current date
    current_date = datetime.now().strftime("%B %dth")
    
    # Return the formatted template
    return template.format(
        title="Hello World",
        date=current_date,
        content="Here is my first blog entry."
    )

if __name__ == '__main__':
    app.run(debug=True)
