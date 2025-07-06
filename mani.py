import cv2
import time
from deepface import DeepFace
from groq import Groq
import pyttsx3
import speech_recognition as sr

# Configuration
GROQ_API_KEY = "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"
USER_NAME = "Amar"

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Groq Response
def get_groq_response(emotion, user_input):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": f"""You are Jarvis, {USER_NAME}'s humorous AI companion. Respond with humor based on detected emotion:
                - Happy: Playfully joke and be cheerful.
                - Sad: Offer humorous support and motivational jokes.
                - Angry: Calm with humor and funny distractions.
                - Surprise: React with amusing curiosity.
                - Fear or Disgust: Provide funny reassurance.
                - Neutral: Be friendly and humorous."""},
                {"role": "user", "content": f"I am feeling {emotion}. Also, {user_input}"}
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=0.95
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Groq error: {e}")
        return "Oops, I short-circuited! Let's try again!"

# Emotion Detection using DeepFace
def detect_emotion():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    recognizer = sr.Recognizer()

    last_time = 0
    interval = 5

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Capture error")
            break

        input_method = input("Choose input method (type/speak/exit): ").lower().strip()
        if input_method == "exit":
            print("Exiting...")
            break

        user_input = ""

        if input_method == "speak":
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                try:
                    user_input = recognizer.recognize_google(audio)
                    print(f"You said: {user_input}")
                except Exception:
                    print("Sorry, I couldn't understand. Please type your input.")
                    user_input = input("Type your message: ")
        elif input_method == "type":
            user_input = input("Type your message: ")
        else:
            print("Invalid input method. Please choose 'type' or 'speak'.")
            continue

        current_time = time.time()
        if current_time - last_time >= interval:
            try:
                analysis = DeepFace.analyze(frame, actions=['emotion'], detector_backend='mtcnn', enforce_detection=False)
                emotion_probs = analysis[0]['emotion']
                detected_emotion = max(emotion_probs, key=emotion_probs.get)
                print("Detected Emotion:", detected_emotion)

                response = get_groq_response(detected_emotion, user_input)
                print("Jarvis says:", response)
                engine.say(response)
                engine.runAndWait()

                last_time = current_time

            except Exception as e:
                print("Analysis error:", e)

        cv2.imshow("Emotion Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    detect_emotion()