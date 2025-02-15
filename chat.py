import cv2
import numpy as np
from sklearn.svm import SVC
import pickle
from config import Config

class TumorPredictor:
    def __init__(self):
        """Initialize the tumor predictor with a pre-trained model."""
        self.model = None
        self.load_model()

    def load_model(self):
        """Load the pre-trained SVM model from disk."""
        try:
            with open(Config.MODEL_PATH, 'rb') as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            # If no pre-trained model exists, create a new one
            self.model = SVC(kernel='linear', probability=True)
            
    def preprocess_image(self, image_path):
        """
        Preprocess the input image for prediction.
        
        Args:
            image_path (str): Path to the input image
            
        Returns:
            numpy.ndarray: Preprocessed image as a flattened array
        """
        # Read and convert image to grayscale
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # Resize image to standard size
        img = cv2.resize(img, Config.IMAGE_SIZE)
        
        # Normalize pixel values
        img = img / 255.0
        
        # Flatten the image
        return img.flatten()

    def predict(self, image_path):
        """
        Predict whether the image contains a tumor.
        
        Args:
            image_path (str): Path to the input image
            
        Returns:
            dict: Prediction results including class and probability
        """
        if self.model is None:
            raise ValueError("Model not loaded")
            
        # Preprocess the image
        processed_image = self.preprocess_image(image_path)
        
        # Make prediction
        prediction = self.model.predict([processed_image])[0]
        probability = self.model.predict_proba([processed_image])[0]
        
        return {
            'prediction': 'Tumor' if prediction == 1 else 'Non-Tumor',
            'probability': float(max(probability))
        }