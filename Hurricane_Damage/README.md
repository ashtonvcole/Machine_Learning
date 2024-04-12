# Hurricane Damage

In this project, we build and test various neural networks to predict property damage from a satellite image. The best-performing network is then saved to disk and developed into a containerized Flask *inference server*.

## Contents

- `api.py`: Python code defining the endpoints of the Flask inference server.
- `data/`: A folder used to hold training data.
	- `data_all_modified.zip`: An archive of the image dataset, i.e. 128x128 JPEG images divided into `damage` and `no_damage` folders.
- `dense-ann.ipynb`: A notebook building a densely connected Artificial Neural Network.
- `Dockerfile`: A file with intructions to build a Docker image of the inference server from this directory.
- `docker-compose.yml`: A file with instructions to build or pull the Docker image and then start a container running the inference server.
- `docker-compose-arm64.yml`: An alternate `docker-compose` file for Mac ARM chip architecture, to resolve platform errors.
- `lenet-5-cnn.ipynb`: A notebook building a LENET-5 Convolutional Neural Network.
- `lenet-5-cnn-alternate.ipynb`: A notebook building an alternate LENET-5 Convolutional Neural Network described in [this paper](https://arxiv.org/pdf/1807.01688.pdf).
- `lenet-5-modified.keras`: A file holding the trained alternate LENET-5 network.
- `preprocessing.ipynb`: A notebook splitting the unzipped `data_all_modified` images into training and testing folders.

## Setup and Execution

### Jupyter Notebook Files

The `.ipynb` files can be run with Jupyter Notebook using a Python 3 kernel. The snippets themselves can also be run as a simple Python script, but the output stream will need to be printed or written to files appropriately.

The archive `data_all_modified.zip` in the `data/` folder will need to be unzipped to a `data_all_modified` folder in the same location for the notebooks to run as expected.

### Inference Server

Ordinary Docker commands may be used to build a Docker image and deploy a container. A `docker-compose.yml` file has also been provided to speed up the process. The image and container may be built at once using the command `docker-compose up`. The command `docker-compose down` stops the container.

The server may be tested using a client-side Python script like the following.

```Python
import requests

url = 'http://127.0.0.1/models/hurricane-damage/v1'
file = open('image.jpeg', 'rb')
files = {'image': file.read()}

response = requests.post(url, files=files)
print(response.json())
```

#### Server Documentation

- `models/hurricane-damage/v1`
	- `GET`: Returns basic metadata about the inference server.
	- `POST`: Classifies a satellite image of property as having been damaged or having not been damaged by a hurricane. This route requires a byte stream of a 128x128 JPEG image, wrapped in a dictionary under the key `"image"`. It returns a JSON dictionary in the following form.

```JSON
{
	"result": [probability_damage, probability_no_damage]
}
```

#### Special Notes for Mac ARM Users

Unfortunately, as of April 2024, Macs cause a couple of issues for users. However, the container will deploy normally on other platrorms.

First, the x86 Linux-based container must be rebuilt to be compatible with ARM architecture. An additional link in `docker-compose-arm64.yml` specifically requires this. To use this file with `docker-compose`, the following command may be used.

```docker-compose -f docker-compose-arm64.yml up```

Port 5000 may be already busy, because newer Macs use port 5000 for Airplay Receiver. Going to `System Settings > General > AirDrop and Handoff` and turning off AirPlay Receiver should resolve this issue.

At the moment, while installing TensorFlow into the container, an error occurs while installing h5py.
