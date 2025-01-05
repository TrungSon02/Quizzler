from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"
FONT = ("Arial",20,"italic")
SCORE_FONT = ("Courier",10,"bold")
class Interface:
    def __init__(self, quiz: QuizBrain):
        self.timer = None
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.canva = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canva.create_text(150,125,width=280,text="Hello bro", font=FONT, fill=THEME_COLOR)
        self.canva.grid(column=0,row=1,columnspan=2,pady=50)

        correct_img = PhotoImage(file="images/true.png")
        incorrect_img = PhotoImage(file="images/false.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0,command=self.correct)
        self.correct_button.grid(column=0,row=2)
        self.incorrect_button = Button(image=incorrect_img, highlightthickness=0,command=self.incorrect)
        self.incorrect_button.grid(column=1, row=2)

        self.score_display = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=SCORE_FONT)
        self.score_display.grid(column=1,row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canva.itemconfig(self.question_text, text=question)
        else:
            messagebox.showinfo(title="The end", message=f"You ran out of questions.\n Your final score is {self.quiz.score}")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")

    def correct(self):
        self.cancel()
        self.give_feedback(self.quiz.check_score("true"))

    def incorrect(self):
        self.cancel()
        self.give_feedback(self.quiz.check_score("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.timer = self.window.after(1000, self.change_back_background)
        self.score_display.config(text=f"Score: {self.quiz.score}")


    def change_back_background(self):
        self.canva.config(bg="white")
        self.get_next_question()

    def cancel(self):
        try:
            self.window.after_cancel(self.timer)
        except ValueError:
            pass



    # def refill_question(self):
    #     try:
    #         self.get_next_question()
    #     except IndexError:
    #         get_data()