from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/opcaoc')
def opcaoc():
    return render_template("opcaoc.html")

@app.route('/cadastroempresa')
def cadastroempresa():
    return render_template("cadastroempresa.html")

@app.route('/telainicial')
def telainicial():
    return render_template("telainicial.html")

@app.route('/recuperar-senha')
def recuperarsenha():
    return render_template("recuperar-senha.html")

if __name__ == "__main__":
    app.run(debug=True)
