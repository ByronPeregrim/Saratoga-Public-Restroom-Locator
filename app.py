from flask import Flask, render_template, jsonify
from database import load_locations_from_db, load_location_from_db

app = Flask(__name__)
        
@app.route("/")
def hello_world():
    locations = load_locations_from_db()
    return render_template('index.html',
                           locations=locations)

@app.route("/api/locations")
def list_locations():
    locations = load_locations_from_db()
    return jsonify(locations)

@app.route("/location/<id>")
def show_location(id):
    location = load_location_from_db(id)
    if not location:
        return "Not Found", 404
    return render_template('locationpage.html',
                           location=location)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)