from flask import Flask, request, jsonify
#el objeto request trae la petición del cliente hacía el servidor 

# creamos la app object 
app = Flask(__name__) #le mando la variable __name__ (puede ser cualquier nombre) para que me devuelva el main de la
                      # web app 

@app.route('/saludo/<name>') # este caso voy a recibir parametros en el request 
# https://localhost:puerto/saludo?name=value&surname=value
def saludo(name):  
    return f"hola {name}"

#si nos devuelve correctamente la función main es porque la app esta ok, y podemos correrla, es decir levantar el webserver
if __name__ == '__main__':
    app.run(debug=True)

