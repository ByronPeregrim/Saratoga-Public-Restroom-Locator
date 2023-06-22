from flask import Flask, render_template, jsonify

app = Flask(__name__)

LOCATIONS = [
    {
        'id': '1',
        'title': 'Stewart\'s Shop - North Broadway',
        'address': '521 Broadway, Saratoga Springs, NY 12866',
        'hours': 'Mon-Fri 6am-11pm, Sat-Sun 24hr',
        'rating': '0'
    },
    {
        'id': '2',
        'title': 'Stewart\'s Shop - Church St',
        'address': '30 Church St, Saratoga Springs, NY 12866',
        'hours': 'Mon-Fri 6am-11pm, Sat-Sun 24hr',
        'rating': '0'
    },
    {
        'id': '3',
        'title': 'Congress Park Public Restrooms',
        'address': '16 Spring St, Saratoga Springs, NY 12866',
        'hours': 'Mon-Fri 8am-8pm, Sat-Sun 8am-3pm',
        'rating': '0'
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html',
                           locations=LOCATIONS)

@app.route("/locations")
def list_locations():
    return jsonify(LOCATIONS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)