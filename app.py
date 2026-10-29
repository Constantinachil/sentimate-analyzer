import pandas as pd
from textblob import TextBlob

# sample data
data = [
    {"id": 1, "text": "This product is absolutely fantastic and works like a charm!"},
    {"id": 2, "text": "Terrible customer service. I am completely disappointed."},
    {"id": 3, "text": "It is okay, nothing special, just an average experience."},
    {"id": 4, "text": "Great value for money, highly recommended to everyone."},
    {"id": 5, "text": "Awful quality. Broke after two days of use."}
]

df = pd.DataFrame(data)

# fuction Sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
   
    if polarity > 0.1:
       sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return pd.Series([polarity, sentiment])

# data application
df[['Polarity_Score', 'Sentiment']] = df['text'].apply(analyze_sentiment)

# display results
print(" ΑΠΟΤΕΛΕΣΜΑΤΑ ΑΝΑΛΥΣΗΣ ")
print(df[['text', 'Sentiment', 'Polarity_Score']])

print("\n ΣΥΝΟΨΗ (DATA INSIGHTS) ")
print(df['Sentiment'].value_counts())

# restore σε CSV
df.to_csv("analyzed_results.csv", index=False)
print("\n[OK] Τα αποτελέσματα αποθηκεύτηκαν στο 'analyzed_results.csv'")
    
    