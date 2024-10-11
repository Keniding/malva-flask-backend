import os

# Obtiene la ruta del directorio donde se encuentra el script
root = os.path.dirname(os.path.realpath(__file__))

# Lista de carpetas a crear
folders = [
    r"app",
    r"app\models",
    r"app\controllers",
    r"app\services",
    r"app\routes",
    r"config",
    r"database",
    r"utils"
]

# Crear las carpetas
for folder in folders:
    os.makedirs(os.path.join(root, folder), exist_ok=True)

# Lista de archivos a crear
files = [
    r"app\__init__.py",
    r"app\models\__init__.py",
    r"app\models\reserva.py",
    r"app\controllers\__init__.py",
    r"app\controllers\reserva_controller.py",
    r"app\services\__init__.py",
    r"app\services\reserva_service.py",
    r"app\routes\__init__.py",
    r"app\routes\reserva_routes.py",
    r"config\__init__.py",
    r"config\config.py",
    r"database\db.py",
    r"utils\__init__.py",
    r"run.py"
]

# Crear los archivos
for file in files:
    with open(os.path.join(root, file), 'w') as f:
        pass  # Solo crea el archivo vacío

print("Estructura de proyecto creada con éxito.")
