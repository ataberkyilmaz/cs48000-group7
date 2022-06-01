import pandas as pd
import os.path
import csv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def predictData(comment_list):
    save_path = r"C:\Users\atabe\GitRepos\cs48000-group7"

    completeName = os.path.join(save_path, "sorted_comments.txt") 
    completeNameCsv = os.path.join(save_path, "sorted_comments.csv") 

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
    reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, labels, test_size=0.2, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(reviews_train)

    X_train = vectorizer.transform(reviews_train)
    X_test = vectorizer.transform(reviews_test)

    classifier = LogisticRegression(max_iter=10000)
    classifier.fit(X_train, y_train)

    accuracy = classifier.score(X_test, y_test)
    print("Accuracy:", accuracy)

    
    X_new = vectorizer.transform(comment_list)
    
    return classifier.predict(X_new)



if __name__ == '__main__':

    """ 
    i love the way this game challenges my brain to solve it but one issue is that it's impossible to scan the tiny qr codes when i make my own levelsso i can send them to my friend for testing othe than that its amazing,1
    one of the best brain teasers  the background music changes with patter of your click. thanks to the developer.. for not adding ads to it.,1
    maze solving with verticality. a very entertaining and engaging game with apt sounds. a very good blend of the concepts. this is the game that i usually recommend to my friends. kudos to the developer.,1
    martin. you've done a great job with this game. the fact that you let us play it for free and then left it to us to determine it's value is incredible. i have never seen any developer do this and it's nothing short of brilliant. you obviously worked hard on this game and judging from the love it's gotten it paid off! congratulations! looking forward to your future projects.,1
    the game isn't puzzling  it's fustrating. why would u make the character move involuntarily towards tazers and bots. it's borderline annoying. also stop asking for money so frequently. did u want the game to be free for everyone to play or did u think it wasn't worth paying for? just label a price on the app store or add a place to donate for it.,0
    really having fun with this. great art style. fun  challenging puzzles. but lowkey and casual. i love it!,1
    loved this game alot  completed a couple of times but still never got bored. eagerly waiting for next version...yeah i know we can download different levels from browser but still just waiting for more. do try this game guys you'll love it for sure.,1
    the game's amazing....i have tried many games over time...and its one of the very good games' category that i would put this game in. it's not very addictive so won't kill ur precious time and it's fun...so overall....good games for everyone looking for a rest time game,1
    i love it. its tricks the mind  but the music and beautiful simple graphic dilutes the pressure and make it such a soothing and refreshing game.,1
    this game was good  it also has options for designing your own level  but you have to purchase the hints. that's the only drawback. overall a very cute game.,1
    i could have given 5 star but some issues is found by me. we can't upload our levels in forums. after completing 3 levels it will show black screen and we again have to play that same level. these are only my issues please say me that how to upload our levels in forums. thank you!,1
    this game us really nice... has a good graphics very simple concept i love the levels... it is easy at first and becomes tough at last... we can even create our own levels... it is a very simple but an intresting... funny... good timepase game... try this game it is really a cool game...,1
    very nice  free and engaging puzzle game after a very long time. 50 levels only but very worth it. knocked it off in 1 day.... worth it,1
    the robot is too  dang cute! wish i can hug it! the puzzles are challenging  but fun! and the sick update! nice one!,1
    this game is 5*****. it keep me going and going. the programmer has done a fantastic job in creating the many many different fun and challenging level. well done.,1
    i actually don't like the zapper. the should be no size limitation in creating a level. i also don't like the red bot that you have push or help you out in level 19 and the red bot with a zapper head to get away with.,0
    the robot keeps falling because of the smallest pushes from the movable parts of the puzzles. gets kinda annoying when you're so close to finish and the little idiot can't even stand by itself.,0
    almost fun. the reliance on weird motions makes it unruly to play on a phone touch screen. too much tricky maneuvering not enough puzzle.,0
    too much ads.. ads actively interupts gameplay  pauses game to show ads. ads in between levels are fine. but pausing an active level just to show ads is not acceptable.,0
    to be honest this game is really bland  the physics are wonky and the levels are super easy  it's practically pay to win since you can't use hints since the game just expects you to know everything about the mechanics of the game  really sloppy  i don't reccomend.,0


    good game on this trashy app store,1
    nice and very entertaining game...,1
    good game. give it a try and see for your self.,1
    fix da game wen ay enter it is black all,0
        
    
    
    """



    new_reviews = ["i love the way this game challenges my brain to solve it but one issue is that it's impossible to scan the tiny qr codes when i make my own levelsso i can send them to my friend for testing othe than that its amazing",
     'one of the best brain teasers  the background music changes with patter of your click. thanks to the developer.. for not adding ads to it.',
      'maze solving with verticality. a very entertaining and engaging game with apt sounds. a very good blend of the concepts. this is the game that i usually recommend to my friends. kudos to the developer.',
      "martin. you've done a great job with this game. the fact that you let us play it for free and then left it to us to determine it's value is incredible. i have never seen any developer do this and it's nothing short of brilliant. you obviously worked hard on this game and judging from the love it's gotten it paid off! congratulations! looking forward to your future projects.",
      "the game isn't puzzling  it's fustrating. why would u make the character move involuntarily towards tazers and bots. it's borderline annoying. also stop asking for money so frequently. did u want the game to be free for everyone to play or did u think it wasn't worth paying for? just label a price on the app store or add a place to donate for it.",
      "really having fun with this. great art style. fun  challenging puzzles. but lowkey and casual. i love it!",
      "loved this game alot  completed a couple of times but still never got bored. eagerly waiting for next version...yeah i know we can download different levels from browser but still just waiting for more. do try this game guys you'll love it for sure.",
      "the game's amazing....i have tried many games over time...and its one of the very good games' category that i would put this game in. it's not very addictive so won't kill ur precious time and it's fun...so overall....good games for everyone looking for a rest time game",
      "i love it. its tricks the mind  but the music and beautiful simple graphic dilutes the pressure and make it such a soothing and refreshing game.",
      "good game on this trashy app store",
      "nice and very entertaining game",
      "good game. give it a try and see for your self.",
      "fix da game wen ay enter it is black all"]


    print("The result is :" , predictData(new_reviews))

    print("----------------DONE------------------------")