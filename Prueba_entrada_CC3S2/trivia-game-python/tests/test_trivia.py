import pytest
from app.trivia import Question


# verificar si cada respuesta es reconocida como correcta
def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")

# verificar si una respuesta incorrecta es detectada como incorrecta
def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")
