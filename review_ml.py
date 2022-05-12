import pandas as pd
import os.path
import csv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

save_path = r"C:\Users\atabe\GitRepos\cs48000-group7"

completeName = os.path.join(save_path, "sorted_comments.txt") 
completeNameCsv = os.path.join(save_path, "sorted_comments.csv") 



if __name__ == '__main__':

    with open(completeName, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(completeNameCsv, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

    # read_file = pd.read_csv(completeName)
    # read_file.to_csv(completeNameCsv, index=None)    

    df = pd.read_csv(completeNameCsv, names=['review', 'sentiment'], sep=',') 
    print(df.head())

    reviews = df['review'].values
    labels = df['sentiment'].values
    reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, labels, test_size=0.2, random_state=1000)

    vectorizer = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))
    #By default, the vectorizer might be created as follows:
    #vectorizer = CountVectorizer()
    vectorizer.fit(reviews_train)

    X_train = vectorizer.transform(reviews_train)
    X_test = vectorizer.transform(reviews_test)

    print(X_train)
    print(X_test)

    
    print("----------------DONE------------------------")