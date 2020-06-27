from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, f1_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC


def accuracy(comments, label):

    X_train, X_test, y_train, y_test = train_test_split(comments, label, test_size=0.2, random_state= 42)

    # vector = TfidfVectorizer().fit(X_train.values.astype('U'))
    # X_train_vector = vector.transform(X_train.values.astype('U')).toarray()
    # X_test_vector = vector.transform(X_test.values.astype('U')).toarray()

    vector = TfidfVectorizer().fit(X_train)
    X_train_vector = vector.transform(X_train).toarray()
    X_test_vector = vector.transform(X_test).toarray()

    cart = DecisionTreeClassifier()
    gnb = BernoulliNB()
    knn = KNeighborsClassifier(n_neighbors=5)
    svm = SVC(kernel='linear')

    cart.fit(X_train_vector, y_train)
    gnb.fit(X_train_vector, y_train)
    knn.fit(X_train_vector, y_train)
    svm.fit(X_train_vector, y_train)

    cartPredict = cart.predict(X_test_vector)
    gnbPredict = gnb.predict(X_test_vector)
    knnPredict = knn.predict(X_test_vector)
    svmPredict = svm.predict(X_test_vector)

    finalDecisionTree = []
    matrixDecisionTree = []
    print('tree')
    finalDecisionTree.append(precision_score(y_test, cartPredict, average='weighted'))
    finalDecisionTree.append(recall_score(y_test, cartPredict, average='weighted'))
    finalDecisionTree.append(f1_score(y_test, cartPredict, average='weighted'))
    finalDecisionTree.append(accuracy_score(y_test, cartPredict))
    print(confusion_matrix(y_test, cartPredict))
    print(classification_report(y_test, cartPredict))

    matrixDecisionTree.append(confusion_matrix(y_test, cartPredict)[0][0])
    matrixDecisionTree.append(confusion_matrix(y_test, cartPredict)[0][1])
    matrixDecisionTree.append(confusion_matrix(y_test, cartPredict)[1][0])
    matrixDecisionTree.append(confusion_matrix(y_test, cartPredict)[1][1])
    matrixDecisionTree.append(round((classification_report(y_test, cartPredict, output_dict=True)['Negative']['precision']), 2))
    matrixDecisionTree.append(round((classification_report(y_test, cartPredict, output_dict=True)['Negative']['recall']), 2))
    matrixDecisionTree.append(round((classification_report(y_test, cartPredict, output_dict=True)['Negative']['f1-score']), 2))
    matrixDecisionTree.append(round((classification_report(y_test, cartPredict, output_dict=True)['Positive']['precision']), 2))
    matrixDecisionTree.append(round((classification_report(y_test, cartPredict, output_dict=True)['Positive']['recall']), 2))
    matrixDecisionTree.append(round((classification_report(y_test, cartPredict, output_dict=True)['Positive']['f1-score']), 2))

    finalNaiveBayes = []
    matrixNaiveBayes = []
    print('nb')
    finalNaiveBayes.append(precision_score(y_test, gnbPredict, average='weighted'))
    finalNaiveBayes.append(recall_score(y_test, gnbPredict, average='weighted'))
    finalNaiveBayes.append(f1_score(y_test, gnbPredict, average='weighted'))
    finalNaiveBayes.append(accuracy_score(y_test, gnbPredict))
    print(confusion_matrix(y_test, gnbPredict))
    print(classification_report(y_test, gnbPredict))

    matrixNaiveBayes.append(confusion_matrix(y_test, gnbPredict)[0][0])
    matrixNaiveBayes.append(confusion_matrix(y_test, gnbPredict)[0][1])
    matrixNaiveBayes.append(confusion_matrix(y_test, gnbPredict)[1][0])
    matrixNaiveBayes.append(confusion_matrix(y_test, gnbPredict)[1][1])
    matrixNaiveBayes.append(round((classification_report(y_test, gnbPredict, output_dict=True)['Negative']['precision']), 2))
    matrixNaiveBayes.append(round((classification_report(y_test, gnbPredict, output_dict=True)['Negative']['recall']), 2))
    matrixNaiveBayes.append(round((classification_report(y_test, gnbPredict, output_dict=True)['Negative']['f1-score']), 2))
    matrixNaiveBayes.append(round((classification_report(y_test, gnbPredict, output_dict=True)['Positive']['precision']), 2))
    matrixNaiveBayes.append(round((classification_report(y_test, gnbPredict, output_dict=True)['Positive']['recall']), 2))
    matrixNaiveBayes.append(round((classification_report(y_test, gnbPredict, output_dict=True)['Positive']['f1-score']), 2))

    finalKNN = []
    matrixKNN = []
    print('knn')
    finalKNN.append(precision_score(y_test, knnPredict, average='weighted'))
    finalKNN.append(recall_score(y_test, knnPredict, average='weighted'))
    finalKNN.append(f1_score(y_test, knnPredict, average='weighted'))
    finalKNN.append(accuracy_score(y_test, knnPredict))
    print(confusion_matrix(y_test, knnPredict))
    print(classification_report(y_test, knnPredict))

    matrixKNN.append(confusion_matrix(y_test, knnPredict)[0][0])
    matrixKNN.append(confusion_matrix(y_test, knnPredict)[0][1])
    matrixKNN.append(confusion_matrix(y_test, knnPredict)[1][0])
    matrixKNN.append(confusion_matrix(y_test, knnPredict)[1][1])
    matrixKNN.append(round((classification_report(y_test, knnPredict, output_dict=True)['Negative']['precision']), 2))
    matrixKNN.append(round((classification_report(y_test, knnPredict, output_dict=True)['Negative']['recall']), 2))
    matrixKNN.append(round((classification_report(y_test, knnPredict, output_dict=True)['Negative']['f1-score']), 2))
    matrixKNN.append(round((classification_report(y_test, knnPredict, output_dict=True)['Positive']['precision']), 2))
    matrixKNN.append(round((classification_report(y_test, knnPredict, output_dict=True)['Positive']['recall']), 2))
    matrixKNN.append(round((classification_report(y_test, knnPredict, output_dict=True)['Positive']['f1-score']), 2))

    finalSVM = []
    matrixSVM = []
    print('svm')
    finalSVM.append(precision_score(y_test, svmPredict, average='weighted'))
    finalSVM.append(recall_score(y_test, svmPredict, average='weighted'))
    finalSVM.append(f1_score(y_test, svmPredict, average='weighted'))
    finalSVM.append(accuracy_score(y_test, svmPredict))
    print(confusion_matrix(y_test, svmPredict))
    print(classification_report(y_test, svmPredict))

    matrixSVM.append(confusion_matrix(y_test, svmPredict)[0][0])
    matrixSVM.append(confusion_matrix(y_test, svmPredict)[0][1])
    matrixSVM.append(confusion_matrix(y_test, svmPredict)[1][0])
    matrixSVM.append(confusion_matrix(y_test, svmPredict)[1][1])
    matrixSVM.append(round((classification_report(y_test, svmPredict, output_dict=True)['Negative']['precision']), 2))
    matrixSVM.append(round((classification_report(y_test, svmPredict, output_dict=True)['Negative']['recall']), 2))
    matrixSVM.append(round((classification_report(y_test, svmPredict, output_dict=True)['Negative']['f1-score']), 2))
    matrixSVM.append(round((classification_report(y_test, svmPredict, output_dict=True)['Positive']['precision']), 2))
    matrixSVM.append(round((classification_report(y_test, svmPredict, output_dict=True)['Positive']['recall']), 2))
    matrixSVM.append(round((classification_report(y_test, svmPredict, output_dict=True)['Positive']['f1-score']), 2))

    return finalDecisionTree, finalNaiveBayes, finalKNN, finalSVM, matrixDecisionTree, matrixNaiveBayes, matrixKNN, matrixSVM

# import pandas as pd
# df = pd.read_csv(r'C:\Users\Aufar\Documents\edm\testLabeled.csv')
#
# accuracy(df['Translated'], df['Label'])


