''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed
    on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector

#Initialize the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using the emotion_detection()
        function. The output returned shows the confidence scores for
        emotions and shows the name of the dominant emotion.
    '''
    # Get text to analyze from the request
    text_to_analyze = request.args.get('textToAnalyze')

    # Perform emotion detection and store the result
    response = emotion_detector(text_to_analyze)

    # Check for null response, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."

    # Otherwise format and return an output string
    dominant_emotion = response['dominant_emotion']
    output = "For the given statement, the system response is: "
    output += f"'anger': {response['anger']} "
    output += f"'disgust': {response['disgust']} "
    output += f"'fear': {response['fear']} "
    output += f"'sadness': {response['sadness']} "
    output += f"'joy': {response['joy']}. "
    output += f"The dominant emotion is {dominant_emotion}."

    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)