from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Página Inicial</h1><p>Bem vindo!!!!!<br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla.<br> <br> <a href="/sobre">Sobre nós <br><a href="/contatos">Contatos<br> <a href="/experiencia">Experiencia <br> <a href="/formação">Formação<br> </p>'

@app.route('/sobre')
def sobre():
    return '<h1>Sobre</h1><p>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla.<br>.</p>'

@app.route('/experiencia')
def experiencia():
    return '<h1>Experiencia</h1><p>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla.<br>.</p>'

@app.route('/formação')
def formação():
    return '<h1>Formação</h1><p>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla <br>bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla.<br>.</p>'

@app.route('/contatos')
def contatos():
    return '<h1>Contatos</h1><p>Nosso telefone: 4002-8922.'



if __name__ == "__main__":
    app.run(debug=True)


