import time
from utils.helpers import capturar
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_login_y_carrito(driver):
    login = LoginPage(driver)
    inventario = InventoryPage(driver)
    carrito = CartPage(driver)

    # 1. Abrir página
    login.abrir()
    capturar(driver, "1_pagina_abierta")

    # 2. Iniciar sesión
    login.iniciar_sesion("standard_user", "secret_sauce")
    capturar(driver, "2_login_completado")
    time.sleep(2)

    # 3. Agregar productos
    inventario.esperar_carga()
    inventario.agregar_productos()
    capturar(driver, "3_productos_agregados")

    # 4. Ir al carrito
    inventario.ir_al_carrito()
    capturar(driver, "4_carrito_abierto")

    # 5. Verificar productos
    productos = carrito.verificar_productos()
    capturar(driver, "5_verificacion_carrito")

    assert "Sauce Labs Backpack" in productos
    assert "Sauce Labs Bike Light" in productos
