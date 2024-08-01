# BashaConnect

BashaConnect is an interactive web application designed to facilitate seamless speech-to-speech translation between Tamil and English. The platform aims to break language barriers and build bridges by providing accurate and culturally sensitive translations.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Folder Structure](#folder-structure)
6. [Contributing](#contributing)


## Features

- **Voice Recorder**: Record audio in Tamil or English and save it for translation.
- **Speech Translation**:
  - Tamil to English translation with audio playback.
  - English to Tamil translation with audio playback.
- **Blog Posts Section**: Information on the challenges faced by monolinguals and non-native speakers.

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
- **Backend**:
  - Flask (Python)
  - `speech_recognition` for speech-to-text conversion
  - `gtts` for text-to-speech synthesis
  - `deep_translator` for language translation (Google Translator API)
- **Database**:
  - (Optional) SQLite/MySQL for storing user data and translations
- **Hosting**:
  - Can be deployed on cloud services such as AWS, GCP, or Azure

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd BashaConnect
   ```

2. **Install dependencies**:
   Make sure you have Python and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://localhost:5000`.

## Usage

1. **Recording and Translating Audio**:
   - Go to the Voice Recorder section and click "Start Recording" to capture audio in Tamil or English.
   - Upload the recorded audio file in the respective translation section (Tamil to English or English to Tamil).
   - Click "Translate" to get the transcribed text, translated text, and translated audio playback.

2. **Blog Posts**:
   - Browse through the blog posts for insights into language challenges and solutions.

## Folder Structure

```
BashaConnect/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── static/
│   ├── styles.css            # CSS styles
│   ├── scripts.js            # JavaScript scripts
├── uploads/                  # Directory to store uploaded audio files
| templates/
    └── index.html            # Main HTML template
```

## Contributing

We welcome contributions to enhance BashaConnect! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


**BashaConnect** - Breaking Barriers, Building Bridges
