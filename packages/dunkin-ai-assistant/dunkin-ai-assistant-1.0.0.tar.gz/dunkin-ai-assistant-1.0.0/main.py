import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Button, Label, Canvas
import os
from difflib import SequenceMatcher
import threading
import PyPDF2
import pyttsx3
import speech_recognition as sr
from nltk.tokenize import sent_tokenize
import openai
import spacy
from PIL import Image, ImageTk

# Setup OpenAI
openai.api_key = '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'

# Initialize text-to-speech and speech recognition
engine = pyttsx3.init()
recognizer = sr.Recognizer()

state = {"questions": [], "document_content": "", "responses": []}

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_md")

file_path = r"D:\Chatgpt_voice_assessment\Trial_changes\ss.txt"  # Adjust this to your file path

def upload_document(file_path):
    try:
        if file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                document_content = ''
                for page in reader.pages:
                    document_content += page.extract_text() + " "
        else:
            with open(file_path, 'r') as file:
                document_content = file.read()
        return document_content
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."

def generate_questions(document_content, num_questions=3):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": document_content},
                {"role": "assistant", "content": "Generate questions based on the document."},
            ],
            max_tokens=num_questions * 20,
        )
        questions = response.choices[0].message.content.strip().split("\n")
        return questions[:num_questions]
    except Exception as e:
        return ["Error generating questions: " + str(e)]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_most_similar_sentence(user_response, document_content):
    sentences = sent_tokenize(document_content)
    highest_score = 0
    most_similar_sentence = None
    for sentence in sentences:
        score = similar(user_response.lower(), sentence.lower())
        if score > highest_score:
            highest_score = score
            most_similar_sentence = sentence
    return most_similar_sentence

def provide_feedback_with_similarity(user_response, most_similar_sentence, similarity_score):
    if similarity_score >= 0.75:
        feedback = "Wow, that's correct!"
    elif similarity_score >= 0.5:
        feedback = "Your answer is Partially correct."
    else:
        feedback = "That's wrong."
    correct_answer = f"The correct answer: {most_similar_sentence}"
    feedback_text = feedback + "\n" + correct_answer
    threading.Thread(target=speak_feedback, args=(feedback_text,)).start()
    return feedback_text

def calculate_similarity(user_response, sentence):
    # Parse the sentence to get the word vectors
    doc = nlp(sentence)
    # Calculate the word vector for the user's response
    response_doc = nlp(user_response)
    # Calculate cosine similarity between the vectors
    return response_doc.similarity(doc)

def find_correct_sentence(user_response, document_content):
    sentences = sent_tokenize(document_content)
    highest_similarity = 0
    most_similar_sentence = None
    for sentence in sentences:
        similarity = calculate_similarity(user_response, sentence)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_sentence = sentence
    return most_similar_sentence, highest_similarity

def speak_feedback(feedback_text):
    engine.setProperty('rate', 125)
    engine.say(feedback_text)
    engine.runAndWait()

def save_responses(file_path, question, answer, feedback):
    responses_file = os.path.splitext(file_path)[0] + "_responses.txt"
    with open(responses_file, "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n")
        file.write(f"Feedback: {feedback}\n\n")

def listen_response():
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            return text
    except (sr.UnknownValueError, sr.RequestError):
        return None

def speak_question(question):
    engine.setProperty('rate', 125)
    engine.say(question)
    engine.runAndWait()

def ask_question_voice_or_text(question):
    threading.Thread(target=speak_question, args=(question,)).start()

    def voice_response():
        user_response = listen_response()
        if user_response:
            most_similar_sentence, similarity_score = find_correct_sentence(user_response, state["document_content"])
            feedback_text = provide_feedback_with_similarity(user_response, most_similar_sentence, similarity_score)
            save_responses(file_path, question, user_response, feedback_text)
            messagebox.showinfo("Feedback", feedback_text)
            response_window.destroy()
            next_question()
        else:
            not_captured_message = "Sorry, I didn't catch that. Please try again or type your answer."
            label.config(text=not_captured_message)
            speak_feedback(not_captured_message)

    def text_response():
        user_response = simpledialog.askstring("Response", "Type your answer here:")
        if user_response:
            most_similar_sentence, similarity_score = find_correct_sentence(user_response, state["document_content"])
            feedback_text = provide_feedback_with_similarity(user_response, most_similar_sentence, similarity_score)
            save_responses(file_path, question, user_response, feedback_text)
            messagebox.showinfo("Feedback", feedback_text)
            response_window.destroy()
            next_question()

    response_window = Toplevel(root)
    response_window.title("Choose Response Method")
    Label(response_window, text=question).pack(pady=10)
    Button(response_window, text="Respond with Voice", command=voice_response).pack(side=tk.LEFT, padx=(20, 10), pady=20)
    Button(response_window, text="Type Response", command=text_response).pack(side=tk.RIGHT, padx=(10, 20), pady=20)
    label = Label(response_window, text="")
    label.pack(pady=(10, 0))

    response_window.update_idletasks()
    width = response_window.winfo_width()
    height = response_window.winfo_height()
    x = (response_window.winfo_screenwidth() // 2) - (width // 2)
    y = (response_window.winfo_screenheight() // 2) - (height // 2)
    response_window.geometry(f"{width}x{height}+{x}+{y}")

def next_question():
    if state["questions"]:
        question = state["questions"].pop(0)
        ask_question_voice_or_text(question)
    else:
        close_application()

def start_questions(file_path, root):
    document_content = upload_document(file_path)
    if document_content.startswith("File not found"):
        messagebox.showerror("Error", document_content)
    else:
        state["document_content"] = document_content
        questions = generate_questions(document_content)
        if questions:
            state["questions"] = questions
            next_question()
        else:
            messagebox.showinfo("Info", "No questions generated.")

def hide_start_button(start_button):
    start_button.destroy()

def close_application():
    engine.say("Thank you for attending the session.")
    engine.runAndWait()
    root.destroy()
    
def start_button_clicked(start_button, root):
    global file_path
    hide_start_button(start_button)
    start_questions(file_path, root)


def create_gui():
    global root
    root = tk.Tk()
    root.title("Dunkin")

    # Use a light background color instead of an image
    background_color = "#FFC0CB"
    canvas = Canvas(root, width=800, height=600, bg=background_color)

    # Use grid for the canvas
    canvas.grid(row=0, column=0, sticky="nsew")

    # Logo image adjustments
    logo_img_path = "D:\Chatgpt_voice_assessment\Trial_changes\Dunkin_logo.png"  # Update with your path

    # Load and place logo
    logo_img = Image.open(logo_img_path).convert("RGBA").resize((200, 100), Image.Resampling.LANCZOS)  # Adjust size as needed

    # Create PhotoImage with transparent background
    logo_image = ImageTk.PhotoImage(logo_img)

    # Place the logo at the center of the canvas
    canvas.create_image(10, 10, anchor=tk.NW, image=logo_image)

    # Styling buttons
    start_button_style = {'font': ('Helvetica', 20, 'bold'), 'background': 'orange', 'foreground': 'white', 'padx': 10, 'pady': 5}
    start_button = Button(root, text="START", command=lambda: start_button_clicked(start_button, root), **start_button_style)

    # Use grid for the start_button
    start_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    # Ensure proper close event handling
    root.protocol("WM_DELETE_WINDOW", lambda: close_application())

    # Make GUI responsive
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
