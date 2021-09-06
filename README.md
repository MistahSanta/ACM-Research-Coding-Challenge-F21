# ACM Research Coding Challenge (Fall 2021)  - Jonathan Le

#Note: This was my first coding challenge I have ever done. I would really appreciate it if I can have feedback on what I did well and what I did wrong. Thank you :)

#Questions
The overall sentiment score of the text is a 0.195495 out of a maximum of 1. Since the score is above 0, the author's attitude 
in the text is a little positve. It is not overwhelmingly positive, but a little positive. This score is a little off from what I would have predicted.
From my feelings, I would say the text leans a little more towards the negative than the positive because of the urgency in the text. 
However, the library I use (Textblob) determines the overall sentiment via the words, so the urgency is lost to a number and value of each word. However, the 
sentiment score is still relatively close. My program also determines the subjectivity of the text, which is how opinionated 
a piece of text is. The overall score is a 0.627928 out of a maximum of 1. This is a pretty high score, so the piece of text is 
highly opininated, which I agree with.

#How I arrive at my solution
When taking upon this challenge, I had around 3 days to learn python, pandas library, and sentiment analysis. It was a difficult challenge, but 
I had a lot of fun learning. From one of the videos I watch, I knew I wanted to use Textblob because this sentiment analysis library
seem easy to implement for me, and it had the added bonus to include the subjectivity score, which other libraries did not have. 
When thinking of my solution, I knew I had to import the files into a dataframe, clean up the text to remove punctuation and stop words, 
and finally calculate the authors attitude. This was my "psydo" code, but the difficult part was implementing it. However, after a 
hours of searching the internet and implemnting new ideas, I have the final product that complete each step I wanted. 

#libraries and API
1) Textblob - used to detemine the overall sentiment score
2) Pandas - Used for dataframe
3) re - used to substitude/replace words (clean up text)

#Citation: 
1) <script src="https://gist.github.com/larsyencken/1440509.js"></script> --- Used this txt file as a list of stop words to clean up text
2) https://github.com/ACM-Research/Coding-Challenge-F21 -- ACM challenge that provided me with the input.txt