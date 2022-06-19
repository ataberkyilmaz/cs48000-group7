# Classifying Game Reviews as Positive or Negative on Google Play Store - Team-7

- Jira Link for the Project: https://cs48000-team7.atlassian.net/jira/software/projects/GPGR/boards/1/backlog


- Project Description

  The objective of this project is to collect data as reviews from the Games submitted to the Google Play Store and in turn using this data predict the positivity and the negativity of the new inputted Games review to be able to give the developer of a game better understanding of the popularity and success of their product.

- Instructions To Get Game Reviews

  Install the following dependencies using the lines below:
  
    npm install node-pandas
    
    npm install scikit-learn
    
    npm install google-play-scraper
    
    npm install languagedetect --save
    
    npm install languagedetect --save
    
  Using the Review_collector.py file get new game review data as a .txt file.
  
  In the main function of the file (line 155) cange the first parameter of the get_review function to the name of the game as a string and then change the second parameter of the function to the Id of the game you choos as a string.
  ![image](https://user-images.githubusercontent.com/102539382/173019665-03c964d7-6863-45dc-ad61-928e463149d0.png)

  You can find the id of the game by going to the google play store:
  
  ![image](https://user-images.githubusercontent.com/102539382/173017902-034853ed-7048-490d-accd-808296432de4.png)
  
  Choose the game you want to get the reviews of:
  
  ![image](https://user-images.githubusercontent.com/102539382/173018169-ba5bbcca-3806-4d16-80e4-4521a4ff3d89.png)

  Go to the link of the website:
  
  ![image](https://user-images.githubusercontent.com/102539382/173018282-4628b8d7-af6d-433a-8f34-7713744a2844.png)

  Get the part after "id=" and before "&gl" if it is there:
  
  ![image](https://user-images.githubusercontent.com/102539382/173018534-99bd1b03-5103-47b0-9b7c-b9283b2237cd.png)

  Then run the code and wait for it to finish. (You will see -------------DONE------------------------ written on the terminal after the collection is done.)
  

- Instructions To Form A Golden Set (If you dont plan on forming your own golden set skip to section Instructions To Expand Training Data)
  
  First open the golden_set.txt file and empty the contents.
  To form your own golden set open the comment_sorter.py file and enter the name of the file you want to sort by hand in the main function of the file into the sort_comments function as a string parameter.

  ![image](https://user-images.githubusercontent.com/102539382/173020052-6ad42807-4f91-4d33-8a56-9882d09197be.png)
  
  Then run the file and follow the instructions on the screen.
  
  After you exit copy the contents of the golden_set.txt file to the empty all_sorted_comments.txt file.
  
- Instructions To Expand Training Data (If you dont plan on forming your own golden set skip to section Instructions To Evaluate the Data)

  To expand the training data open the unsupervised_learning.py file. Then in the main function of the file write the name of the game review folder that you want to add the reviews of the game to the training data into the predictAdd function.
  
  ![image](https://user-images.githubusercontent.com/102539382/173020863-1996f8fd-8c49-4407-aa29-53ee5974f6d5.png)
  
  Then run the code and wait for it to finish. (You will see -------------DONE------------------------ written on the terminal after it is done.)
  

- Instructions To Evaluate the Data
  
  To evaluate a game review file open the evaluation.py file and in the main function write the file name into the evaluate function as a string.
  
  ![image](https://user-images.githubusercontent.com/102539382/173021406-36d525fd-8373-4ed0-9b0d-beab80461125.png)
  
  Then run the code and wait for it to finish. (You will see -------------DONE------------------------ written on the terminal after it is done.)
  
  You can now see the evaluation of the reviews in the terminal.

- Examples

  Example data after Review_collector.py is done:
  
  ![image](https://user-images.githubusercontent.com/102539382/173021674-cdb11870-3679-4a8f-8e45-cbd99dfb2ab3.png)
  
  ![image](https://user-images.githubusercontent.com/102539382/173021722-344981f0-65e0-411a-b38f-158789b26649.png)
  
  Example data after comment_sorter.py is done:
  
  ![image](https://user-images.githubusercontent.com/102539382/173021927-56b12d83-84f7-460d-a306-da093cb544d8.png)
  
  Example data after unsupervised_learning.py is done:
  
  ![image](https://user-images.githubusercontent.com/102539382/173022088-6243c20e-e1f2-4937-a4f1-bd3d902cf72a.png)

  Example of the terminal after evaluation.py is done:
  
  ![image](https://user-images.githubusercontent.com/102539382/173023916-acc758f0-3c20-4d89-ad5f-f30e0f1961af.png)

  
  

  
  

  


