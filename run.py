import subprocess
from typing import Literal
from rich.prompt import Prompt
from rich import print
from textwrap import dedent
from json import load
from pathlib import Path

from find_modify_dir import FindDir
from upload import Upload


def sync() -> None:
    for script in ('./sync_system.sh', './sync_person.sh'):
        subprocess.run(['bash', script])


def find_dir() -> dict[str, set[str]]:
    instance = FindDir()
    instance.run()
    return instance.dir_dict


def upload(dir_dict: dict[str, str] | dict[str, set[str]], value_type: Literal['set', 'str']) -> None:
    instance = Upload(dir_dict, value_type)
    instance.run()


def run():
    dir_dict_file = str(Path(__file__).with_name('dir_dict.json'))
    tips = dedent(
        f'''
        {'='*25}
        1. 备份文件并同步到云盘（同步修改）
        2. 修改配置文件(Linux)
        3. 批量上传到云盘（配置文件）
        {'='*25}
        '''
    )
    print(f'[bright_cyan]{tips}')

    while (mode := Prompt.ask(f'[bright_cyan]请选择运行模式', choices=['q', '1', '2', '3'])) != 'q':
        if mode == '1':
            sync()
            dir_dict = find_dir()
            value_type = 'set'
            if Prompt.ask(f'[bright_cyan]是否同步到云盘', choices=['y', 'n'], default='y') == 'y':
                upload(dir_dict, value_type)

        elif mode == '2':
            try:
                subprocess.run(['xdg-open', dir_dict_file])
                input()
            except:
                pass

        else:
            with open(dir_dict_file, encoding='utf-8') as f:
                dir_dict = load(f)
                value_type = 'str'
            upload(dir_dict, value_type)


if __name__ == '__main__':
    run()
