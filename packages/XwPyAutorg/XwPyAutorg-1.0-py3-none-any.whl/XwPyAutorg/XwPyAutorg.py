def autorg():
    from pathlib import Path
    scr_folder = Path(input('输入待整理的路径>>>'))
    des_folder = Path(input('输入输出路径>>>'))
    files = scr_folder.glob('*')
    for i in files:
        if i.is_file():
            des_Path = des_folder / i.suffix.strip('.')
            if not des_Path.exists():
                des_Path.mkdir(parents=True)
            i.replace(des_Path / i.name)
if __name__ == '__main__':
    autorg