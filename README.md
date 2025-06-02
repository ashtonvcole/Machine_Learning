# Machine Learning

This repository contains assignments from COE 379L: Software Design for Responsive Intelligent Systems with Joe Stubbs ([Email](mailto:jstubbs@tacc.utexas.edu), [TACC](https://tacc.utexas.edu/about/staff-directory/joe-stubbs/), [GitHub](https://github.com/joestubbs)).

## What is this class?

Though the name is long, this was essentially an application-oriented machine learning course. We learned how to choose and develop machine learning models for realistic applications in the sciences. We were introduced to several common kinds of models, including linear regression, K-nearest neighbor, naive Bayes, random forest, artificial neural networks, convolutional neural networks, large language models etc. Crucially, we investigated what kinds of problems these tools are best-equipped to solve. Additional topics included verification and validation, data filtering and cleaning, interactive computing, and software development best practices.

## Contents

- Project 1, [Linear Regression](/Linear_Regression): Uses a high-dimensional linear regression model to study factors impacting fuel efficiency in cars.
- Project 2, [Breast Cancer](/Breast_Cancer): Compares K-Nearest Neghbor, Naive Bayes, and Random Forest models predicting breast cancer recurrence.
- Project 3, [Hurricane Damage](/Hurricane_Damage): Compares ANN and CNN models determining whether a property is flooded from satellite images.
- Final Project, [ANN Optimization](/ANN_Optimization): Conducts a hyperparameter sweep to attempt to optimize ANN's for a variety of sample problems.

## Setup and Execution

The `.ipynb` files can be run with Jupyter Notebook using a Python 3 kernel. Common machine learning libraries may need to be installed, too. Import statements are found in the first executable cell of each Jupyter Notebook file.

The snippets themselves can also be run as a simple Python script, but the output stream will need to be printed or written to files appropriately. Jupyter Notebook, however, provides a better workflow for developing models. Cells can be run, adjusted, and re-run independently, empowering the user, for example, to plot and analyze without re-training the model.