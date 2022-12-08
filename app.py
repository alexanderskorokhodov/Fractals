import json
import os
from PIL import Image
from flask import Flask, render_template, request, url_for, flash, redirect, make_response
from werkzeug.exceptions import abort
from fractal import julia

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
STATIC_DIR = "static"


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'submit_button' in request.form:
        center_cx = float(request.form.get('center_cx'))
        center_cy = float(request.form.get('center_cy'))
        # diameter_x = request.form.get('diameter_x')
        max_iter = int(request.form.get('max_iter'))
        # max_betrag_quadrat = request.form.get('max_betrag_quadrat')
        iter_func = request.form.get('iter_func')
        # julia_r = request.form.get('julia_r')
        # julia_i = request.form.get('julia_i')
        id_ = julia(cX=center_cx, cY=center_cy, maxIter=max_iter)
        print('fdfsf')
        return redirect(f'fractal/{id_}')

    fractals = list(map(lambda x: (x[:-5], 'fractals/' + x), os.listdir('static/fractals')))
    return render_template('index.html', static_folder=STATIC_DIR, fractals=fractals)


def on_import():
    pass


def on_export():
    pass


@app.route('/fractal/<id_>')
def fractal(id_):
    if f'{id_}.jpeg' not in os.listdir('static/fractals'):
        return redirect('/')


    return render_template(template_name_or_list='fractal.html', static_folder=STATIC_DIR, img=f"/fractals/{id_}.jpeg")


if __name__ == '__main__':
    app.run()
