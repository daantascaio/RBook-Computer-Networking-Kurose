from pathlib import Path

FILE_DEST = Path(__file__).parent


for i in range(1, 35):
    name_file = FILE_DEST / f"p_{i:03d}.md"
    with open(name_file, 'a') as file:
        lines = ['###\n', '\n', '#\n']
        file.writelines(lines)
