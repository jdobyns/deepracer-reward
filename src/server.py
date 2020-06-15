from flask import Flask
from healthcheck import healthcheck_api
from reward import reward_api

app = Flask(__name__)

app.register_blueprint(healthcheck_api, url_prefix='/api')
app.register_blueprint(reward_api, url_prefix='/api')

if __name__ == "__main__":
  app.run()
