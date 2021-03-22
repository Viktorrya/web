from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/list_prof/<param_list>')
def list_prof(param_list):
    prof = ["инженер-исследователь", "пилот", "врач"]
    return render_template
