from asyncio.windows_events import NULL
from google_play_scraper import Sort, reviews_all, app
import os.path
from langdetect import detect
from cleantext import clean


used_links = [];


def get_reviews(app_name, app_link):

    save_path = r"C:\Users\karah\Desktop\cs48000-group7"

    completeName = os.path.join(save_path, app_name+".txt") 
    
      
   
    f = open(completeName, "w", encoding="utf-8")

    

    result = reviews_all(
    app_link,
    lang='en', # defaults to 'en'
    country='TR', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
   
    )

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

   
    if len(result) == 0:
        f.close()
        os.remove(completeName)
        pass

    for rev in result:
       
        user = clean(rev["userName"], no_emoji=True)
        content = clean(rev["content"], no_emoji=True)

        lang = "try"

        try:
            lang = detect(content)
        except:
            lang = "error"
            print("This row throws an error")

        if(len(user) == 0 or len(content) == 0 or lang != 'en'):
            continue
       
        f.write(user + " : "+ content + "\n")

    
    f.close()


def get_reviews_rec(app_link, num):
    
    app_info = app(
    app_link,
    lang='en', # defaults to 'en'
    country='TR' # defaults to 'us'
    )
    print(app_info["title"])
    used_links.append(app_link)

    similarlst = app_info["similarApps"]

    similar = ""

    for item in similarlst:
        if item not in used_links:
            similar = item
        else:
            break
    
    
    save_path = r"C:\Users\karah\Desktop\cs48000-group7"

    completeName = os.path.join(save_path, app_info["title"]+".txt") 
    
      
   
    f = open(completeName, "w", encoding="utf-8")

    
    
   
    result = reviews_all(
    app_link,
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='TR', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
    )
    
    

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

    if len(result) == 0:
        f.close()
        print("closed mid")
        os.remove(completeName)
        pass

    for rev in result:
       
        user = clean(rev["userName"], no_emoji=True)
        content = clean(rev["content"], no_emoji=True)

        lang = "try"

        try:
            lang = detect(content)
        except:
            lang = "error"
            print("This row throws an error")

        if(len(user) == 0 or len(content) == 0 or lang != 'en'):
            continue
       
        f.write(user + " : "+ content + "\n")

    
    f.close()
    print("closed end")
    if num > 0:
        get_reviews_rec(similar, num -1)

def get_reviews_from_all(file_name):
    save_path = r"C:\Users\karah\Desktop\cs48000-group7"

    completeName = os.path.join(save_path, file_name+".txt")   
   
    f = open(completeName, "r", encoding="utf-8")
    for line in f:
        lst = line.split("-")
        if(lst[0] == NULL or lst[1] == NULL):
            continue
        get_reviews(lst[0].strip(), lst[1].strip())
    f.close()



if __name__ == '__main__':
    #get_reviews_from_all("google_play_apps")
    get_reviews_rec("com.noodlecake.altosadventure", 10)
    print("-------------DONE------------------------")