Ryder Nance EC602 Project

This project is a customer service sentiment analyzer. The idea is to enter the twitter handle of the customer service account for a particular company and then the program would grab the sentiment data for that particular company and period. This could be helpful in determing bugs with new software, or if a particular event or change in the company has negatively or positively affected the brand's image. 

The program itself is fairly simply. The system grabs tweets that match the search parameters (the company, date, and time) and then cleans the tweets up with the broom function. The clean tweets are then run through Google's natural language processor and assigned a sentiment score. The output is then tabulated into a list and then printed.



To run:
1. You must EITHER set your path variable for google (set GOOGLE_APPLICATION_CREDENTIALS=[PATH]) to the location of  your downloaded JSON credential file, or you can explicitly define the location in code
2. Determine your access credentials for the twitter API, and enter them into the code. Be careful not to share this information with anyone. 
3. Run the code. Answer the prompts


Interpretation of results:
The NLP outputs a number between -1 and 1, with -1 being a negative sentiment, and 1 being a positive sentiment. I have the result expressed to one decmial point for clarity. 
