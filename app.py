from flask import Flask, render_template, jsonify, request
from database import load_locations_from_db, load_location_from_db, add_location_to_db, add_comment_to_db, load_comments_from_db, get_location_rating, update_rating_in_db

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
    comments = load_comments_from_db()
    if not location:
        return "Not Found", 404
    rating = get_location_rating(id)
    if rating != None:
        update_rating_in_db(id, rating)
    return render_template('locationpage.html',
                           location=location,
                           comments=comments)

@app.route("/location/<id>/comment-submit", methods=['post'])
def submit_comment(id):
    data = request.form
    add_comment_to_db(id, data)
    rating = get_location_rating(id)
    if rating != None:
        update_rating_in_db(id, rating)
    return render_template('submitted.html')

@app.route("/location-form")
def render_location():
    return render_template('location-form.html')

@app.route("/location-form/submit", methods=['post'])
def submit_form():
    data = request.form
    add_location_to_db(data)
    return render_template('submitted.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)