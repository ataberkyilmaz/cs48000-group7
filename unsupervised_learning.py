from unittest import skip
import pandas as pd
import os.path
import csv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def getList(file_name, save_path):

    completeName = os.path.join(save_path, file_name) 
    comments = []



    with open(completeName, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        # lines = (line.split(":") for line in stripped if line)
        for line in stripped:
            line = line.replace(",", " ")
            line = line.replace("\n", "")
            thisLine = line.split(" : ")
            if len(thisLine) == 2:
                comments.append(thisLine[1])

    return comments




def predictNewData(comment_list, save_path, completeName):
    
    completeNameCsv = os.path.join(save_path, "all_sorted_comments.csv") 

    with open(completeName, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(completeNameCsv, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)  

    df = pd.read_csv(completeNameCsv, names=['review', 'sentiment'], sep=',') 
    print('Data Dimensionality: ' , df.shape)
    print('Data Summary: ' , df.info)

    reviews = df['review'].values.astype('U')
    labels = df['sentiment'].values.astype('U')
    reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, labels, test_size=0.0000001, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(reviews_train)

    X_train = vectorizer.transform(reviews_train)
    X_test = vectorizer.transform(reviews_test)

    classifier = LogisticRegression(max_iter=1000000)
    classifier.fit(X_train, y_train)

    accuracy = classifier.score(X_test, y_test)
    print("Accuracy:", accuracy)

    
    X_new = vectorizer.transform(comment_list)
    
    predictions = classifier.predict(X_new)

    print(len(predictions))
    return predictions
        
def predictAdd(file_name):

    save_path = r"C:\Users\atabe\GitRepos\cs48000-group7"

    completeName = os.path.join(save_path, "all_sorted_comments.txt") 

    new_reviews = getList(file_name, save_path)

    print("predictions:" , len(new_reviews))

    predictions = predictNewData(new_reviews,save_path, completeName)

    for i in range(len(new_reviews)):
            f1 = open(completeName, "a", encoding="utf-8")
            f1.write(new_reviews[i] + "," +str(predictions[i]) +"\n")
            f1.close()




if __name__ == '__main__':

    predictAdd("Unholy Adventure Mystery.txt")
   


    print("----------------DONE------------------------")
