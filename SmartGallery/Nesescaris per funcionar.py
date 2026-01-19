import os
import subprocess
import sys
errordep = ""
errorpip = ""
# ------------------------------
# Funcions útils
# ------------------------------

def run(cmd):
    """Executa una comanda al terminal i mostra sortida."""
    print(f"\n➡ Executant: {cmd}")
    process = subprocess.Popen(cmd, shell=True)
    process.communicate()


def pip_install(*modules):
    """Instal·la un o més paquets Python via pip."""
    cmd = [sys.executable, "-m", "pip", "install"] + list(modules)
    print(f"\n📦 Instal·lant: {' '.join(modules)}")
    subprocess.check_call(cmd)


# ------------------------------
# 1. Actualitzar pip
# ------------------------------

print("\n==============================")
print("🔧 Actualitzant pip…")
print("==============================")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
except Exception as e:
    errorpip = e

# ------------------------------
# 2. Instal·lar dependències del projecte
# ------------------------------

modules = [
    "rawpy",
    "imageio",
    "pillow",
    "piexif",
    "numpy",
    "scikit-learn",
    "opencv-python",
    "tensorflow",
    "torch",
    "ultralytics",
    "matplotlib",
]

print("\n==============================")
print("📦 Instal·lant dependències del SmartGallery")
print("==============================")

for m in modules:
    try:
        pip_install(m)
    except Exception as e:
        errordep = e
        print(f"❌ No s'ha pogut instal·lar {m}: {e}")

# ------------------------------
# 4. Missatge final
# ------------------------------


if errordep or errorpip == True:
    print(f"Ha fallat: {errordep} o {errorpip}")
else:
    print("\n=======================================")
    print("🎉 Instal·lació COMPLETADA amb èxit!")
    print("Ja pots executar SmartGallery 🚀")
    print("=======================================")