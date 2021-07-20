# Bank-Note-Authentication-kaggle-project
This is a project enisted on Kaggle(https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data). Named as Bank Note Authentication, the aim of the project was to determine the authenticity of bank notes based on the different
features(independent variables) provided in the csv datasheet categorised as- variance, skewness, curtosis and entropy. The dependent variable column, named as class consists of two
values-0 and 1, implying if the data implies to a fake bank note or not.

1. Building the ML Model:
The dependent variable being a categorical variable, the model to be used is a classification model. The data was complete and hence no cleaning was required. The values were too 
properly to the scale and hence no scaling or normalisation technique was used.
Accuracy on all the classification models available was tested and Random Forest Classifier was found to be the best technique. The accuracy was 0.9902912621359223. The train-test split
was the default value of 0.25.
The libraries used were as follows: numpy, pandas, sklearn, matplotlib.pyplot, pickle

2. Building the webapp:
The web application was built using flask for the backend. No html was used as the frontend. Instead flasgger was used for building a normal interface. Another implementation was 
done using streamlit library

Containerizing the app is done with Docker(toolkit).
