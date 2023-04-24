from cx_Freeze import setup, Executable
base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "pygame"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name = "Space Invaders",
    options = options,
    version = "2.4",
    description = 'Voici le jeu space invaders, réalisé dans le cadre de la NSI avec Nathanael, Matthias, Lucas & Hugo',
    executables = executables
)