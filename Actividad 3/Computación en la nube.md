## A. Cuestionario

### 1. Motivaciones para la nube

**(a) ¿Qué problemas o limitaciones existían antes del surgimiento de la computación en la nube y cómo los solucionó la centralización de servidores en data centers?**  

Antes de la nube, las empresas gastaban mucho en hardware y no podían escalar rápido. La centralización en data centers (Aws, Azure, GCP) resolvió esto con un modelo de pago por uso y recursos “on-demand”, reduciendo costos y simplificando la gestión.

**(b) ¿Por qué se habla de “The Power Wall” y cómo influyó la aparición de procesadores multi-core en la evolución hacia la nube?**  
 The Power Wall describe la dificultad de subir la frecuencia de CPU sin consumir más energía. Surgieron procesadores multi-core, permitiendo ejecutar muchas VMs o contenedores en un solo servidor donde esto hizo posible la nube escalable y eficiente que conocemos hoy.

---

### 2. Clusters y load balancing

**(a) Explica cómo la necesidad de atender grandes volúmenes de tráfico en sitios web condujo a la adopción de clústeres y balanceadores de carga.**  

Para manejar alto tráfico se agrupan varios servidores en un clúster donde un balanceador de carga reparte las peticiones entre ellos, evitando sobrecarga. En la nube, servicios como AWS, Azure o Google Cloud facilitan esta práctica garantizando mejor disponibilidad y rendimiento.

**(b) Describe un ejemplo práctico de cómo un desarrollador de software puede beneficiarse del uso de load balancers para una aplicación web.**  
Un ejemplo es un servicio de streaming con picos de audiencia. El balanceador redirige el tráfico a servidores adicionales y descarta los fallidos, asegurando respuesta rápida y evitando caídas completas.
### 3. Elastic computing

**(a) Define con tus propias palabras el concepto de Elastic Computing.**  
Es la capacidad de subir o bajar recursos como cpu o ram, sin complicaciones físicas según la demanda de forma casi inmediata.

---

**(b) ¿Por qué la virtualización es una pieza clave para la elasticidad en la nube?**  
Gracias a la virtualización los vms o contenedores se pueden crear o eliminar instancias en segundos. Esto permite a la nube dar recursos y así ahorrar costos o agregar capacidad al instante.


**(c) Menciona un escenario donde, desde la perspectiva de desarrollo, sería muy difícil escalar la infraestructura sin un entorno elástico.**  
Un ejemplo claro es un portal de ventas en Black Friday: sin entornos elásticos, habría que comprar más servidores cuando la demanda esta en su pico, quedando sin uso de ellas luego de terminar. 

---

### 4. Modelos de servicio (IaaS, PaaS, SaaS, DaaS)

**(a)**  
- **IaaS** proporciona infraestructura virtual que el usuario administra.  
- **PaaS** ofrece una plataforma completa para desarrollar y desplegar aplicaciones sin gestionar servidores.  
- **SaaS** entrega software listo para usar vía web.  
- **DaaS** brinda acceso a datos como un servicio.  

Un desarrollador opta por PaaS cuando desea enfocarse solo en el desarrollo de la aplicación, sin encargarse de la infraestructura.

**(b)**  
- **IaaS**: Aws EC2, Azure Virtual Machines, Google Compute Engine  
- **PaaS**: Aws Elastic Beanstalk, Azure App Service, Google App Engine  
- **SaaS**: Microsoft 365, Salesforce, Google Docs  
- **DaaS**: Amazon RDS, Google BigQuery, Azure SQL Database

### 5. Tipos de nubes (Pública, Privada, Híbrida, Multi-Cloud)

**(a) ¿Cuáles son las ventajas de implementar una nube privada para una organización grande?**   
Una nube privada da mayor control, seguridad personalizada y mejor integración con sistemas antiguos. Además, aprovecha el hardware propio y ayuda a cumplir normativas internas.

**(b) ¿Por qué una empresa podría verse afectada por el “provider lock-in”?**  
El provider lock-in ocurre cuando una empresa depende mucho de un solo proveedor y cambiar a otro se vuelve costoso y complicado por las tecnologías específicas usadas.



**(c) ¿Qué rol juegan los “hyperscalers” en el ecosistema de la nube?**  
Los hyperscalers son empresas que ofrecen infraestructura en la nube a gran escala con centros de datos distribuidos en todo el mundo, como Aws, Azure, Google Cloud, y estos dan servicios como cómputo o almacenamiento para que otras empresas puedan crecer y escalar sin tener sus propios servidores.

## B. Actividades de investigación y aplicación


A continuación, se presentan los casos de Netflix y Slack, destacando sus motivaciones, beneficios y desafíos al migrar parte de su infraestructura a la nube:
### 1. Estudio de casos

#### 1. **Netflix**

**Motivaciones**:  
- **Escalabilidad y disponibilidad**: Netflix necesitaba una infraestructura que pudiera manejar el crecimiento explosivo de su base de usuarios y ofrecer una experiencia de streaming sin interrupciones.
- **Innovación y velocidad**: La empresa buscaba acelerar el lanzamiento de nuevas características y contenido, aprovechando la flexibilidad de la nube.

**Beneficios**:  
- **Escalabilidad**: Pudieron expandirse rápidamente a más de 130 países, ofreciendo una experiencia de streaming global sin los limitantes de los centros de datos tradicionales.
- **Disponibilidad**: Mejoraron significativamente la disponibilidad del servicio, reduciendo el tiempo de inactividad.
- **Costos**: Aunque no fue la motivación principal, Netflix logró ahorros de costos gracias a la elasticidad de la nube, evitando costos fijos por infraestructura subutilizada[5].

**Desafíos**:  
- **Complejidad en la migración**: La migración completa a la nube tomó siete años, requiriendo una reestructuración significativa de su arquitectura de aplicaciones[5].
- **Seguridad y cumplimiento**: Asegurar la seguridad y el cumplimiento normativo en un entorno de nube pública fue un desafío continuo[2].

Un caso bien documentado de migración a la nube es el de **IstoÉ**, una reconocida empresa de comunicaciones en Brasil. A continuación, se describe su caso:

**Fuentes**:
https://www.cio.com/article/2072682/tras-diez-anos-netflix-termina-su-migracion-a-la-nube-con-aws.html
https://about.netflix.com/es_es/news/completing-the-netflix-cloud-migration


#### 2. Istoé

**Motivaciones**:  
- **Transformación Digital**: Istoé buscaba modernizar su infraestructura tecnológica para mejorar la eficiencia operativa y ofrecer mejores servicios a sus clientes.
- **Escalabilidad y Flexibilidad**: Necesitaban una infraestructura que pudiera adaptarse rápidamente a las demandas cambiantes del mercado.

**Beneficios**:  
- **Mejora en la eficiencia operativa**: Lograron optimizar sus procesos internos y mejorar la colaboración entre departamentos.
- **Escalabilidad**: Pudieron expandir su capacidad de procesamiento sin necesidad de invertir en hardware adicional.
- **Costos reducidos**: Al migrar a Google Cloud, redujeron significativamente los costos asociados con el mantenimiento de servidores físicos[1].

**Desafíos**:  
- **Complejidad en la migración**: La transición a la nube requirió un proyecto de transformación digital personalizado, que implicó cambios significativos en su infraestructura y procesos.
- **Seguridad y Cumplimiento**: Asegurar la seguridad y el cumplimiento normativo fue un desafío continuo durante la migración.

**Fuente**:
https://www.ipnet.cloud/blog/es/nube-de-google/migracion-a-la-nube-caso-de-exito-istoe/



### 2. Comparativa de modelos de servicio

- **IaaS:** El desarrollador instala el sistema operativo se configura servidores y aplica parches, donde este tiene control total pero también más responsabilidad.  
  Ejemplo: Aws EC2, Azure VMs.

- **PaaS:** El proveedor da una plataforma lista para subir código, este no gestiona la infraestructura solo la app.  
  Ejemplo: Aws Elastic Beanstalk, Azure App Service.

- **SaaS:** El software ya está listo para usar, no se instala nada solo se accede y se usa.  
  Ejemplo: Google Workspace, Office de Microsoft.

**Escalado y seguridad:**  
En IaaS, todo se configura. En PaaS, el proveedor ayuda con el escalado y seguridad base. En SaaS, todo lo gestiona el proveedor.


#### 3. Armar una estrategia multi-cloud o híbrida
En una empresa mediana que tiene parte de su sistema en su propio data center y otra parte en una nube pública como AWS, pero ahora se quiere usar también otro proveedor como Azure para no depender solo de uno, donde se pasaría la mitad de las aplicaciones a Azure, que no estén tan ligadas al sistema principal, para no complicar la conexión entre todo. Entonces la base de datos se dejaria en el data center para tener respaldo por si algo falla. Para la configuración de red se tendria que conectar todo con una Vpn para que las aplicaciones puedan comunicarse entre si.





#### 4. Debate sobre costos
##### **Nube pública**:  
  - **Costos iniciales bajos (OPEX)** y escalabilidad inmediata, pero puede subir con la demanda.  
  - Cumplir normativas requiere configurar servicios específicos como por ejemplo AWS security hub o Azure security center.  
  - Cambiar de proveedor puede ser complejo como se vio (lock-in).

##### **Nube privada**:
  - **Costos iniciales altos (CAPEX)** ya que se adquiere hardware, pero control total de seguridad y datos.  
  - Es más rígida al escalar capacidades limitadas al hardware propio.  
  - Favorece cumplimiento de normativas y alta personalización.

##### **Nube híbrida**:
  - Balance de lo mejor de ambos mundos como flexibilidad y control.  
  - Complejidades de red y administración doble.

##### **Multi-cloud**:
  - Evita dependencia de un solo proveedor y puede optimizar costos usando servicios específicos de cada uno.  
  - Implica manejar múltiples cuentas, facturación y compatibilidades.


#### 1. **Nube Pública**
##### **Pros**:
- **Costos iniciales bajos (OPEX)**: No requiere inversiones iniciales significativas en hardware o infraestructura, ya que se paga por uso.
 -**Flexibilidad y escalabilidad**: Ofrece escalabilidad instantánea según las necesidades del negocio, sin necesidad de infraestructura adicional.
-**Cumplimiento normativo**: Proveedores como AWS, Azure y Google Cloud ofrecen herramientas y servicios para cumplir con normativas como GDPR y HIPAA.

#####**Contras**:
- **Control limitado**: Menor control sobre la infraestructura y los datos, lo que puede ser un problema para datos sensibles.
- **Dependencia del proveedor**: Riesgo de vendor lock-in, lo que complica el cambio a otro proveedor.

#### 2. **Nube Privada**
#####**Pros**:
- **Control total**: Mayor control sobre la infraestructura y los datos, ideal para aplicaciones críticas o datos sensibles.
- **Cumplimiento normativo**: Facilita el cumplimiento de normativas estrictas al mantener los datos en un entorno controlado.

#####**Contras**:
- **Costos iniciales altos (CAPEX)**: Requiere inversiones significativas en hardware y mantenimiento.
- **Limitaciones en escalabilidad**: La escalabilidad es más difícil y costosa que en la nube pública.

#### 3. **Nube Híbrida**
#####**Pros**:
- **Flexibilidad y control**: Combina la escalabilidad de la nube pública con el control de la nube privada.
- **Cumplimiento normativo**: Permite mantener datos sensibles en una nube privada mientras se utilizan recursos públicos para aplicaciones menos críticas.
- **Optimización de costos**: Puede optimizar costos al utilizar la nube pública solo cuando sea necesario.

##### **Contras**:
- **Costos iniciales altos**: Requiere inversión en infraestructura privada y gestión compleja.
- **Complejidad en la gestión**: La integración de entornos privados y públicos puede ser complicada.

#### 4. **Multi-Cloud**
##### **Pros**:
- **Flexibilidad y escalabilidad**: Ofrece acceso a múltiples proveedores, lo que permite aprovechar las fortalezas de cada uno y mitigar riesgos.
- **Evitación del vendor lock-in**: Reduce la dependencia de un solo proveedor, facilitando el cambio entre ellos.
- **Innovación constante**: Acceso a las últimas tecnologías y servicios de diferentes proveedores.

##### **Contras**:
- **Costos iniciales moderados**: Aunque menores que la nube privada, pueden ser más altos que la nube pública debido a la gestión compleja.
- **Gestión compleja**: Requiere herramientas y habilidades especializadas para gestionar múltiples proveedores.

