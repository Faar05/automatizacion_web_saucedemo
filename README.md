# 🧪 Automatización de Pruebas Web – SauceDemo

Este proyecto fue desarrollado como práctica para fortalecer mis conocimientos en **automatización de pruebas funcionales** utilizando **Python, Selenium y Pytest**.

Automatiza el flujo completo de **inicio de sesión, agregado de productos al carrito y validación de los mismos** en la aplicación de prueba [Sauce Demo](https://www.saucedemo.com/).

---

## 📋 Descripción del proyecto

El test automatizado realiza las siguientes acciones paso a paso:

1. Abrir el sitio de Sauce Demo.  
2. Iniciar sesión con credenciales válidas (`standard_user` / `secret_sauce`).  
3. Agregar productos al carrito de compras.  
4. Acceder al carrito.  
5. Verificar que los productos agregados estén presentes.  
6. Tomar capturas de pantalla en cada etapa del proceso.

Este flujo reproduce una **prueba funcional de regresión**, validando que el comportamiento del sistema sea el esperado ante distintas interacciones del usuario.

---

## ⚙️ Tecnologías utilizadas

- 🐍 Python 3.13  
- 🌐 Selenium WebDriver  
- 🧩 Pytest  
- ⚡ WebDriver Manager  
- 💻 Google Chrome  
- 🖼️ Capturas automáticas con `save_screenshot`  

---

## 🗂️ Estructura del proyecto
automatizacion_web/
├─ pages/ # Clases que representan páginas
│ ├─ cart_page.py
│ └─ otra_pagina.py
├─ tests/ # Carpeta con todos los tests
│ ├─ init.py
│ └─ test_login_carrito.py
├─ utils/ # Funciones de ayuda, utilidades y capturas
│ ├─ init.py
│ └─ helpers.py
├─ conftest.py # Fixtures globales (driver, setup/teardown)
├─ README.md
└─ requirements.txt

---

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd AUTOMATIZACION_WEB_SAUCEDEMO

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta los tests:
   ```bash
   pytest tests/test_login_carrito.py
   ```

