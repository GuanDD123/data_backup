from pathlib import Path
from datetime import datetime as Datetime


class FindDir():
    dirpath_str = [
        (
            '/media/sika/Expansion/00_Backup',
            'https://www.123pan.com/?homeFilePath=10798076',
            'https://www.123pan.com/?homeFilePath=10798076,10798077'
        ),
        (
            '/media/sika/Expansion/10_Pictures',
            'https://www.123pan.com/?homeFilePath=10767595',
            'https://www.123pan.com/?homeFilePath=10767595,10767596'
        ),
        (
            '/media/sika/Expansion/20_Music',
            'https://www.123pan.com/?homeFilePath=10767852',
            'https://www.123pan.com/?homeFilePath=10767852,10798471'
        ),
        (
            '/media/sika/Expansion/30_Videos',
            'https://www.123pan.com/?homeFilePath=10799744',
            'https://www.123pan.com/?homeFilePath=10799744,10799746'
        ),
        (
            '/media/sika/Expansion/40_Documents',
            'https://www.123pan.com/?homeFilePath=10767974',
            'https://www.123pan.com/?homeFilePath=10767974,10767975',
        ),
        (
            '/media/sika/Expansion/50_Applications',
            'https://www.123pan.com/?homeFilePath=10769488',
            'https://www.123pan.com/?homeFilePath=10769488,10798588'
        ),
        (
            '/media/sika/Expansion/60_Nutstore',
            'https://www.123pan.com/?homeFilePath=10769603',
            'https://www.123pan.com/?homeFilePath=10769603,10797938',
        ),
        (
            '/media/sika/Expansion/61_Cryptomator',
            'https://www.123pan.com/?homeFilePath=10769646',
            'https://www.123pan.com/?homeFilePath=10769646,10769647'
        )
    ]

    def run(self) -> None:
        self._get_last_modify_time()
        self.dir_dict = {}
        for dirpath, url, url_d in self.dirpath_str:
            self.dir_dict[url] = set()
            self.dir_dict[url_d] = set()
            self._generate_dir_dict(Path(dirpath), url, url_d)
            print()

    def _get_last_modify_time(self) -> None:
        self.last_modify_time = Datetime.fromtimestamp(Path('/media/sika/Expansion').stat().st_mtime)

    def _generate_dir_dict(self, path: Path, url: str, url_d: str) -> None:
        if self._check_time(path):
            if (str(path.parent.parent.absolute()) == '/media/sika/Expansion') and path.is_file():
                self.dir_dict[url].add(str(path.absolute()))
            elif str(path.parent.parent.parent.absolute()) == '/media/sika/Expansion':
                self.dir_dict[url_d].add(str(path.absolute()))
            else:
                for path_child in path.iterdir():
                    self._generate_dir_dict(path_child, url, url_d)

    def _check_time(self, path: Path) -> bool:
        datetime_modify = Datetime.fromtimestamp(path.stat().st_mtime)
        if datetime_modify >= self.last_modify_time:
            print(f'\033]8;;file://{path.parent if path.is_file() else path}\033\\{path}' +
                  f' --- {datetime_modify.strftime('%Y/%m/%d %H:%M:%S')}\033]8;;\033\\')
            return True
        return False


if __name__ == '__main__':
    instance = FindDir()
    instance.run()
    for i, v in instance.dir_dict.items():
        print(i, '------', v)
    input()
