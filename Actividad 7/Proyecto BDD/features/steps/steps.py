from behave import given, when, then
import re
import random 

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return float(palabra)
    except ValueError:
        numeros = {
            # Español
            "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4,
            "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
            "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
            "veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
            "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "media": 0.5,
            # Ingles
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
            "fifteen": 15, "twenty": 20, "thirty": 30, "forty": 40,
            "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
            "half": 0.5
        }
        return numeros.get(palabra.lower(), 0)





@given('que he comido {cukes:g} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        context.belly.comer(cukes)
    except ValueError as e:
        context.error = str(e)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    raw = time_description.strip('"').lower()
    time_description = raw
    time_description = time_description.replace(' y ', ' ')
    time_description = time_description.replace(' and ', ' ')
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()

    if "un tiempo aleatorio entre" in raw:
        match = re.match(r'un tiempo aleatorio entre\s+(\d+(?:\.\d+)?)\s+y\s+(\d+(?:\.\d+)?)\s+horas?',raw)
        if match:
            min_horas = float(match.group(1))
            max_horas = float(match.group(2))

            random.seed(42)  # semilla fija para CI
            tiempo_random = random.uniform(min_horas, max_horas)
            print(f"[DEBUG] Tiempo aleatorio elegido: {tiempo_random:.2f} horas")

            context.belly.esperar(tiempo_random)
            return


    if time_description in ['media hora', 'half hour']:
        total_time_in_hours = 0.5
    else:
        pattern = re.compile(
            r'(?:(\w+)\s*(?:hora|horas|hour|hours))?\s*'
            r'(?:(\w+)\s*(?:minuto|minutos|minute|minutes))?\s*'
            r'(?:(\w+)\s*(?:segundo|segundos|second|seconds))?')


        match = pattern.fullmatch(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería ocurrir un error de cantidad negativa.')
def step_then_error_pepinos(context):
    assert hasattr(context, 'error') and "no se puede comer" in context.error.lower()
