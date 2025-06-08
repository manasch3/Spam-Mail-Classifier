# Spam Mail Classifier

CleanInbox AI is a machine learning-based web application that detects and classifies spam messages. This project uses natural language processing (NLP) and a trained classification model to accurately identify spam emails, helping users maintain a cleaner and safer inbox.

## Features

- Real-time spam detection using a trained machine learning model
- Text preprocessing with TF-IDF vectorization
- Flask-based web interface with a simple frontend
- Lightweight and easy to run locally

## Tech Stack

- **Backend**: Python, Flask  
- **Machine Learning**: Scikit-learn  
- **NLP**: NLTK  
- **UI**: HTML (Jinja2 Template)  
- **Model Files**: `model.pkl`, `vectorizer.pkl`  

## Project Structure

```
spammail-master/
├── app.py              # Main Flask application
├── model.pkl           # Trained spam classifier model
├── vectorizer.pkl      # TF-IDF vectorizer used during training
├── spam.csv            # Dataset used for model training
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML template for the frontend
```

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://localhost:5000/
   ```

## Usage

- Enter a message into the input field.
- Click on the "Predict" button.
- The model will output whether the message is **Spam** or **Not Spam**.

## Notes

- `model.pkl` is a logistic regression model trained on labeled email messages.
- The TF-IDF vectorizer (`vectorizer.pkl`) transforms input text into numerical features.
- `spam.csv` contains the dataset used to train and validate the model.

## Future Improvements

- Add batch message classification
- Improve UI with dark mode and real-time confidence feedback
- Export prediction results as downloadable reports

## License

This project is for educational purposes and is open-source under the MIT License.

