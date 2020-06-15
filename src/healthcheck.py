from flask import Blueprint, request
import json

healthcheck_api = Blueprint('healthcheck_api', __name__)

@healthcheck_api.route("/healthcheck")
def healthcheck():
  return {
    'message': 'success',
    'version': '0.0.1'
  }
