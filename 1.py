from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/choice/<planet_name>')
def choice_pl(planet_name):
    if planet_name[0] == 'М':
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
                                <h1>Моё предложение: {planet_name}!</h1>
                                 <div class="alert alert-success" role="alert">Название начинается на М</div>
                                 <div class="alert alert-dark" role="alert">Мы сделаем обитаемыми безжизненные пока планеты</div>
                                 <div class="alert alert-warning" role="alert">И начнём с Марса!</div>
                                 <div class="alert alert-danger" role="alert">Присоединяйся!
                                </div>
                              </body>
                            </html>"""
    else:
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
                                        <h1>Жди нас, {planet_name}!</h1>
                                         <div class="alert alert-success" role="alert">Название не на М</div>
                                         <div class="alert alert-dark" role="alert">Мы сделаем обитаемыми безжизненные пока планеты</div>
                                         <div class="alert alert-warning" role="alert">И начнём с Марса!</div>
                                         <div class="alert alert-danger" role="alert">Присоединяйся!
                                        </div>
                                      </body>
                                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

