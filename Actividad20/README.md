
# Actividad: Infraestructura como código local con Terraform

**Fase0**

- Revisar el estructura modular del proyecto

![Descripción](Imagenes/fot1.png)

- Verificar ejecucion 

![Descripción](Imagenes/fot2.png)

- Se generaron 10 entornos

![Descripción](Imagenes/fot3.png)

- verificacion de ejecucion del entorno

![Descripción](Imagenes/fot4.png)


**Fase 1**

Se genera el entorno `app1` mediante el script `generate_envs.py`.

Luego en `environments/app1`, se ejecuta el comando `terraform init` para inicializar el backend de Terraform y descargar los proveedores necesarios.

```bash
cd environments/app1
terraform init
```

![Descripción](Imagenes/fot4.png)

Al completarse la inicialización sin errores, se ejecuta el comando `terraform plan` para verificar qué acciones realizará Terraform sobre la infraestructura declarada en `main.tf.json`.

```bash
terraform plan
```


Terraform indica que se creará el recurso `null_resource.app1`, con los siguientes triggers:

* `"name" = "app1"`
* `"network" = "net1"`

Esto confirma que los archivos fueron generados correctamente y que la infraestructura está lista para aplicarse.

![Descripción](Imagenes/fot5.png)


**Fase 2**


Se simula un cambio manual fuera del flujo de infraestructura como código, 
```json
el siguiente
"name": "app2"
por
"name": "hacked-app"
```
![Descripción](Imagenes/fot6.png)

Este tipo de modificación representa un **drift** ya que altera el estado real sin modificar la fuente original 
Luego se ejecuta:

```bash
terraform plan
```
![Descripción](Imagenes/fot7.png)
Terraform detecta la discrepancia entre el estado deseado y el estado real y propone revertir el cambio:

Al aplicar el plan con:

```bash
terraform apply
```
![Descripción](Imagenes/fot8.png)

Terraform restaura el valor original de `"name": "app2"`, demostrando su capacidad de ralizar el camboi.