from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener datos por el atributo 'name' del input en el HTML
        usuario = request.form.get('username')
        password = request.form.get('password')
        return f"Usuario: {usuario} logueado."
    
    return '''<form method="post">
                <input type="text" name="username">
                <input type="password" name="password">
                <input type="submit" value="Enviar">
              </form>'''
