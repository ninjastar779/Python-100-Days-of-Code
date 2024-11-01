from flask import Flask
app = Flask(__name__)

@app.route('/<page_number>')
def home(page_number):
    page = ""
    f = open("templates/journal.html", "r")
    page = f.read()
    entries = {
        "78": ["Example Link", "This was very fun to do."],
        "79": ["Example Link", "I don't know what could come up."],
    }

    page = page.replace("{day}", page_number)

    if page_number in entries:
        page = page.replace("{link}", entries[page_number][0])
        page = page.replace("{text}", entries[page_number][1])
    return page


app.run(host="0.0.0.0", port=81)