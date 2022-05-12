import os.path
from asyncio.windows_events import NULL

def sort_comments(game_name):


    save_path = r"C:\Users\karah\Desktop\cs48000-group7"
   
    app_name = "sorted_comments"
    

    completeName1 = os.path.join(save_path, app_name+".txt")
    completeName3 = os.path.join(save_path, game_name+".txt")
    
    count = 0

    f3 = open(completeName3, "r", encoding="utf-8")       
    lines = f3.readlines()
    
    for line in lines:
        lst = line.split(":")
        removedCom = lst[1].replace(",", " ")
        removedCom = removedCom.replace("\n", "")
        print(removedCom)
        inp = input("Enter 1 for positive, Enter 2 for negative,, Enter 3 to skip, Enter 0 to end: (currently " + str(count) + " comments)")
        print(inp)
    
        if inp == "1" :
            f1 = open(completeName1, "a", encoding="utf-8")
            f1.write(removedCom + ",1\n")
            f1.close()
            count += 1
        if inp == "2" :
            f1 = open(completeName1, "a", encoding="utf-8")
            f1.write(removedCom + ",0\n")
            f1.close()
            count += 1
        if inp == "3" :
            continue
        if inp == "0" :
            break


    f3.close()
    

    


if __name__ == '__main__':
    
    sort_comments("Redbros")
    print("-------------DONE------------------------")