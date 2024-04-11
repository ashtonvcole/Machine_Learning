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

### Building Docker Container

### Running and Testing Inference Server
