import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import webbrowser
import nltk

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class FlashcardGeneratorAI:
    def __init__(self, master, data):
        self.master = master
        self.master.title("AI-powered Flashcard Generator")

        # Process data for NLP
        self.questions, self.answers = self.process_data(data)

        # Generate initial flashcards
        self.flashcards = self.generate_flashcards()

        # Initialize flashcard index
        self.current_flashcard_index = 0

        # Create GUI elements
        self.question_label = tk.Label(master, text="Question: ")
        self.question_label.pack()

        self.answer_label = tk.Label(master, text="")
        self.answer_label.pack()

        # Use icons for buttons
        self.show_question_icon = tk.PhotoImage(file="question_icon.png").subsample(3)
        self.show_question_button = tk.Button(master, image=self.show_question_icon, compound="left", command=self.show_question)
        self.show_question_button.pack(side="left", fill=tk.BOTH, expand=True)

        self.show_answer_icon = tk.PhotoImage(file="answer_icon.png").subsample(3)
        self.show_answer_button = tk.Button(master, image=self.show_answer_icon, compound="left", command=self.show_answer)
        self.show_answer_button.pack(side="left", fill=tk.BOTH, expand=True)
        self.show_answer_button.config(state="disabled")

        self.next_flashcard_icon = tk.PhotoImage(file="next_icon.png").subsample(3)
        self.next_flashcard_button = tk.Button(master, image=self.next_flashcard_icon, compound="left", command=self.show_next_flashcard)
        self.next_flashcard_button.pack(side="left", fill=tk.BOTH, expand=True)

        self.feedback_icon = tk.PhotoImage(file="feedback_icon.png").subsample(3)
        self.feedback_button = tk.Button(master, image=self.feedback_icon, compound="left", command=self.show_feedback)
        self.feedback_button.pack(side="left", fill=tk.BOTH, expand=True)

        # Show the first question initially
        self.show_question()

    def process_data(self, data):
        questions = []
        answers = []
        for item in data:
            questions.append(item["question"])
            answers.append(item["answer"])
        return questions, answers

    def generate_flashcards(self):
        flashcards = []
        for i in range(len(self.questions)):
            flashcards.append({"question": self.questions[i], "answer": self.answers[i]})
        return flashcards

    def show_question(self):
        flashcard = self.flashcards[self.current_flashcard_index]
        self.question_label.config(text=f"Question: {flashcard['question']}")
        self.answer_label.config(text="")
        self.show_answer_button.config(state="normal")

    def show_answer(self):
        flashcard = self.flashcards[self.current_flashcard_index]
        self.answer_label.config(text=f"Answer: {flashcard['answer']}")
        self.show_answer_button.config(state="disabled")

    def show_next_flashcard(self):
        if self.current_flashcard_index < len(self.flashcards) - 1:
            self.current_flashcard_index += 1
            self.show_question()

    def show_feedback(self):
        # Get user's answer using askstring from simpledialog
        user_answer = simpledialog.askstring("Feedback", "Enter your answer:")
        if user_answer:
            # Tokenize user's answer
            user_tokens = nltk.word_tokenize(user_answer.lower())

            # Tokenize and lowercase answer
            answer_tokens = nltk.word_tokenize(self.flashcards[self.current_flashcard_index]["answer"].lower())

            # Check if any word in the user's answer matches any word in the answer
            matched_words = [word for word in user_tokens if word in answer_tokens]

            # Provide feedback based on matching words
            if matched_words:
                feedback = "Your answer contains relevant keywords. That's a good start!"
            else:
                feedback = "Your answer doesn't seem to relate to the question. Try again with more relevant content."

            # Show feedback in a popup
            messagebox.showinfo("Feedback", feedback)

def main():
    data = [
        {"question": "What is the difference between stress and strain?", "answer": "Stress is a measure of the internal force per unit area, while strain is a measure of the deformation of a material."},
        {"question": "What is Ohm's Law?", "answer": "Ohm's Law states that the current through a conductor between two points is directly proportional to the voltage across the two points."},
        {"question": "What is the first law of thermodynamics?", "answer": "The first law of thermodynamics, also known as the law of energy conservation, states that energy cannot be created or destroyed in an isolated system."},
        {"question": "What is the difference between renewable and non-renewable energy sources?", "answer": "Renewable energy sources are those that can be replenished naturally, such as sunlight and wind, while non-renewable energy sources are finite and will eventually be depleted, such as fossil fuels."},
        {"question": "What is a differential equation?", "answer": "A differential equation is a mathematical equation that relates the rates of change of a function with respect to one or more independent variables."},
        {"question": "What is the purpose of a control system in engineering?", "answer": "The purpose of a control system is to regulate or control the behavior of a dynamic system to achieve desired objectives."},
        {"question": "What is the concept of torque?", "answer": "Torque is a measure of the force that can cause an object to rotate about an axis."},
        {"question": "What are the different types of bridges?", "answer": "There are several types of bridges, including beam bridges, arch bridges, suspension bridges, and cable-stayed bridges."},
        {"question": "What is the function of a capacitor?", "answer": "A capacitor stores electrical energy in an electric field and can release it when needed."},
        {"question": "What is the purpose of a transistor?", "answer": "A transistor is a semiconductor device used to amplify or switch electronic signals and electrical power."},
        {"question": "What is the difference between parallel and series circuits?", "answer": "In a parallel circuit, the components are connected in parallel branches, allowing different currents to flow through each component, while in a series circuit, the components are connected end-to-end, allowing the same current to flow through each component."}
    ]

    root = tk.Tk()
    app = FlashcardGeneratorAI(root, data)
    root.mainloop()

if __name__ == "__main__":
    main()
