import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Access the environment variable
    my_variable = os.environ.get('MY_VARIABLE', 'Default Value')
    return f"Value of MY_VARIABLE is: {my_variable}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
