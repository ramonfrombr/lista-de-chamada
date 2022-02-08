from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource


api_bp = Blueprint('api', __name__)

api = Api(api_bp)


from . import rotas