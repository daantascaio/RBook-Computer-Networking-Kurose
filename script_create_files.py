from pathlib import Path

FILE_DEST = Path(__file__) # not complete
    


for i in range(20, 29):
    name_file = FILE_DEST / f"e_{i:03d}.md"
    with open(name_file, 'a') as file:
        lines = ['###\n', '\n', '#\n']
        file.writelines(lines)
