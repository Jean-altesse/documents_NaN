from pathlib import Path

pt = Path.home().iterdir()

for i in pt:
    if i.is_file():
        print(i)