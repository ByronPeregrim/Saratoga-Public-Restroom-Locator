from flask import Flask, render_template, jsonify
from database import load_locations_from_db
from sqlalchemy import text

app = Flask(__name__)
        
@app.route("/")
def hello_world():
    locations = load_locations_from_db()
    return render_template('index.html',
                           locations=locations)

@app.route("/location/<id>")
def list_locations():
    locations = load_locations_from_db()
    return jsonify(locations)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)