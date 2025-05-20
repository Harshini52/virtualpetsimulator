from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Initialize pet data
pet = {
    "name": "Fluffy",
    "happiness": 50,
    "hunger": 50,
    "mood": "happy"
}

@app.route('/')
def home():
    return render_template('index.html', pet=pet)

@app.route('/feed', methods=['POST'])
def feed():
    pet["hunger"] = max(0, pet["hunger"] - 15)
    pet["happiness"] = max(0, pet["happiness"] - 5)
    update_mood()
    return jsonify(pet)

@app.route('/play', methods=['POST'])
def play():
    pet["happiness"] = min(100, pet["happiness"] + 15)
    pet["hunger"] = min(100, pet["hunger"] + 5)
    update_mood()
    return jsonify(pet)

@app.route('/update', methods=['POST'])
def update():
    # Simulate time passing
    pet["hunger"] = min(100, pet["hunger"] + 5)
    pet["happiness"] = max(0, pet["happiness"] - 5)
    update_mood()
    return jsonify(pet)

def update_mood():
    if pet["happiness"] > 70:
        pet["mood"] = "happy"
    elif pet["happiness"] > 30:
        pet["mood"] = "neutral"
    else:
        pet["mood"] = "sad"

if __name__ == '__main__':
    app.run(debug=True)