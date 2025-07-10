# 🚖 Urban Routes - Proyecto de Automatización QA

Este repositorio contiene un conjunto de pruebas automatizadas para validar el flujo principal de la aplicación web **Urban Routes**, desarrolladas utilizando `Selenium WebDriver`, `Pytest` y el patrón de diseño **Page Object Model (POM)**.

---

## 📌 Descripción del Proyecto

La aplicación **Urban Routes** permite a los usuarios solicitar un taxi agregando diferentes preferencias, como el tipo de tarifa, número de teléfono, métodos de pago, solicitudes adicionales y más.

Este proyecto automatiza todo el flujo de reserva de un taxi, validando la correcta funcionalidad de cada paso del proceso.

---

## ⚙️ Tecnologías Utilizadas

- 🐍 Python 3.11+
- 🧪 Pytest
- 🌐 Selenium WebDriver
- 💡 Page Object Model (POM)
- 🔧 WebDriverWait (esperas explícitas)
- 📦 Virtualenv (entorno virtual)

---

## 🚀 Instrucciones para Ejecutar

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/urban-routes-qa.git
   cd urban-routes-qa
   
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt

3. Ejecuta los tests:

   ```bash
   pytest tests/

## 📋 Pruebas Automatizadas Incluidas   

   | Prueba                               | Descripción                                          |
   | ------------------------------------ | ---------------------------------------------------- |
   | ✅ `test_set_route`                   | Ingresar direcciones de origen y destino             |
   | ✅ `test_select_comfort_tariff`       | Selección de tarifa "Comfort"                        |
   | ✅ `test_add_phone_number`            | Ingreso y verificación de número de teléfono por SMS |
   | ✅ `test_add_card_number`             | Agregar tarjeta de crédito con validación del botón  |
   | ✅ `test_write_message_to_driver`     | Enviar mensaje al conductor                          |
   | ✅ `test_order_a_blanket_and_tissues` | Solicitar manta y pañuelos                           |
   | ✅ `test_order_2_ice_creams`          | Agregar 2 helados como extra                         |
   | ✅ `test_the_cab_search_mode_appears` | Finalizar solicitud y buscar conductor               |
   
## 👨‍💻 Autor
Benjamín Vera - QA Engineer en formación 🚀

Proyecto realizado en el bootcamp TripleTen


   
