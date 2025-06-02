# ANN Optimization

In my final project, I conducted hyperparameter sweeps with Keras to optimize the number of perceptrons and layers in an Artificial Neural Network (ANN), applied to several different data sets for comparison. I was curious whether I could find any sort of optimal architecture for an ANN.

The results were not so satisfying. Part of the problem is that I used image classification problems as test cases. An ANN works fine on simple black-and-white numbers in the MNIST data set, but not so well on visually-complicated color pictures. Really, a Convolutional Neural Network (CNN) is more useful for images because it better accounts for relative spatial relationships.

Even if I found better application problems, I would need to find a better approach than a hyperparameter sweep, too. Adding more layers to the neural network exponentially increases the number of perceptron combinations. A stronger theoretical foundation would probably be useful. Nevertheless, it was fun to try, and not doing things perfectly is how one learns.

## Contents

- [`ann-beans.ipynb`](ann-beans.ipynb): Hyperparameter sweep on the beans dataset.
- [`ann-hurricane.ipynb`](ann-beans.ipynb): Hyperparameter sweep on the hurricane dataset.
- [`ann-mnist.ipynb`](ann-beans.ipynb): Hyperparameter sweep on the MNIST dataset.
- [`data/`](data)
	- [`data_all_modified.zip`](data/data_all_modified.zip): An archive of all image datasets used in the project.
- [`proposal/`](proposal)
	- [`proposal.pdf`](proposal/proposal.pdf): Initial proposal pitching the question and methods of the project.
	- [`proposal.tex`](proposal/proposal.tex)
- [`report/`](report)
	- [`report.pdf`](report/report.pdf): Detailled report summarizing methodology and findings.
	- [`report.tex`](report/report.tex)
- [`preprocessing.ipynb`](preprocessing.ipynb): This file organizes the datasets into random training and testing sets, separated into new directories. It must be run on an unzipped copy of the data sets for the other notebooks to run successfully.

## Setup and Execution

The `.ipynb` files can be run with Jupyter Notebook using a Python 3 kernel. The snippets themselves can also be run as a simple Python script, but the output stream will need to be printed or written to files appropriately.

The data files must be unzipped with an archive utility. `preprocessing.ipynb` should be run first. Then, each of the case notebooks can be run to solve a particular dataset.