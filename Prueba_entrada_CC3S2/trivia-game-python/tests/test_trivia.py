# tests/test_trivia.py
import pytest
from app.trivia import Question, Quiz

# se espera que la respuesta 4 sea correcta.
def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")

# se espera que la respuesta "2" sea incorrecta
def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")

# verificar que el puntaje del quiz se actualiza correctamente
def test_quiz_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    quiz.add_question(question)

    # primera respuesta correcta
    assert quiz.answer_question(question, "4") == True
    assert quiz.correct_answers == 1

    # segunda respuesta por fallo o errores
    assert quiz.answer_question(question, "3") == False
    assert quiz.incorrect_answers == 1
