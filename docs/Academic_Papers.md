# Academic Papers #

## Machine learning models and bankruptcy prediction ##

* Date: 15th October 2017
* Authors: Flavio Barboza, Herbert Kimura, Edward Altman
* KeyWords: Bankruptcy prediction, Machine learning, Support vector machines, Boosting, Bagging, Random forest
* https://www.sciencedirect.com/science/article/pii/S0957417417302415

This paper looks into machine learning models to show improved bankruptcy prediction accuracy over traditional models to predict bankruptcy one year prior to the event. Various models were tested using different accuracy metrics.

The machine learning models explained in section 2 are:

### Bagging (2.2) ### 
Bagging, also known as ‘bootstrap aggregating’, is a technique involving independent classifiers that uses portions of the data and then combines them through model averaging, providing the most efficient results concerning a collection.

### Boosting(2.3) ###
The boosting technique consists of the repeated use of a base prediction rule or function on different sets of the initial set. Boosting builds on other classification schemes and assigns a weight to each training set, which is then incorporated into the model. The data are then reweighted.

### Random Forrest (2.4) ###
The random forest technique (RF) is based on decision tree models, also known as generalised classification and regression trees’ (CART). The model has a level of precision similar to that of AdaBoost and, depending on the set, can provide better results than boosting can. It is particularly robust and allows for the presence of outliers and noise in the training set.

Compustat was used to collect financial data on American and Canadian companies covering 1985 to 2013. Information on firm insolvency was collected form NYU’s Salomon Center database. A subset from 1985 to 2005 was extracted to provide the training set.

The Altman Z-score is a formula for predicting bankruptcy, made in 1968 and a seminal paper on organisational performance by Carton and Hofer (2006) was used to choose predictive variables for the program.

The variables can be found under 3. Data and Method.

Examples of some variables are:
* X1 = net working capital / total assets
* X2 = retained earnings/total assets

Eight techniques were applied to the datasets:
• Bagging,
• Boosting,
• Random forest (RF),
• SVM with two kernels: linear (SVM-Lin) and radial basis function(SVM-RBF),
• Artificial neural networks (ANN),
• Logistic regression (Logit), and
• MDA. 

//table

Through the various tests ran they found that giving the program 5 years’ worth training data may not be relevant to current events. But mainly found that the three machine learning techniques: boosting, bagging and Random Forrest showed the best outcomes in all the tests with Random Forrest usually performing the best.


