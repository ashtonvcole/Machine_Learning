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
- `lenet-5-cnn-alternate.ipynb`: A notebook building an alternate LENET-5 Convolutional Neural Network described in [this paper](https://arxiv.org/pdf/1807.01688.pdf).
- `lenet-5-cnn.ipynb`: A notebook building a LENET-5 Convolutional Neural Network.
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

url = `http://127.0.0.1/models/hurricane-damage/v1`
file = open('image.jpeg', 'rb')
files = {'image': file.read()}

response = requests.post(url, files=files)
print(response.json)
```

#### Server Documentation

#### Special Notes for Mac Users

Unfortunately, as of April 2024, Macs cause a couple of issues for users.

First, the Linux-based container may have issues running on ARM architecture. An additional linke in `docker-compose-arm64.yml` specifically sets a version of Linux that may run on ARM architecture. To specifically use this file, the following command may be used.

```docker-compose -f docker-compose-arm64.yml up```

Port 5000 may be already busy, because newer Macs use port 5000 for Airplay Receiver. Going to `System Settings > General > AirDrop and Handoff` and turning off AitPlay Receiver should resolve this issue.

At the moment, while installing TensorFlow into the container, an error occurs while installing h5py. However, the container will deploy on other platrorms.
