import spacy
import nltk
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from goose3 import Goose
from nltk.tokenize import sent_tokenize

# Download models and data
nltk.download('punkt_tab', quiet=True)  # quiet=True para não poluir o terminal
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_lg"])
    nlp = spacy.load("en_core_web_lg")

g = Goose()

# Update article for astronomy
def update_article_about_astronomy():
    url_astronomy = "https://en.wikipedia.org/wiki/General_relativity"
    print(f"🔄 Fetching new article about Astronomy.")
    try:
        article = g.extract(url=url_astronomy)
        return article.cleaned_text
    except Exception as e:
        print(f"⚠️ Could not fetch article about Astronomy: {str(e)}")
    return None

# Preprocessing
def preprocessing(sentence):
    sentence = sentence.lower()
    tokens = [
        token.text for token in nlp(sentence)
        if not (token.is_stop or token.like_num or token.is_punct or token.is_space or len(token) == 1)
    ]
    return ' '.join(tokens)

# Question keywords
question_keywords = {
    "how many": "quantity",
    "how much": "amount",
    "how long": "duration",
    "how often": "frequency",
    "what": "definition",
    "who": "person",
    "when": "time",
    "where": "place",
    "why": "reason",
    "how": "method",
    "which": "choice",
}

def get_question_type(question):
    question = question.lower()
    for key in question_keywords:
        if key in question:
            return question_keywords[key]
    return "unknown"

# Chatbot answer
def answer(user_text, threshold=0.1):
    question_type = get_question_type(user_text)

    cleaned_sentences = [preprocessing(sentence) for sentence in original_sentences]
    user_text_clean = preprocessing(user_text)
    cleaned_sentences.append(user_text_clean)

    tfidf = TfidfVectorizer()
    x_sentences = tfidf.fit_transform(cleaned_sentences)

    similarity = cosine_similarity(x_sentences[-1], x_sentences[:-1]).flatten()

    for i, sentence in enumerate(original_sentences):
        lower_sentence = sentence.lower()
        if question_type == "time" and any(char.isdigit() for char in lower_sentence):
            similarity[i] *= 1.2
        elif question_type == "method" and ("how" in lower_sentence or "process" in lower_sentence):
            similarity[i] *= 1.2
        elif question_type == "definition" and ("is" in lower_sentence or "refers to" in lower_sentence):
            similarity[i] *= 1.2

    best_index = similarity.argmax()
    best_score = similarity[best_index]

    if best_score < threshold:
        return "Sorry, no answer was found."
    else:
        return original_sentences[best_index]

# GUI functions
def send_message():
    user_text = user_input.get()
    if not user_text.strip():
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {user_text}\n", 'user')
    chat_area.config(state='disabled')
    user_input.delete(0, tk.END)

    def bot_response():
        loading_label.config(text="⏳ Fetching article, please wait...")
        new_article_text = update_article_about_astronomy()
        if new_article_text:
            global original_sentences
            original_sentences = sent_tokenize(new_article_text)
        loading_label.config(text="")
        bot_text = answer(user_text)
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f"Bot: {bot_text}\n", 'bot')
        chat_area.config(state='disabled')
        chat_area.see(tk.END)

    threading.Thread(target=bot_response, daemon=True).start()

def quit_app():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        window.destroy()

# Initial article (Astronomy)
original_sentences = [
    "Astronomy is the scientific study of celestial bodies such as stars, planets, comets, and galaxies, as well as the phenomena that originate outside Earth's atmosphere."
]

# GUI setup
window = tk.Tk()
window.title("🌌 Astronomy Chatbot")
window.geometry("600x600")
window.config(bg="#f0f8ff")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', bg="#ffffff", fg="#333333", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_input = tk.Entry(window, font=("Arial", 14))
user_input.pack(padx=10, pady=(0, 10), fill=tk.X)

button_frame = tk.Frame(window, bg="#f0f8ff")
button_frame.pack(pady=(0, 10))

send_button = tk.Button(button_frame, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 12), width=10)
send_button.grid(row=0, column=0, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=quit_app, bg="#f44336", fg="white", font=("Arial", 12), width=10)
exit_button.grid(row=0, column=1, padx=5)

loading_label = tk.Label(window, text="", bg="#f0f8ff", fg="#555555", font=("Arial", 10))
loading_label.pack()

# Start GUI
window.mainloop()
