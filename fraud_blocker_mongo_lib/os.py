import os


def join_paths(paths):
    if not isinstance(paths, list):
        raise ValueError(f"Pass a list(). {type(paths)} passed instead.")
    elif len(paths) <= 1:
        raise ValueError(f"List with at least 2 paths is needed. Passed a list with {len(paths)} instead")
    else:
        path = paths[0]
        paths_lenght = len(paths)
        for index in range(paths_lenght):
            if index + 1 == paths_lenght: break
            path = os.path.join(path, paths[index + 1])
        return path


class Directory:
    def __init__(self, __file__):
        self.__file__ = __file__
        self.THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.DATA_DIR = os.path.join(os.path.join(self.BASE_DIR, 'data'))

    def __str__(self):
        return f'''Directory(__file__ = {self.__file__},
        THIS_DIR = {self.THIS_DIR},
        BASE_DIR = {self.BASE_DIR},
        DATA_DIR = {self.DATA_DIR})'''


class MainDir(Directory):
    def __init__(self, __file__):
        self.__file__ = __file__
        self.THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        self.BASE_DIR = self.THIS_DIR
        self.DATA_DIR = os.path.join(os.path.join(self.BASE_DIR, 'data'))