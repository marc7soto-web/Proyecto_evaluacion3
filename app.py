from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza la página principal con botones a los ejercicios
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    promedio = None
    error = None

    if request.method == 'POST':
        try:
            # Captura y convierte los datos del formulario
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            # Validaciones de rango
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
            elif not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0 y 100."
            else:
                # Cálculo del promedio
                promedio = round((nota1 + nota2 + nota3) / 3, 1)
                resultado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
        except ValueError:
            error = "Todos los campos deben ser números válidos."

    return render_template('ejercicio1.html', resultado=resultado, promedio=promedio, error=error)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_largo = None
    cantidad = None
    error = None

    if request.method == 'POST':
        # Captura los nombres
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        # Validación de campos vacíos
        if not nombre1 or not nombre2 or not nombre3:
            error = "Todos los campos deben estar completos."
        else:
            nombres = [nombre1, nombre2, nombre3]
            nombre_largo = max(nombres, key=len)
            cantidad = len(nombre_largo)

    return render_template('ejercicio2.html', nombre_largo=nombre_largo, cantidad=cantidad, error=error)

if __name__ == '__main__':
    # Ejecuta la aplicación
    app.run(debug=True)
