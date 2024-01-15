# Import the Flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "Hello, World!"

# Run the application if this script is executed
if __name__ == "__main__":
    # Set the host and port for the web server
    # Use 0.0.0.0 to make it accessible from external devices
    app.run(host="0.0.0.0", port=5050)
