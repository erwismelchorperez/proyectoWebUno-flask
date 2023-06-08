from flask import Blueprint, render_template, request, redirect, url_for,g

from aplication.auth import login_required

from .models import Aplicacion, User
from aplication import db


bp = Blueprint('application', __name__, url_prefix='/application')

@bp.route('/list')
@login_required
def index():
    aplicaciones = Aplicacion.query.all()

    return render_template('application/index.html', aplicaciones = aplicaciones)

@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        aplicacion = Aplicacion(g.user.id, title, desc)
        db.session.add(aplicacion)
        db.session.commit()
        return redirect(url_for('application.index'))
    return render_template('application/create.html')

def get_aplication(id):
    aplicacion = Aplicacion.query.get_or_404(id)
    return aplicacion

@bp.route('/update/<int:id>', methods=('GET','POST'))
@login_required
def update(id):
    aplicacion = get_aplication(id)

    if request.method == 'POST':
        aplicacion.title = request.form['title']
        aplicacion.desc = request.form['desc']
        aplicacion.state = True if request.form.get('state') == 'on' else False
        db.session.commit()

        return redirect(url_for('application.index'))
    return render_template('application/update.html', aplicacion = aplicacion)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    aplicacion = get_aplication(id)
    db.session.delete(aplicacion)
    db.session.commit()
    return redirect(url_for('application.index'))
