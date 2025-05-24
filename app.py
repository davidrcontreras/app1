import os
from flask import Flask#, request, jsonify
#el objeto request trae la petición del cliente hacía el servidor 

#### #ste ejemplo recibe en metodo GET por defecto a la ruta Raíz de la api y responde simplemente un saludo en el
#### Body de la web.

# creamos la web app object 
app = Flask(__name__) #le mando la variable __name__ (puede ser cualquier nombre) para que me devuelva el main de la
                      # web app 
# Usamos el decorator para generar una ruta de recurso o endpoint
@app.route('/') # esto es la raíz o sea esta representado por la url https://localhost:puerto/ ese ultimo /
#función que se envía al decorator: Es la función q se ejecuta cuando llega un request a esa URL
def home():
    return "Vamos Boquita carajo, un poquito maaa loquillo!"

#Levantamos el server app
#si nos devuelve correctamente la función main es porque la app esta ok, y podemos correrla, es decir levantar el webserver
if __name__ == '__main__':
    #app.run(host="0.0.0.0",port=5000,debug=True)
    app.run()