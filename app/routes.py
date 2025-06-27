from flask import Blueprint, jsonify
import random
from .insults import generate_insult

bp = Blueprint('insults', __name__)

@bp.route('/insult', methods=['GET'])
def get_insult():
    insult = generate_insult()
    return jsonify({'insult': insult})