import pathlib
path=pathlib.Path()
path.rmdir()
for file in path.glob("*.py"):
    print(file)