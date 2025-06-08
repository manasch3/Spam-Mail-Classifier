from flask import Flask, request, render_template
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_sms = request.form['sms']
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        prediction = model.predict(vector_input)[0]
        result = "SPAM " if prediction == 1 else "NOT SPAM "

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
