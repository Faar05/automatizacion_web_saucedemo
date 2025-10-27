import os

def capturar(driver, nombre):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    ruta = os.path.join("screenshots", f"{nombre}.png")
    driver.save_screenshot(ruta)
    print(f"Captura tomada: {ruta}")
