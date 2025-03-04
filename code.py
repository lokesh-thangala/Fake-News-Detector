def fake_news_detector(text):
    fake_keywords = ["win", "million", "free", "click here", "limited offer"]
    for word in text.lower().split():
        if word in fake_keywords:
            return "Fake News"
    return "Real News"

headline = input("Enter a news headline: ")
print("Prediction:", fake_news_detector(headline))
