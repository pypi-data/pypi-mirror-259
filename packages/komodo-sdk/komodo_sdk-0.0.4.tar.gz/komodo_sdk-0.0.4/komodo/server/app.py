import os

from flask import Flask, render_template, request, jsonify

from komodo.loaders.appliance_loader import ApplianceLoader
from komodo.loaders.user_loader import UserLoader
from komodo.models.framework.runners import run_appliance

app = Flask(__name__)
app.static_folder = os.path.dirname(__file__) + '/static'
app.template_folder = os.path.dirname(__file__) + '/templates'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/api/v1', methods=['GET'])
def api_root():
    return render_template('index.html')


@app.route('/api/v1/user-profile', methods=['GET'])
def user_profile():
    # Extract email from the X-User-Email header
    email = request.headers.get('X-User-Email')
    if not email:
        return jsonify({"error": "X-User-Email header missing"}), 400

    user = UserLoader.load(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return user.to_dict()


@app.route('/api/v1/appliance', methods=['GET'])
def get_appliance():
    guid = request.args.get('guid')
    name = request.args.get('name')
    appliance = ApplianceLoader.load('sample')

    if not appliance:
        return jsonify({"error": "Appliance not found"}), 404

    # Convert the protobuf Appliance object to a dictionary for JSON response
    appliance_dict = {
        "shortcode": 'sample',
        "name": appliance.name,
        "purpose": appliance.purpose,
    }

    return jsonify(appliance_dict)


@app.route('/api/v1/agents', methods=['GET'])
def get_agents():
    appliance = ApplianceLoader.load('sample')
    return jsonify([a.to_dict() for a in appliance.agents])


# Endpoint to list agents
@app.route('/appliance/list', methods=['GET'])
def list_agents():
    appliance = ApplianceLoader.load('sample')
    return jsonify({"agents": [a.to_dict() for a in appliance.agents]})


# Endpoint to ask an agent a question
@app.route('/agent/ask', methods=['GET', 'POST'])
def ask_agent():
    message = "how are you doing today"
    appliance = ApplianceLoader.load('sample')
    reply = run_appliance(appliance, message)
    return jsonify({"reply": reply.text, "message": message})


if __name__ == '__main__':
    app.run(debug=True)
