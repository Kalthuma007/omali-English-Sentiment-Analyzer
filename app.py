
from flask import Flask, render_template, request
from sentiment_analyzer import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    user_input = ""
    if request.method == 'POST':
        user_input = request.form['text']
        if user_input.strip():
            sentiment = analyze_sentiment(user_input)
    return render_template('index.html', sentiment=sentiment, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
