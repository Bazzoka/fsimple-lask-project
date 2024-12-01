from flask import Flask, render_template

app = Flask(__name__)

guns = [
    
    {"id": 2, "name": "M4 Carbine", "price": "$1200", "description": "A lightweight carbine.", "image": "th.5.jpg"},
    {"id": 3, "name": "Glock 17", "price": "$500", "description": "A compact 9mm pistol.", "image": "th.6.jpg"},
    {"id": 4, "name": "Remington 870", "price": "$800", "description": "A versatile pump shotgun.", "image": "th.7.jpg"},
    {"id": 5, "name": "Barrett M82", "price": "$9000", "description": "A .50 caliber sniper rifle.", "image": "th.8.jpg"}
]

@app.route('/')
def index():
    return render_template("index.html", guns=guns)

if __name__ == "__main__":
    app.run(debug=True)
