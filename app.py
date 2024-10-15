import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Access the environment variable
    my_variable = os.getenv('my_variable')
    return f"this is from slot 2"

if __name__ == "__main__":
    app.run()
