import pandas as pd
import os.path
import csv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def predictData(comment_list):
    save_path = r"C:\Users\karah\Desktop\cs48000-group7"

    completeName = os.path.join(save_path, "sorted_comments.txt") 
    completeNameCsv = os.path.join(save_path, "sorted_comments.csv") 

    with open(completeName, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(completeNameCsv, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)  

    df = pd.read_csv(completeNameCsv, names=['review', 'sentiment'], sep=',') 
    print(df.head())

    reviews = df['review'].values
    labels = df['sentiment'].values
    reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, labels, test_size=0.2, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(reviews_train)

    X_train = vectorizer.transform(reviews_train)
    X_test = vectorizer.transform(reviews_test)

    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    accuracy = classifier.score(X_test, y_test)
    print("Accuracy:", accuracy)

    
    X_new = vectorizer.transform(comment_list)
    return classifier.predict(X_new)



if __name__ == '__main__':

    new_reviews = ['Old version of python useless', 'Very good effort, but not five stars', 'Clear and concise']
    print(predictData(new_reviews))

    print("----------------DONE------------------------")