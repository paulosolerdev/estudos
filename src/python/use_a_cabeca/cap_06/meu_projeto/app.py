from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search.html", the_title="Pesquisar Letras")

@app.route("/search", methods=["POST"])
def search():
    phrase = request.form.get("phrase")
    letters = request.form.get("letters")

    # aqui só pra testar, vamos mostrar de volta os dados
    resultado = f"Você digitou a frase: '{phrase}' e as letras: '{letters}'"
    return render_template("results.html", the_title="Resultado", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
