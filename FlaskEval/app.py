from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/FormPromedio', methods=['GET', 'POST'])
def formPromedio():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asist1 = int(request.form['asist1'])
        if asist1 < 0 or asist1 > 100:
            error = 'ERROR: Asistencia debe ser mayor o igual que 0 y menor o igual a 100'
            return render_template('FormPromedio.html', error=error, nota1=nota1, nota2=nota2, nota3=nota3, asist1=asist1)
        if nota1 >= 10 and nota1 <= 70:
            if nota2 >= 10 and nota2 <= 70:
                if nota3 >= 10 and nota3 <= 70:
                    resultado = (nota1 + nota2 + nota3)/3
                    if asist1 >= 75 and resultado >= 40:
                        estado = 'Aprobado'
                        return render_template('FormPromedio.html', resultado=resultado, estado=estado, nota1=nota1, nota2=nota2, nota3=nota3, asist1=asist1)
                    else:
                        estado = 'Reprobado'
                        return render_template('FormPromedio.html', resultado=resultado, estado=estado, nota1=nota1, nota2=nota2, nota3=nota3, asist1=asist1)
                else:
                    error = 'ERROR: Las notas deben se mayores o iguales a 10 y menores o iguales a 70'
                    return render_template('FormPromedio.html', error=error, nota1=nota1, nota2=nota2, nota3=nota3, asist1=asist1)
            else:
                error = 'ERROR: Las notas deben se mayores o iguales a 10 y menores o iguales a 70'
                return render_template('FormPromedio.html', error=error, nota1=nota1, nota2=nota2, nota3=nota3, asist1=asist1)
        else:
            error = 'ERROR: Las notas deben se mayores o iguales a 10 y menores o iguales a 70'
            return render_template('FormPromedio.html', error=error, nota1=nota1, nota2=nota2, nota3=nota3, asist1=asist1)
    return render_template('FormPromedio.html')

@app.route('/FormCaracteres', methods=['GET', 'POST'])
def fromCaracteres():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        n1 = len(nombre1)
        n2 = len(nombre2)
        n3 = len(nombre3)
        if n1 > n2:
            if n1 > n3:
                resultado = nombre1
                return render_template('FormCaracteres.html', resultado=resultado, cant=n1, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)
            else:
                resultado = nombre3
                return render_template('FormCaracteres.html', resultado=resultado, cant=n3, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)
        elif nombre2 > nombre3:
            resultado = nombre2
            return render_template('FormCaracteres.html', resultado=resultado, cant=n2, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)
        else:
            resultado = nombre3
            return render_template('FormCaracteres.html', resultado=resultado, cant=n3, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)
    return render_template('FormCaracteres.html')

if __name__ == '__main__':
    app.run()
