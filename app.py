import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return f"this is from slot 1 updated. pleaseeeeeeeeeeeeeeeeeyyyyyy"

if __name__ == "__main__":
    app.run()
