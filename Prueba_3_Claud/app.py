from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        aprobado = promedio >= 40 and asistencia >= 75

        estado = "APROBADO" if aprobado else "REPROBADO"

        return render_template('ejercicio1.html', promedio=f'{promedio:.2f}', asistencia=asistencia, estado=estado)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template('ejercicio2.html', nombre_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)

if __name__ == '__main__':
    app.run(debug=True)