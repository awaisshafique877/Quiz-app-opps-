import tkinter as tk
from tkinter import messagebox

# Sample Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "HTML", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"],
        "answer": "Central Processing Unit"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App with Timer")
        self.root.geometry("500x400")
        
        self.question_index = 0
        self.score = 0
        self.time_limit = 15  # seconds per question
        self.time_left = self.time_limit
        
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=450)
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}s", font=("Arial", 14))
        self.timer_label.pack(pady=20)

        self.next_question()
    
    def next_question(self):
        if self.question_index < len(questions):
            self.time_left = self.time_limit
            self.update_timer()

            q = questions[self.question_index]
            self.question_label.config(text=f"Q{self.question_index + 1}: {q['question']}")
            for i, option in enumerate(q['options']):
                self.option_buttons[i].config(text=option, state="normal")
        else:
            self.show_result()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.disable_buttons()
            self.root.after(1000, self.next_question_delay)

    def check_answer(self, selected_index):
        self.root.after_cancel(self.timer_id)
        selected_option = questions[self.question_index]['options'][selected_index]
        correct_answer = questions[self.question_index]['answer']
        if selected_option == correct_answer:
            self.score += 1
        self.disable_buttons()
        self.root.after(1000, self.next_question_delay)

    def disable_buttons(self):
        for btn in self.option_buttons:
            btn.config(state="disabled")

    def next_question_delay(self):
        self.question_index += 1
        self.next_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your score is {self.score}/{len(questions)}")
        self.root.destroy()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
