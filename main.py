#Description: Program for the ACM coding challenge that determines the overall sentiment value of a piece of text 
import pandas as pd 
from textblob import TextBlob
import re

# open and read text 

input = open("input.txt","r")
T_df = pd.read_table(input, names = ['story'])
# Create a dataframe for stop_words
stopwords = open("stopwords.txt", "r")
S_df = pd.DataFrame(stopwords, columns = ['STOP'])
S_df = S_df['STOP'].replace('\n',' ', regex=True)
S_df = ' ' + S_df.astype(str)  # add spaces at the beginning

# Create a Dataframe for Polarity and Subjecivity 
df = pd.DataFrame()

#def var of the rows of stop words
num_SW = S_df.shape[0]

# Clean up text by removing stop words and special characters 
# run a for loop to check all words if it matches the stop words. If it does, then it removes that word from the text

# Create a function that cleans up the text 
def cleanTxt(text):
    
    for i in range (num_SW):
        text = re.sub((S_df[i]) , ' ', text) # remove stop words in text
    
    text = re.sub(r'[^A-Za-z0-9]+', ' ', text) #remove all punctuation
    return text

T_df['story'] = T_df['story'].apply(cleanTxt)

#Apply the textblob (sentiment Analysis) to rate the overall polarity and subjectivity of the text

#function for subjectivity
def getSub(text):
    return TextBlob(text).sentiment.subjectivity

#function for polarity 
def getPolar(text):
    return  TextBlob(text).sentiment.polarity

#Create two new columns in dataframe
df['Subjectivity'] = T_df['story'].apply(getSub)
df['Polarity'] = T_df['story'].apply(getPolar)

# Create a function breakline that determines the author's attutitudes toward a text (polarity)
def Polar_Analysis(result):
    if result > 0:
        return 'Positive'
    elif result < 0:
        return 'Negetive'
    else:
        return 'Neutral'

df['Polarity_Result'] = df['Polarity'].apply(Polar_Analysis)

print (df)