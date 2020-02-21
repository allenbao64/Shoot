from cx_Freeze import setup, Executable

include = ["script.txt", "audio", "images", "README.md"]
packages = ["pygame"]

setup(
    name="Shoot",
    options={"build_exe": {"include_files": include, "packages": packages}},
    executables=[Executable("main.py")]
)
