from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice_pl(nickname, level, rating):
    return f"""<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" href="../static/css/style.css" />
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                              </head>
                              <body>
                                <h1>Результаты отбора</h1>
                                <h2>Претендента на участие {nickname}
                                 <div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                                 <div>составляет {rating}</div>
                                 <div class="alert alert-warning" role="alert">Желаем удачи</div>
                                </div>
                              </body>
                            </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')