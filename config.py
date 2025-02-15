from dotenv import load_dotenv
import os
import google.generativeai as genai
# from chat_gemini import GeminiChatBot
from langchain_google_genai import ChatGoogleGenerativeAI
# Load environment variables from .env file
load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-pro")
print(llm.invoke("how is relationship with trump and modi?"))
# # Configuration class to store all application settings
class Config:
    # OpenAI API configuration
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    # Flask configuration
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-here')
    
    # Model configuration
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/tumor_classifier.pkl')
    IMAGE_SIZE = (100, 100)  # Size to resize all input images
    
    # Upload configuration
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}