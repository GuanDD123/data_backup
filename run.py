import subprocess
from typing import Literal
from rich.prompt import Prompt
from rich import print
from textwrap import dedent
from json import load
from pathlib import Path

from upload import Upload


def sync() -> None:
    for script in (str(Path(__file__).with_name('sync_system.sh')),
                   str(Path(__file__).with_name('sync_person.sh'))):
        subprocess.run(['bash', script])


def upload(dir_dict: dict[str, str] | dict[str, set[str]], value_type: Literal['set', 'str']) -> None:
    instance = Upload(dir_dict, value_type)
    instance.run()


def run():
    dir_dict_file = str(Path(__file__).with_name('dir_dict.json'))
    tips = dedent(
        f'''
        {'='*25}
        1. 备份文件
        {'='*25}
        2. 上传全部文件到云盘
        {'='*25}
        3. 修改配置文件(Linux)
        4. 批量上传到云盘（配置文件）
        {'='*25}
        '''
    )
    print(f'[bright_cyan]{tips}')

    while (mode := Prompt.ask(f'[bright_cyan]请选择运行模式', choices=['q', '1', '2', '3', '4'])) != 'q':
        match mode:
            case '1':
                sync()

            case '3':
                try:
                    subprocess.run(['xdg-open', dir_dict_file])
                    input()
                except:
                    pass

            case '2':
                with open(dir_dict_file, encoding='utf-8') as f:
                    dir_dict = load(f)['default_config']
                    value_type = 'str'
                    upload(dir_dict, value_type)
            case '4':
                with open(dir_dict_file, encoding='utf-8') as f:
                    dir_dict = load(f)['person_config']
                    value_type = 'str'
                upload(dir_dict, value_type)


if __name__ == '__main__':
    run()
