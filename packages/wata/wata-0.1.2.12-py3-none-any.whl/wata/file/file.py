from wata.file.utils import utils, file_tree_utils # 不能去掉
from pathlib import Path


class FileProcess:

    @staticmethod
    def load_file(path):
        utils.load_file(path)

    @staticmethod
    def save_file(data, save_path):
        utils.save_file(data, save_path)

    @staticmethod
    def write_file(data, save_path):
        utils.save_file(data, save_path)

    @staticmethod
    def file_tree(path, save_txt=None):
        file_tree_utils.file_tree(path, save_txt)