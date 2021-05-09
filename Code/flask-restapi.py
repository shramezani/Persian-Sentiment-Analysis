# importing the required libraries
import settings
from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# load the pipeline object
model = load_model(settings.MODEL_PATH)

with open(settings.TOKENIZER_PATH, 'rb') as handle:
    tokenizer = pickle.load(handle)

def prepare_data(text):    
    sequence_docs = tokenizer.texts_to_sequences([text])
    # pad data to Maximum Sequence Length
    pad_sequence_docs = pad_sequences(sequence_docs, maxlen=settings.SEQUENCE_LEN, padding='post')
    return pad_sequence_docs
 # function to get results for a particular text query
def requestResults(text):
    try:
        padded_text = prepare_data(text )
        prediction = model.predict(padded_text)
        pred = np.argmax(prediction, axis = 1)
        data = "Sentiment: "+str(settings.LABEL_DIC[pred[0]]) + '\n\n'
        return "text: "+str(text)+'\n\n'+ data  
    except Exception :
        return "Systemt couldn't predict sentiment of your text\n please enter a valid text"




# start flask
app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        query = request.form['search']
        return redirect(url_for('success', name=query))

# get the data for the requested query
@app.route('/success/<name>')
def success(name):
    
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)