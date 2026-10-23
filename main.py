def sentiment_analysis(text):
    positive = ["good", "great", "excellent", "happy", "love", " amazing"]
    negative = ["bad", "worst", "terrible", "sad", "hate", "poor"]

    words = text.lower().split()

    pos = sum(word.strip(".,!?") in positive for word in words)
    neg = sum(word.strip(".,!?") in negative for word in words)

    if pos > neg:
        return "Positive 😊"
    elif neg > pos:
        return "Negative"
    else:
        return "Neutral"

review = input("Enter your review: ")
print("Sentiment:", sentiment_analysis(review))