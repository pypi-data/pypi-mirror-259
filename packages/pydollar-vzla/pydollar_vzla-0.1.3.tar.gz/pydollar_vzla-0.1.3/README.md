
# PyDollar_VZLA: Obtención de Precios del Dólar en Venezuela

![Python](https://img.shields.io/badge/Lenguaje-Python-blue)
![Web Scraping](https://img.shields.io/badge/Tecnología-Web%20Scraping-green)
![BeautifulSoup](https://img.shields.io/badge/Tecnología-BeautifulSoup-orange)
![Requests](https://img.shields.io/badge/Tecnología-Requests-red)

---

## Descripción

Esta es una librería en Python diseñada para obtener de manera eficiente y confiable el precio del dólar en Venezuela desde múltiples fuentes. Desarrollada con el propósito de ofrecer una herramienta versátil y fácil de usar, la librería cuenta con la capacidad de extraer información de diversas páginas web utilizando técnicas de web scraping, combinando las potentes capacidades de BeautifulSoup y Requests para garantizar la precisión de los datos obtenidos.

## Características Principales

- **Obtención de Datos desde Múltiples Fuentes:** Actualmente, la librería ofrece la capacidad de obtener el precio del dólar en Venezuela desde tres fuentes diferentes, lo que asegura una mayor robustez y fiabilidad en los datos recolectados.
- **Modularidad y Escalabilidad:** Diseñada con un enfoque modular, esta librería está preparada para la incorporación de nuevas fuentes de información en el futuro, lo que garantiza su escalabilidad y adaptabilidad a medida que evolucionan las necesidades del usuario.
- **Fácil Integración:** Gracias a su interfaz intuitiva y sencilla, la librería puede ser fácilmente integrada en proyectos existentes con un mínimo esfuerzo de desarrollo, lo que la convierte en una solución atractiva y práctica para desarrolladores de todos los niveles de experiencia.

## Tasas soportadas

1. MonitorDolar
2. DolarToday
3. BCV

## Instalación

Para instalar la librería abra una shell interactiva y ejecute:

```bash
   pip install pydollar-vzla
```
---

## Uso

```bash
   from pydollar_vzla.dolar_price import DolarPrice

   # Crear una instancia de PyDollar
   pydollar = DolarPrice()

   # Obtener el precio del dólar de una fuente específica
   dollar_prices = pydollar.get_all_dolar_prices()
   print("Dollar prices:", dollar_prices)

```

## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a PyDollar, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/feature_name).
3. Realiza tus cambios y documenta tus adiciones.
4. Haz commit de tus cambios (git commit -am 'Añadir nueva característica').
5. Haz push a la rama (git push origin feature/feature_name).
6. Abre un Pull Request.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo a través de [vila.antoniojose@gmail.com](mailto:vila.antoniojose@gmail.com).

¡Gracias por tu interés en mi trabajo
