class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_quest = Question("How to fly?", "False")
sec_question = Question("Where is the Eagle?", "New York")
print(sec_question.answer)
print(new_quest.text)