from flask import Flask,render_template

app = Flask(__name__)

@app.route('/ola')
def hello():
    retorno = ''
    for i in range(10):
        retorno += f'<P> contando - {i} </P>'

    return render_template('hello.html', dados=retorno)

app.run()
