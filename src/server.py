from flask import Flask
from healthcheck import healthcheck_api
from reward import reward_api
from werkzeug.middleware.profiler import ProfilerMiddleware

app = Flask(__name__)

app.register_blueprint(healthcheck_api, url_prefix='/api')
app.register_blueprint(reward_api, url_prefix='/api')

if __name__ == "__main__":
  app.config['PROFILE'] = True
  app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
  app.run(debug = True)
