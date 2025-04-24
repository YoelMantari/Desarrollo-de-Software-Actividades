

# Actividad 7


## 1. Creación de la estructura del proyecto


La estructura generada del proyecto :

![Descripción](Imagenes/bdd1.png)

En el archivo `features/belly.feature`, se agrega los escenarios en Gherkin, se utilizaron frases en español para simular acciones.

![Descripción](Imagenes/inii2.png)

Se creó la clase `Belly`, encargada de manejar la lógica principal que incluye los métodos como `comer`, `esperar` y `esta_gruñendo`.

![Descripción](Imagenes/ini2.png)


Se agregar el archivo `steps.py` los pasos correspondientes a los escenarios definidos en Gherkin. Cada paso traduce las frases del lenguaje natural a funciones ejecutables. 

![Descripción](Imagenes/ini1.png)

	Se configura este archivo para inicializar una nueva instancia de `Belly` antes de cada escenario, asegurando que cada prueba comience con un estado limpio.
![Descripción](Imagenes/ini3.png)


## 2. Ejecución de las pruebas BDD

Una vez implementados los pasos y la lógica se ejecutan las pruebas:

![Descripción](Imagenes/inii2.png)

Cada escenario Gherkin prueba si el estómago gruñe o no después de comer cierta cantidad de pepinos y esperar un tiempo. Se validan distintos formatos de tiempo: horas, media hora, minutos y frases completas.


## 3. Creacion del pipeline

## Automatización de pruebas con GitHub Actions

Se configuró un flujo de trabajo automatizado utilizando GitHub Actions el cual se encarga de ejecutar tanto las pruebas unitarias con `pytest` como las pruebas BDD con `behave` de manera automática cada vez que se realiza un `push` o `pull request` en el repositorio.

![Descripción](Imagenes/PDU.png)

  - **Nombre del workflow**: Pruebas BDD y Unitarias
  - El flujo se ejecuta automaticamente al hacer `push` o `pull request`, lo que verifica en tiempo real que no rompa ninguna prueba.
  - Se crea un `jobs` llamado test para correr un entorno linux con `ubuntu-latest`.
  - `actions/chechout@v3` descarga el contenido del repositorio para trabajar con el.
  - `python-version: '3.9'` Instala y configura la versión 3.9 de Python para el entorno
  - `Instalar dependencias` desde la carpeta de proyectos se instala todas las dependencias del archivo `requeriments.txt`.
  - `Ejecturar pruebas unitarias`se ejecuta las pruebas unitarias usando pytest.
  - `Ejecturar pruebas BDD`Ejecuta las pruebas BDD escritas en Gherkin a través de `behave`.

## Ejercicio 1
### Añadir soporte para minutos y segundos en tiempos de espera

Se agrega nuevo escenario en la prueba.
   ![Descripción](Imagenes/Eje11.png)

Se modifica `steps.py` la expresion regular para que pueda aceptar segundos 

```python
pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
seconds = convertir_palabra_a_numero(seconds_word)
total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
```
  ![Descripción](Imagenes/Eje12.png)

  - Se crea una prueba unitaria que verifique que el estómago gruñe cuando se comen 35 pepinos y se espera exactamente 1 hora, 30 minutos y 45 segundos
  
  ![Descripción](Imagenes/Eje13.png)

#### Resultados
- Se ejecuta el comando `behave` exitosamente los 6 escenarios, donde cada escenario simula una situación diferente y todos se pasaron,ejecutandose de manera correcta y sin errores.
  
  ![Descripción](Imagenes/pd1.png)

- Se ejecuta el comando `pytest -v`, el resultado fue exitoso, donde el metodo `gruñir` funciona correctamente.

  ![Descripción](Imagenes/pd2.png)

## Ejercicio 2:
## Manejo de cantidades fraccionarias de pepinos

### Añadir soporte para pepinos fraccionarios
Se agrega nuevo escenario en la prueba.
  ```text
    Escenario: Esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir
  ```

  
Se modifica el decorador para que capure un numero entero.
```python
@given('que he comido {cukes:d} pepinos')
```
  ![Descripción](Imagenes/Eje21.png)

  - Se modifica el metodo `comer` de `belly.py` para que no acepte valores negativos.

  ![Descripción](Imagenes/Eje22.png)

  - Se crea una prueba unitaria que verifique que el estómago gruñe cuando se comen 35 pepinos y se espera exactamente 1 hora, 30 minutos y 45 segundos
  
  ![Descripción](Imagenes/Eje23.png)


#### Resultados de las pruebas
  
  ![Descripción](Imagenes/Eje24.png)

  ![Descripción](Imagenes/Eje25.png)

## Ejercicio 3:
## Soporte para idiomas múltiples (Español e Inglés)

**Actualizaciónn del pipeline para aceptar tags en @spannish e @english y ejecturar en etapas diferentes**

 ![Descripción](Imagenes/Eje31.png)

**Se agrega nuevo  un escenario:**

```text
Escenario: Esperar usando horas en inglés
  Dado que he comido 20 pepinos
  Cuando espero "two hours and thirty minutes"
  Entonces mi estómago debería gruñir
```
**Se actualizaron las siguientes funciones para que puedan aceptar horario en ingles y tambien los conectores como  and**

 ![Descripción](Imagenes/Eje32.png)

 ![Descripción](Imagenes/Eje36.png)
#### Resultado al ejecutar behave con en los escenarios solo de ingles y de español
 ![Descripción](Imagenes/Eje37.png)
 ![Descripción](Imagenes/Eje38.png)
  ![Descripción](Imagenes/Eje39.png)

## Ejercicio 4:
## Manejo de tiempos aleatorios

**Se agrega nuevo  un escenario para tiempos aleatorios:**
```text
Escenario: Comer pepinos y esperar un tiempo aleatorio
  Dado que he comido 25 pepinos
  Cuando espero un tiempo aleatorio entre 1 y 3 horas
  Entonces mi estómago debería gruñir
```
**Se actualizaron stesp.py para que pueda aceptar un valor aleatorio dentro de un rango fijando una semilla
que garantiza resultados en CI/CD"**

  ![Descripción](Imagenes/Eje41.png)

#### Resultado

  ![Descripción](Imagenes/Eje42.png)

## Ejercicio5:
## Ejercicio 5: Validación de cantidades no válidas

**Se agrega nuevo  un escenario:**


```text
  @spanish
  Escenario: Manejar una cantidad no válida de pepinos más de 100
    Dado que he comido 120 pepinos
    Entonces debería ocurrir un error de cantidad negativa.
```
  **Se agrega nueva validacion para aceptar solo pepinos en un rango de 0 a 100, si estan fuera de este rango devuelve un mensaje**

  ![Descripción](Imagenes/Eje51.png)

  **Verifica que paso durante el paso `Dado que he comido` y captura si hay un error**

  ![Descripción](Imagenes/Eje52.png)

 **Se agrega una prueba cuando intenta comer 120 pepinos**

   ![Descripción](Imagenes/Eje53.png)

#### Resultado
   ![Descripción](Imagenes/Eje54.png)
   ![Descripción](Imagenes/Eje55.png)

## Ejercicio6:
## Escalabilidad con grandes cantidades de pepinos