# Import the Flask library and render_templates library
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__) #two underscores on each side of name 

# Define a route for the home page ("/")
@app.route('/')
def index():
    return render_template('index.html')

# Run the Flask app if this script is the main entry point. #two underscores on each side of name and main

if __name__ == "__main__":
    app.run(debug=True)
