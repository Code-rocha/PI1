from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

@bp.route("/")
def homepage():
    return render_template("homepage.html")

@bp.route("/vacinas_disponiveis")
def vdisponiveis():
    return render_template("vdisponiveis.html")

@bp.route("/quem_pode_se_vacinar")
def qpsvacinar():
    return render_template("quem_pode_se_vacinar.html")

@bp.route("/calendario")
def calendario():
    return render_template("calendario.html")

@bp.route("/locais")
def locais():
    return render_template("locais.html")
