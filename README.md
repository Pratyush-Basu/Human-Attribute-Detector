# 🧠 Human Attribute Detector using Google Gemini API

This project uses **Google's Gemini AI** to analyze and extract detailed human attributes from uploaded images. Built using **Flask**, this app lets users upload a face image and returns structured information such as gender, age estimate, emotion, accessories, and more.

---

## 🔍 Features

- Detects:
  - Gender
  - Age estimate
  - Face shape
  - Ethnicity
  - Facial expression & mood
  - Accessories (glasses, earrings, etc.)
  - Clothing type & color
  - Makeup
  - Posture & head tilt
  - Mask detection
  - Beard and hair details
  - Eye color
  - Emotions
  - Public figure detection
  - Confidence level (percentage + text)

---

## 🚀 How It Works

1. User uploads an image via the web interface.
2. Image is converted to Base64 and sent to the **Gemini AI (gemini-1.5-flash-latest)**.
3. Gemini returns a detailed analysis of human attributes.
4. The output is cleaned and displayed without markdown symbols like `**`.

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Google Generative AI (`google-generativeai`)
- dotenv
- Pillow (PIL)
- HTML (for `index.html` form)

---
###🙌 Credits
Developed by Pratyush Basu
Powered by Google Gemini API


## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Pratyush-Basu/Human-Attribute-Detector.git
cd Human-Attribute-Detector


