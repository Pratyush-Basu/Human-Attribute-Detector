from flask import Flask, render_template, request
import google.generativeai as genai
import base64
from io import BytesIO
import PIL.Image
import os
from dotenv import load_dotenv



# Initialize Flask app
app = Flask(__name__)

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Function to analyze image
def analyze_human_attributes(image):
    # Convert image to Base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")  # Ensure PNG format
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # AI Prompt
    prompt = """
    You are an AI trained to analyze human attributes from images.  
    Provide structured analysis including:  
    - Gender : 
    - Age Estimate :
    - Face Shape : (Oval, Round, Square, Heart, Diamond)
    - Ethnicity : 
    - Mood :  
    - Facial Expression :
    - Accessories :(Earrings, Necklace, Watch, Hat, Headphones)
    - Clothing Type :(Formal, Casual, Traditional and it's colour)
    - Makeup Detection (Lipstick, Eye Shadow, No Makeup and more if applicable)
    - Teeth Visibility :(Visible, Not Visible [Analysis carefully for Female,Because the wear nose pin sometimes])
    - Posture & Head Tilt :(Straight, Tilted, Slouched)
    - Mask Detection :(Yes/No) [if yes, colour of mask] 
    - Glasses :(Yes/No)[if yes shape of the glass and frame visible color of the frame]  
    - Beard : (Yes/No) [if yes beard colour and if female no need to write Bread:No]  
    - Hair Color :  
    - Eye Color :
    - Headwear : (Yes/No) [if yes what type of headwear is and colour]  
    - Emotions Detected : (e.g., Joyful, Focused, Angry, etc.)
    - Confidence Level :[Level(Eg.low,medium,high) and also add in percentage also]
    Also try to find he/she is any public figure or not.
    Give the result this format don't use **Attributes** Ans Format]
    And Also do detail analysis of everything including background.
    Remove *** always.
    """

    # Send request to Google Gemini API
    try:
        response = model.generate_content(
            [
                {"text": prompt},
                {"inline_data": {"mime_type": "image/png", "data": img_base64}}
            ]
        )
        cleaned_response = response.text.replace("**", "").strip() if response.text else "No response received."
        return cleaned_response
    except Exception as e:
        return f"Error: {str(e)}"

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return "No image uploaded"

    file = request.files['image']
    image = PIL.Image.open(file)
    result = analyze_human_attributes(image)
    
    return result

# Run Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
