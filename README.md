# InnerPeace AI

**InnerPeace AI** is an advanced conversational AI chatbot designed to provide compassionate and insightful guidance on personal relationships and life challenges. Built using Google’s Generative AI API for natural language understanding and **pyttsx3** for faster, offline Text-to-Speech (TTS) responses, it serves as a virtual therapist for users seeking emotional support.

## Patent Granted
- **Patent Link**: IEEE Xplore – [Patent #10894494](https://ieeexplore.ieee.org/document/10894494)
## Key Features

- **Natural Language Understanding**: InnerPeace.AI leverages Google Generative AI to respond intelligently and contextually.
- **Offline Text-to-Speech**: Integrated with `pyttsx3` for real-time, offline voice responses with minimal delay.
- **Streamlit UI**: Simple and user-friendly web interface using **Streamlit**.
- **Scalable Architecture**: Designed for smooth deployment and interaction.

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Niranjan-NN/InnerPeace.AI/
cd InnerPeaceAI
```

### 2. Install Dependencies
Ensure you have Python 3.x installed. Then, install the required Python libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
To use Google Generative AI, configure your API key:
```python
genai.configure(api_key="YOUR_GOOGLE_API_KEY")
```

### 4. Run the Application
The UI is built using **Streamlit**. To run the application locally, execute the following command:
```bash
streamlit run main.py
```

### 5. Access the App
Once the app is running, you can access it by opening your browser and navigating to the local URL displayed in the terminal (usually `http://localhost:8501`).

## How to Use

1. **Enter Your Query**: Users can type their personal challenges or questions in the input box provided on the web interface.
2. **Get a Response**: Nila-AI processes the query using Google Generative AI and provides a thoughtful and empathetic response. 
3. **Text-to-Speech (Optional)**: The chatbot will also speak the response aloud using `pyttsx3`, giving an interactive, voice-based experience.

## Project Structure

- **main.py**: Contains the core logic and UI with updated Text-to-Speech functionality using `pyttsx3`.
- **requirements.txt**: Lists the required dependencies for the project.

## Core Workflow

1. **Input**: The user inputs their query or problem.
2. **Processing**: The query is analyzed by Google Generative AI and a thoughtful response is generated.
3. **Output**: The response is displayed as text in the UI and spoken aloud using `pyttsx3` (for offline TTS).

## Documentation & References

- [Google Generative AI Documentation](https://cloud.google.com/generative-ai)
- [pyttsx3 Text-to-Speech Documentation](https://pypi.org/project/pyttsx3/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Google API Client](https://googleapis.dev/python/google-api-core/latest/index.html)

For more detailed API integration or advanced use cases, please refer to the above official documentation.

## Other Projects

- 📝 **Smart Ration** – An app that streamlines ration booking.
- 🌏 **FieastaIndiana** – A tourism platform enabling bookings for hotels, guides, and more.
- 🤖 **Aara** – An AI-powered chatbot for image recognition and insights.
## Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, make your changes, and submit a pull request. Suggestions to improve functionality or add new features are encouraged.

