from pathlib import Path


class FindDir():

    def __init__(self, last_modify_time: float = None, dir_dict_find_modify: dict[str, str] = {}) -> None:
        '''默认自动获取文件的最近一次修改时间'''
        self.dir_dict_find_modify = dir_dict_find_modify
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time
        else:
            self.last_modify_time = self._get_last_modify_time()

    def run(self) -> None:
        self.dir_dict = {}
        for url, dir in self.dir_dict_find_modify.items():
            self.dir_dict[url] = set()
            self._generate_dir_dict(Path(dir), url)
            print()

    def _get_last_modify_time(self) -> float:
        last_modify_time_dict = {}
        for _, dir in self.dir_dict_find_modify.items():
            dirpath = Path(dir)
            last_modify_time_dict[dir] = max(dirpath.stat().st_mtime,
                                             max((path.stat().st_mtime for path in dirpath.rglob('*')), default=None))
        return max(last_modify_time_dict.values())

    def _generate_dir_dict(self, path: Path, url: str) -> None:
        if str(path.name) == 'd':
            for path_child in path.iterdir():
                if self._check_time(path_child):
                    self.dir_dict[url].add(str(path_child.absolute()))
        else:
            for path_child in path.iterdir():
                if path_child.is_file() and self._check_time(path_child):
                    self.dir_dict[url].add(str(path_child.absolute()))

    def _check_time(self, path: Path) -> bool:
        if path.stat().st_mtime >= self.last_modify_time:
            print(f'\033]8;;file://{path.parent if path.is_file() else path}\033\\{path}\033]8;;\033\\')
            return True
        return False
