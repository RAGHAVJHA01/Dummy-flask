from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Welcome to the Dummy Flask App!"

@app.route('/api/data')
def get_data():
    data = {
        "name": "Flask App",
        "version": "1.0",
        "description": "This is a dummy API endpoint."
    }
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
