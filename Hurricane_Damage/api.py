from flask import Flask, request
import PIL.Image
import tensorflow as tf
from tensorflow.keras.layers.experimental.preprocessing import Rescaling

app = Flask(__name__)

model = tf.keras.models.load_model('lenet-5-modified.keras')
rescale = Rescaling(scale=1.0/255)
fname = 'temp.jpeg'



#######################
# ANCILLARY FUNCTIONS #
#######################



def preprocess_input(image):
    # Temporarily save image so that TensorFlow may read it
    # If not only request being processed, potential race condition
    image.save(fname)
    image = tf.io.read_file(fname)
    image = tf.io.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [128, 128])
    image = rescale(image)
    image = tf.reshape(image, [1,] + image.shape.as_list())
    return image



##############
# API ROUTES #
##############



@app.route('/models/hurricane-damage/v1', methods=['GET'])
def model_info():
    return {
        'version': 'v1',
        'name': 'hurricane-damage',
        'description': 'Classify satellite images of properties to determine if they are damaged',
        'number_of_parameters': 2601666
    }



@app.route('/models/hurricane-damage/v1', methods=['POST'])
def classify_hurricane_damage_image():
    image = request.files.get('image')
    result = None
    if not image:
        return {'error': 'An image must be posted'}, 400
    try:
        image = preprocess_input(image)
    except Exception as e:
        return {'error': f'Could not process image: {e}'}, 400
    try:
        result = model.predict(image).tolist()
    except Exception as e:
        return {'error': f'Could not predict: {e}'}, 400
    return {'result': result}, 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')