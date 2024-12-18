from flask import Flask, render_template

# Crea la app de Flask
app = Flask(__name__)

# Ruta principal de la página
@app.route('/')
def home():
    return render_template('index.html')

# Ejecuta la app
if __name__ == '__main__':
    app.run(debug=True)