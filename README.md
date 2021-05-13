# Spam Email Classification
Email is an essential mechanism to communicate people around the world for sharing useful financial and personal information within family, friends or even for official reasons. In occurrence of that, more possibility of undesirable illegitimate spam emails threads drops into user inbox as a junk mails and occupy additional storage space and lead to annoying task of email users to handle it. So it is fundamental need to classify the emails as harmful or useful. This project uses supervised learning approach to  classify the emails as spam or ham.

## Getting Started
Clone this project using below github url: https://github.com/hanumantmule/Email_Classification.git

### Prerequisites

Python packages you need to install. The list of libraries and its version is added in requirement.txt file. 

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Flask is a web application framework written in Python.
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

## Steps involved in implementation
1. Understanding dataset
2. Dataset preprocessing
3. Features extraction
4. Features reduction
5. Data distribution visualization
6. Divide the training and test set
7. Support Vector Machine Classifier
8. Naive Bayes Classifier

## Dataset

The dataset used for this project is **Enron-Spam dataset**. This dataset is collected from [here](http://www2.aueb.gr/users/ion/data/enron-spam/). We have just used **Enron1** folder. It contains two folders of spam and ham. Each folder contains emails. We have iterated to each text file of those folders and created a dataframe and written to a csv file.
Dataset can be found [here](https://github.com/hanumantmule/Email_Classification/blob/main/spam_ham_dataset.csv).
Enron1 dataset contain 3672 ham emails and 1499 spam emails.
**Dataset Classification**

![Dataset bar plot](https://github.com/hanumantmule/Email_Classification/blob/main/Screenshots/dataset%20classification%20bar%20plot.png?raw=true)


## How to use ?

We are planning to launch a web app which will provide classification service. User will type/paste the email content into the text box and check whether the email is spam or ham by simply clicking submit button.

**Steps to use.**
![Home Page](https://github.com/hanumantmule/Email_Classification/blob/main/Screenshots//web%20app/home_page.png?raw=true)

1. Launch the web application
3. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in the browser.
4. Type or paste the email content into the textbox.
5. Click the submit button. 
6. Visualize the email class as spam or ham.

## Classification Results

Till now We have assesed the model using two classifiers, Support vector machine and Naive Bayes algorithms.
Entire dataset contain 3672 ham emails and 1499 spam emails. 
The test set (which is distinct from the train and validation sets used to develop the model) was composed of 742 spam and 293 Ham emails.

**SVM Configuration :** kernel='linear'.

**Naive Bayes:** The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification).

Below tables shows the Classification report for SVM classifier and Naive bayes.

![SVM Result](https://github.com/hanumantmule/Email_Classification/blob/main/Screenshots/svm%20result.png?raw=true)

![Naive Bayes Result](https://github.com/hanumantmule/Email_Classification/blob/main/Screenshots/naive%20bayes%20result.png?raw=true)

## Future Scope
This model will be used as service for the email client like MS Outlook, Gmail or any personal email client, which scan the email before accepting it in the Mailbox. If the email is detected as spam then notify the user and qurantine the email. 


## References
[1] https://pip.pypa.io/en/stable/reference/pip_install/  
[2] http://www2.aueb.gr/users/ion/data/enron-spam/  
[3] https://towardsdatascience.com/higher-accuracy-and-less-process-time-in-text-classification-with-lda-and-tf-idf-d2d949e344c3

## Contributing

Please read [CONTRIBUTING.md](https://github.com/hanumantmule/Email_Classification/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Hanumant Mule** - [Github](https://github.com/hanumantmule/)
* **Namrata Kadam** - [Github](https://github.com/NamrataKadam/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

