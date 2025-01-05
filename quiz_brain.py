import html
class QuizBrain:

    def __init__(self, q_list):
        self.score_list = []
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        qtext = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {qtext}"


    def check_score(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer.lower():
            if len(self.score_list) < self.question_number:
                self.score += 1
                self.score_list.append(self.score)
            return True
        else:
            self.score_list.append(self.score)
            return False
