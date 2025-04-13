
# clase que representa una pregunta trivia
class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    # verificar si una respuesta dada es correcta
    def is_correct(self, answer):
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

def run_quiz():
    # creamos una instancia de Quiz
    quiz = Quiz()
    
    # creamos algunas preguntas de ejemplo utilizando la clase Question
    question1 = Question(
        "¿Cuál es la capital de Francia?",
        ["Madrid", "Londres", "París", "Berlín"],
        "París"
    )
    question2 = Question(
        "¿Cuánto es 2 + 2?",
        ["3", "4", "5", "6"],
        "4"
    )

    # Agregamos las preguntas al quiz
    quiz.add_question(question1)
    quiz.add_question(question2)
    
    #  ir imprimiendo cada pregunta hasta que no queden
    while True:
        current_question = quiz.get_next_question()
        if not current_question:
            print("No hay más preguntas. Fin del quiz.")
            break
        # Imprime el enunciado y las opciones
        print(f"Pregunta: {current_question.description}")
        for index, option in enumerate(current_question.options, start=1):
            print(f"  {index}) {option}")
        print()  # Línea en blanco para separar preguntas

# si ejecutamos este archivo directamente correremos run_quiz()
if __name__ == "__main__":
    run_quiz()
