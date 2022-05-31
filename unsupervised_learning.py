import pandas as pd
import os.path
import csv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def getList(file_name, save_path, completeName):

    comments = []



    with open(completeName, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        for line in lines:
            comments.append(line[0])

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

    reviews = df['review'].values
    labels = df['sentiment'].values
    reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, labels, test_size=0.0000001, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(reviews_train)

    X_train = vectorizer.transform(reviews_train)
    X_test = vectorizer.transform(reviews_test)

    classifier = LogisticRegression(max_iter=10000)
    classifier.fit(X_train, y_train)

    accuracy = classifier.score(X_test, y_test)
    print("Accuracy:", accuracy)

    
    X_new = vectorizer.transform(comment_list)
    
    predictions = classifier.predict(X_new)

    print(predictions)
    return predictions
        
def predictAdd(file_name):

    save_path = r"C:\Users\karah\Desktop\cs48000-group7"

    completeName = os.path.join(save_path, "all_sorted_comments.txt") 

    new_reviews = getList(file_name, save_path, completeName)

    predictions = predictNewData(new_reviews,save_path, completeName)

    for i in range(len(new_reviews)):
            f1 = open(completeName, "a", encoding="utf-8")
            f1.write(new_reviews[i] + "," +str(predictions[i]) +"\n")
            f1.close()




if __name__ == '__main__':

    predictAdd("#Cats in Time Relaxing Puzzle.txt")
   


    print("----------------DONE------------------------")