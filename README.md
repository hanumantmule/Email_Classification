# Spam Email Classification
Email is an essential mechanism to communicate people around the world for sharing useful financial and personal information within family, friends or even for official reasons. In occurrence of that, more possibility of undesirable illegitimate spam emails threads drops into user inbox as a junk mails and occupy additional storage space and lead to annoying task of email users to handle it. So it is fundamental need to classify the emails as harmful or useful. This project uses supervised learning approach to  classify the emails as spam or ham.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python packages you need to install. The list of libraries and its version is added in requirement.txt file. 

* [NumPy](https://pypi.org/project/numpy/) - NumPy is an open-source numerical Python library.
* [pandas](https://pandas.pydata.org/) - Python Data Analysis Library.
* [matplotlib](https://matplotlib.org/) - Library for creating static, animated, and interactive visualizations.
* [seaborn](https://seaborn.pydata.org/) - Python data visualization library based on matplotlib.
* [nltk](https://www.nltk.org/) - Natural Language Toolkit 
* [sklearn](https://scikit-learn.org/) - Simple and efficient tools for predictive data analysis.
* [imblearn](https://pypi.org/project/imblearn/) - Imbalanced-learn is a python package offering a number of re-sampling techniques.

### Installing
Here we are using PIP which is a package manager for Python packages, or modules if you like. 
Note: If you have Python version 3.4 or later, PIP is included by default.
To install the all the dependencies for the project. Type below command in shell console. 
```
pip install -r requirements.txt
```
This will install all the libraries mentioned in the requirements.txt file.

## Dataset

The dataset used for this project is **Enron-Spam dataset**. This dataset is collected from [here](http://www2.aueb.gr/users/ion/data/enron-spam/). We have just used **Enron1** folder. It contains two folders of spam and ham. Each folder contains emails. We have iterated to each text file of those folders and created a dataframe and written to a csv file.
Dataset can be found [here](https://github.com/hanumantmule/Email_Classification/blob/main/spam_ham_dataset.csv)

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```


## Contributing

Please read [CONTRIBUTING.md](https://github.com/hanumantmule/Email_Classification/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Hanumant Mule** - [Github](https://github.com/hanumantmule/)
* **Namrata Kadam** - [Github](https://github.com/hanumantmule/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
