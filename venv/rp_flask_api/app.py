# app.py

from flask import Flask, render_template
import connexion # this simplifies using Swagger/OpenAPI specs for RESTful APIs

app = connexion.App(__name__, specification_dir='./') # The API is initialized using Connexion rather than Flask directly. This allows the API to be configured based on a Swagger/OpenAPI specification file (swagger.yml) in the current directory.
app.add_api("swagger.yml") # tells Connexion to read the swagger.yml file and create API endpoints accordingly. This means the API's structure, endpoints, and their specifications are defined within swagger.yml.

# app = Flask(__name__) # App in no longer initialized using Flask directly, but rather using Connexion. This means the app is now a Connexion instance rather than a Flask instance.

@app.route('/') # Decorator for the home() function, which tells Flask to use the home() function to handle requests to the root URL ('/').
def home():
    return render_template('home.html') # Uses the render_template() function to render the home.html template. This integrates the Flask application with a front-end, providing a UI accessible via the web browser.

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True) # checks if the script is executed as the main program and runs the app on localhost (0.0.0.0) at port 8000 with debug mode enabled. Debug mode allows for more verbose output in the console and automatic reloading upon file changes.