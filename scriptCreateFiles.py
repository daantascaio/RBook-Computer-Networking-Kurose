from pathlib import Path

FILE_DEST = Path(
    'C:\\Users\\caio.dantas\\Desktop\\RBook-Computer-Networking-Kurose\\fixation_exercises\\ch_01')


for i in range(3, 6):
    name_file = FILE_DEST / f"e_{i:03d}.md"
    with open(name_file, 'a') as file:
        lines = ['###\n', '\n', '#\n']
        file.writelines(lines)
