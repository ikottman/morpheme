from flask import Blueprint, jsonify


text_blueprint = Blueprint('text', __name__)

@text_blueprint.route('/text', methods=['GET'])
def index():
    return jsonify({
        'name': 'Hardcoded test data',
        'author': 'me',
        'text': 'This will be a blob of text'
    })