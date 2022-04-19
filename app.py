from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, jsonify, render_template
import json
from waitress import serve

app = Flask(__name__)

SWAGGER_URL = "/swagger"
API_URL = "/static/openapi.yaml"
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "doc"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


def clear_file(string):
    return string.replace('\n', '')


@app.route("/contacts")
def get_contacts():
    with open("contacts.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        # n = dict(data['CONTACTS of VC'])
        data_ = data["Center"]
        encoding_data = json.dumps(data_, sort_keys=False, ensure_ascii=False, indent=4)
        clear_data = clear_file(encoding_data)
    return clear_data


@app.route("/news")
def get_news():
    with open("news.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        data_ = data["News"]
        encoding_data = json.dumps(data_, sort_keys=False, ensure_ascii=False, indent=4)
        clear_data = clear_file(encoding_data)
    return clear_data


@app.route("/")
def index():
    return render_template("/index.html")


# @app.route("/documentation")
# def get_documentation():
#     pass


def start_flask():
    # if __name__ == "__main__":
    # app.run(ssl_context="adhoc", port=5000, debug=True)

    serve(app, host='0.0.0.0', port=8080, threads=1)
