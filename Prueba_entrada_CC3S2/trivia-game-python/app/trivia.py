# clase para una pregunta de trivia.
class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    # Verifica si una respuesta dada es correcta.
    def is_correct(self, answer):
        return self.correct_answer == answer


# clase para un quiz con puntuación y manejar las rondas.
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    # agregar una nueva pregunta al quiz
    def add_question(self, question):
        self.questions.append(question)

    # devuelve la siguiente pregunta del quiz
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    # recibe una respuesta para una pregunta y actualiza el puntaje
    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False


# ejecuta el juego de trivia
def run_quiz():
    # agregar interfaz
    print("Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    print("Nivel de dificultad: Fácil\n")  # agregar dificultad
    

    quiz = Quiz()

    # se crean 2 preguntas de ejemplo
    questions = [
        Question(
            "Pregunta 1: ¿Cuál es la capital de Francia?",
            ["Madrid", "Londres", "París", "Berlín"],
            "París"
        ),
        Question(
            "Pregunta 2: ¿Cuánto es 2 + 2?",
            ["3", "4", "5", "6"],
            "4"
        ),
    ]

    # agregamos las preguntas al quiz
    for q in questions:
        quiz.add_question(q)

    # si hay menos de 10 preguntas, duplicamos las existentes hasta tener 10
    while len(quiz.questions) < 10:
        quiz.questions.extend(questions)
    quiz.questions = quiz.questions[:10]  # Nos aseguramos de tener exactamente 10 preguntas

    # se maneja el flujo de 10 rondas
    round_number = 1
    while round_number <= 10:
        current_question = quiz.get_next_question()
        if not current_question:
            print("No hay más preguntas disponibles. Fin del quiz.")
            break

        # presentación de cada pregunta 
        print(f"\nPregunta {round_number}: {current_question.description}")
        for index, option in enumerate(current_question.options, start=1):
            print(f"  {index}) {option}")

        # se solicita la respuesta del usuario y se convierte el número a la opción en texto
        try:
            user_input = int(input("Tu respuesta: ").strip())
            if 1 <= user_input <= len(current_question.options):
                selected_option = current_question.options[user_input - 1]
            else:
                print("Número fuera de rango. Se cuenta como incorrecta.")
                selected_option = ""
        except ValueError:
            print("Entrada inválida. Se cuenta como incorrecta.")
            selected_option = ""

        if quiz.answer_question(current_question, selected_option):
            print("¡Correcto!")
        else:
            print("Incorrecto!")

        round_number += 1


    print("\nJuego terminado.")
    print("----- Resumen del Juego -----")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")


if __name__ == "__main__":
    run_quiz()
