

![Descripción](Imagenes/Eje6_1.png)

### Resolver conflictos en una fusión non-fast-forward

1. Se crea una nueva carpeta y se inicializa un repositorio vacío de Git.

2. Se crea un archivo llamado `index.html` con contenido y se hace un commit en la rama principal `main`.

3. Luego, se crea una nueva rama llamada `feature-update` donde se edita el archivo `index.html` agregando un párrafo y se guarda ese cambio con un commit.

4. Después se regresa a la rama `main` y se hace otra modificación al mismo archivo, esta vez añadiendo un pie de página y se guarda también con otro commit.

5. Al intentar fusionar la rama `feature-update` con la rama `main` usando `git merge --no-ff` Git detecta un conflicto porque ambos cambios se hicieron en el mismo archivo.

6. Se abre el archivo `index.html` y se eliminan las marcas de conflicto. Luego, se combinan los dos cambios manualmente segun nos convenga.

7. Una vez resuelto el conflicto, se guarda el archivo corregido y se agrega al control de cambios y se finaliza la fusión con un commit.

8. Finalmente, se revisa el historial de commits para confirmar que la fusión se realizó correctamente y que se resolvió el conflicto.

---

### Preguntas:

**¿Qué pasos adicionales tomaste para resolver el conflicto?**  
Fue necesario abrir el archivo con conflicto para entender las diferencias entre ambas ramas y asi eliminar las marcas automáticas de Git, se combinar manualmente los cambios y luego hacer un commit adicional para completar el merge.

**¿Qué estrategias pueden ayudarte a evitar conflictos en el futuro?**  
Algunas estrategias son mantener una buena comunicación entre los miembros del equipo o actualizar frecuentemente la rama local con los últimos cambios del repositorio remoto y asi evitar trabajar varios en el mismo archivo o en la misma parte del archivo, y tambien hacer commits pequeños y frecuentes para facilitar el proceso.


