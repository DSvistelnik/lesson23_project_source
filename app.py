from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/perform_query", methods=['GET'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    args = request.values

    if not checker.is_valid(args):
        abort(400)
    return app.response_class('', content_type="text/plain")
