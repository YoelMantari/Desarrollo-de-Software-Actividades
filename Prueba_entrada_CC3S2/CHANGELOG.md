# CHANGELOG - Proyecto Trivia Game

El Juego de Trivia es una aplicación interactiva de preguntas y respuestas por consola, donde el jugador debe responder correctamente 10 preguntas de opción múltiple. Cada pregunta tiene una única respuesta correcta, y el sistema registra el puntaje según el número de respuestas acertadas. Al final del juego, se presenta un resumen con los aciertos, errores y total de preguntas contestadas.

El objetivo principal es combinar lógica de programación y buenas prácticas de desarrollo en FastAPI, pruebas unitarias y manejo de versiones.

---

## Día 1 - Configuración inicial del entorno y estructura básica


### Actividades:
- Se creó la estructura inicial del proyecto `trivia-game-python/`.
- Configuración de entorno virtual y paquetes base (`fastapi`, `uvicorn`, `asyncpg`).
- Se crearon los archivos `Dockerfile` y `docker-compose.yml`.
- Se inicializó el repositorio con Git y se agregó `.gitignore`.

---

## Día 2 - Implementación de la clase Question y pruebas unitarias

### Actividades:
- Se implementó la clase `Question` con los métodos `__init__()` e `is_correct()`.
- Se creó el archivo `test_trivia.py` y se añadieron pruebas con `pytest`.
- Validación del correcto funcionamiento del modelo de pregunta.

---

## Día 3 - Clase Quiz y flujo básico del juego


### Actividades:
- Se creó la clase `Quiz` para gestionar una lista de preguntas.
- Se implementaron los métodos `add_question()` y `get_next_question()`.
- Se programó la función `run_quiz()` para mostrar preguntas en consola.
- Simulación de juego básico sin puntuación.

---

## Día 4 - Sistema de puntuación, manejo de rondas y finalización del juego


### Actividades:
- Se ampliaron los atributos de la clase `Quiz`: `correct_answers` e `incorrect_answers`.
- Se añadió el método `answer_question()` para actualizar la puntuación del jugador.
- Se modificó `run_quiz()` para manejar 10 rondas de preguntas.
- Se generó un resumen final con el puntaje total.
- Se añadieron pruebas unitarias para verificar la lógica de puntuación.

## Día 5 - Mejora de interfaz de usuario y refinamientos

### Actividades:
- Se mejoró la presentación en consola con mensajes de bienvenida y guía al jugador.
- Se actualizó la función `run_quiz()` para mostrar instrucciones claras antes de iniciar.
- Se incorporó un resumen final más detallado al finalizar el juego.
- Se dejó preparado el espacio para incluir niveles de dificultad mas adelante.
---

## Día 6 - Configuración de CI/CD y pruebas de integración

### Actividades:
- Se creó el directorio `.github/workflows/` y el archivo `ci.yml` para configurar GitHub Actions.
- El pipeline ejecuta automáticamente `pytest` en cada push o pull request a las ramas `develop` y `main`.
- Se instalaron y agregaron `pytest` y `httpx` en `requirements.txt` para soportar las pruebas automatizadas.
- Se creó el archivo `tests/integration/test_api.py` para verificar que el endpoint raíz (`/`) de FastAPI responde correctamente.
- Se validó localmente el funcionamiento correcto de todas las pruebas (`4 passed`).
- Se creó la rama `feature/ci-cd-integration` y se etiquetó el avance con `v1.0-day6`.

