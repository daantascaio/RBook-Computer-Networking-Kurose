from pathlib import Path

FILE_DEST = Path(__file__).parent / 'fixation_exercises' / 'ch_01'


for i in range(0, 29):
    name_file = FILE_DEST / f"e_{i:03d}.md"
    with open(name_file, 'a') as file:
        lines = ['###\n', '\n', '#\n']
        file.writelines(lines)
