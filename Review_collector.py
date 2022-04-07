from asyncio.windows_events import NULL
from google_play_scraper import Sort, reviews
import os.path


def get_reviews(app_name, app_link):

    save_path = r"C:\Users\karah\Desktop\review"

    completeName = os.path.join(save_path, app_name+".txt")   
   
    f = open(completeName, "w", encoding="utf-8")

    result, continuation_token = reviews(
    app_link,
    lang='en', # defaults to 'en'
    country='TR', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=1000, # defaults to 100
    
    )

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

    result, _ = reviews(
        app_link,
        continuation_token=continuation_token # defaults to None(load from the beginning)
    )
    for rev in result:
       
        user = rev["userName"]
        content = rev["content"]
       
        f.write(user + " : "+ content + "\n")

    
    f.close()

def get_reviews_from_all(file_name):
    save_path = r"C:\Users\karah\Desktop\review"

    completeName = os.path.join(save_path, file_name+".txt")   
   
    f = open(completeName, "r", encoding="utf-8")
    for line in f:
        lst = line.split("-")
        if(lst[0] == NULL or lst[1] == NULL):
            continue
        get_reviews(lst[0].strip(), lst[1].strip())
    f.close()



if __name__ == '__main__':
    get_reviews_from_all("google_play_apps")
    print("-------------DONE------------------------")