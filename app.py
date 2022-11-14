from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)  # Приложение Flask



dist_result = {
    'user': 'admin',
    'password': 'admin'
}


# region | API: /get_ksp_name | Получение списка отделений
@app.route('/get_user_admin', methods=['GET'])
def get_user_admin():
    return (jsonify(dist_result), 201)
# endregion


if __name__ == '__main__':
    """ ПРИЛОЖЕНИЕ """

    ip = '127.0.0.1'
    port = 8050

    CORS(app)
    app.run(debug=False, port=port, host=ip)