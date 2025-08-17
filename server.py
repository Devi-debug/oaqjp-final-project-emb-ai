''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app.
app=Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_analyzer():
    '''This code receives the text from the HTML interface and
       runs emotion analysis over it using emotion_detector()
       function. The output returned shows the emotion and their score.
    '''
    text_to_analyze=request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    dominant_emotion=response['dominant_emotion']
    if dominant_emotion  is None:
        return "Invalid text! please try again!"
    emotion_scores=", ".join([
        f"'{emotion}: {score}'"
        for emotion,score in response.items()
        if emotion != 'dominant_emotion'
    ])
    
    result_text=(f"For the given statement, the system response is {emotion_scores}. "
    f"The dominant emotion is {dominant_emotion}.")
    return result_text

@app.route("/")
def render_index_page():
    '''This function initiates the rendering of the main application
       page over the Flask channel.
    '''
    return render_template('index.html')
if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
