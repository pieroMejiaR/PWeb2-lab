<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Django</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>07</td><td>AÑO LECTIVO:</td><td>2023</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>4-July-2023</td><td>FECHA FIN:</td><td>14-July   -2023</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">RECURSOS:
    <ul>
        <li>https://www.w3schools.com/python/python_reference.asp</li>
        <li>https://docs.python.org/3/tutorial/</li>
        <li>https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models</li>
        <li>https://tutorial.djangogirls.org/es/django_models/</li>
        <li>https://pear.php.net/manual/en/standards.php</li>
        <li>https://docs.djangoproject.com/en/4.0/</li>
        <li>https://www.youtube.com/watch?v=M4NIs4BM1dk</li>
        <li>https://pypi.org/</li>
        <li>https://pip.pypa.io/en/latest/user_guide/</li>
        <li>https://packaging.python.org/en/latest/tutorials/installing-packages/</li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Anibal Sardon</li>
</ul>
</td>
</<tr>
<tr><td colspan="6">Estudiante:
<ul>
<li>Piero Douglas Mejia Ramos - pmejia@unsa.edu.pe</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

# Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

#

## OBJETIVOS TEMAS Y COMPETENCIAS

### OBJETIVOS

-   Crear un Proyecto Django dentro de un entorno virtual.

### TEMAS
-   Entorno virtual
-   Django
-   Modelos
-   Migraciones
-   Panel de administración

<details>
<summary>COMPETENCIAS</summary>

- C.c Diseña responsablemente sistemas, componentes o procesos para satisfacer necesidades dentro de restricciones realistas: económicas, medio ambientales, sociales, políticas, éticas, de salud, de seguridad, manufacturación y sostenibilidad.
- C.m Construye responsablemente soluciones siguiendo un proceso adecuado llevando a cabo las pruebas ajustada a los recursos disponibles del cliente.
- C.p Aplica de forma flexible técnicas, métodos, principios, normas, estándares y herramientas de ingeniería necesarias para la construcción de software e implementación de sistemas de información.

</details>

## CONTENIDO DE LA GUÍA
-  Implementar una aplicación en Django utilizando una plantilla profesional.
-  Utilizar una tabla de Destinos turísticos para leer y completar la página web.
-  Utilizar los tags “if” y “for” en los archivos html para leer todos los registros de
una tabla desde una base de datos.
### MARCO CONCEPTUAL

-  Un framework es una abstracción en la cual se puede reusar código y funcionalidades
adaptándolos a nuestras necesidades.
-  Un modelo en un framework se suele referir a los datos y su organización
-  Una vista permite apreciar el resultado de la lectura de una tabla incluida en una página
web.


## EJERCICIOS PROPUESTOS

Reproducir las actividades de los videos donde trabajamos:
1. Relación de uno a muchos
2. Relación muchos a muchos
3. Impresión de pdfs 
4. Envio de emails

Crear su video Flipgrid: con Git es obligatorio. Revisa el avance de la
teoría Django parte4

## Commits

<img src="./img/commits-2.png" style="width:50%; height:auto"/>

<img src="./img/commits-1.png" style="width:50%; height:auto"/>


## Explicando las modelos que se usaran para la aplicacion

En este laborotario se usaran 3 aplicaciones: una para la parte de relaciones de uno a muchos y de muchos a muchos; otra para crear PDF con django y la ultima para enviar emails.

- Aplicacion 1:

<img src="./img/model-pdf.png" style="width:50%; height:auto"/>

El modelo render_to_pdf es  una función o método personalizado que se utiliza para generar un archivo PDF a partir de un archivo HTML. En general, este modelo se encarga de realizar la conversión del HTML al formato PDF utilizando una biblioteca o herramienta externa, como WeasyPrint o ReportLab.

- Aplicacion 2:

<img src="./img/email-view.png" style="width:50%; height:auto"/>

El método send_email en views.py es un controlador de vista que se utiliza para procesar el formulario de envío de correo electrónico

Primero, se verifica si la solicitud es de tipo POST utilizando el condicional if request.method == 'POST'.

Si la solicitud es de tipo POST, se crea una instancia del formulario EmailForm utilizando los datos enviados en la solicitud (request.POST).

A continuación, se verifica si el formulario es válido utilizando el método is_valid() del formulario. Si el formulario no es válido, se renderiza la plantilla send_email.html nuevamente con el formulario y se muestra cualquier error de validación.

Luego, se crea un objeto EmailMessage utilizando los datos extraídos. Se establecen el remitente, el destinatario, el asunto y el contenido del correo electrónico.

Se envía el correo electrónico utilizando el método send() del objeto EmailMessage.

Si el correo electrónico se envía correctamente, se redirige al usuario a la página email_sent.html, que muestra un mensaje de confirmación.

<img src="./img/email-form.png" style="width:50%; height:auto"/>

Se usa el template send_email.html para pedir los datos que se necesitan para el email, se uso de un form

## Evidencia de los ejercicios resueltos

- Usando la aplicacion de crear PDF con Django

<img src="./img/generate-pdf.png" style="width:50%; height:auto"/>

Esta clase se utiliza para procesar una solicitud POST y generar el PDF correspondiente en función de los datos proporcionados en el formulario. Luego, el PDF se devuelve como respuesta HTTP al cliente.

<img src="./img/mostrar-pdf.png" style="width:50%; height:auto"/>

Aqui se muestra como quedaria el PDF

<img src="./img/descargar-pdf.png" style="width:50%; height:auto"/>

De la misma manera tambien se pueden descargar

-Enviando un email

<img src="./img/email-prueba.png" style="width:50%; height:auto"/>

Aqui se llenara el formulario con los campos necesarios para enviar un email

<img src="./img/email-enviado.png" style="width:50%; height:auto"/>

Este es el mensaje de confirmación de eviar el email

## REFERENCIAS
-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/
-   https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models
-   https://tutorial.djangogirls.org/es/django_models/
-   https://pear.php.net/manual/en/standards.php
-   https://docs.djangoproject.com/en/4.0/
-   https://www.youtube.com/watch?v=M4NIs4BM1dk
-   https://pypi.org/
-   https://pip.pypa.io/en/latest/user_guide/
-   https://packaging.python.org/en/latest/tutorials/installing-packages/

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
