from flask import Flask, request, jsonify
from tensorflow import keras
from flask_cors import CORS
from PIL import Image
import numpy as np


app = Flask(__name__)
CORS(app)

app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
# Carga el modelo previamente entrenado
modelo = keras.models.load_model('./modelo_entrenado1.h5')

# Define una ruta para realizar predicciones


@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    imagen = request.files['imagen']
    img = Image.open(imagen)
    img = img.resize((700, 700))
    img = img.convert('L')
    #normalizamos
    img = np.array(img) / 255.0
    # Aseguraramos que la imagen tenga la forma adecuada
    img = np.expand_dims(img, axis=-1)

    # Realizar la predicción con el modelo
    resultado = modelo.predict(np.array([img]))
    print(resultado)
    # Decodifica el resultado en una etiqueta legible
    etiqueta = np.argmax(resultado)

    print(etiqueta)

    # Crea una respuesta JSON con la etiqueta predicha
    respuesta = {'etiqueta': str( etiqueta )}

    print(respuesta)
    return str(etiqueta)

if __name__ == '__main__':
    app.run(debug=True)

