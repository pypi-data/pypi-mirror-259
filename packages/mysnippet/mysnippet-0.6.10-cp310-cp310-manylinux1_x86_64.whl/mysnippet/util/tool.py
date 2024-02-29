import os
import sys
import copy
import stat
import shutil
import logging
import contextlib

from pathlib import Path


def configure_logger(stream_level:str='INFO'):
    LOG_LEVELS = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
    }

    LOG_FORMATS = {
        'DEBUG': '%(levelname)s %(name)s: %(message)s',
        'INFO': '%(levelname)s: %(message)s',
    }

    logger = logging.getLogger("mysnippet")
    logger.setLevel(logging.DEBUG)

    # Remove all attached handlers, in case there was
    # a logger with using the name 'cookiecutter'
    del logger.handlers[:]

    # Get settings based on the given stream_level
    log_formatter = logging.Formatter(LOG_FORMATS[stream_level])
    log_level = LOG_LEVELS[stream_level]

    # Create a stream handler
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)

    return logger



def rmtree(path):
    def _force_delete(_func, _path, _exc_info):
        os.chmod(_path, stat.S_IWRITE)
        _func(_path)
    shutil.rmtree(path, onerror=_force_delete)


def make_sure_path_exists(path: "os.PathLike[str]") -> None:
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except OSError as error:
        raise OSError(f'Unable to create directory at {path}') from error


def make_executable(script_path):
    status = os.stat(script_path)
    os.chmod(script_path, status.st_mode | stat.S_IEXEC)


@contextlib.contextmanager
def work_in(dirname=None):
    cur_dir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(cur_dir)


class ContextImportRepo2Path:
    def __init__(self, repo_dir):
        self._repo_dir = repo_dir
        self._path = None

    def __enter__(self):
        self._path = copy.copy(sys.path)
        sys.path.append(self._repo_dir)

    def __exit__(self, type, value, traceback):
        sys.path = self._path