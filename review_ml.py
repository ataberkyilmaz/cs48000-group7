import pandas as pd
import os.path

save_path = r"C:\Users\karah\Desktop\cs48000-group7"

completeName = os.path.join(save_path, "sorted_comments.txt") 




if __name__ == '__main__':



    df = pd.read_csv(completeName, names=['review', 'sentiment'], sep=',') 
    df.head()
    
    print("----------------DONE------------------------")