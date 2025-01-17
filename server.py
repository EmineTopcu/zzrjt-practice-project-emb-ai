from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyser

app = Flask('Sentiment Analyser')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    textToAnalyze = request.args.get('textToAnalyze')
    #response = sentiment_analyser(textToAnalyze)
    #sentiment = response['label']
    #score = response['score']
    return textToAnalyze #"The given text has been identified as {} with a score of {}.".format(label, score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)