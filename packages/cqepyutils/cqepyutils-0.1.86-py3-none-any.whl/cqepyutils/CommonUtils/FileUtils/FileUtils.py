import os
import shutil
from robot.api import logger


class FileUtils:
    @staticmethod
    def create_folder(path):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def create_subfolders(parent_path, subfolders):
        for subfolder in subfolders:
            subfolder_path = os.path.join(parent_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

    @staticmethod
    def delete_and_create_dir(dir_path: str):
        """
        This method is used to delete existing directory and create new directory based on dir_path
        :param dir_path: r'C://Desktop//Comparison//data//actual//'
        :return:
        """
        logger.info('****************************************************************************************************')
        logger.info('FileUtil - Delete and Create Directory')
        logger.info('****************************************************************************************************')
        logger.info('Step-01 : Verify if the directory already exist if Yes, delete and create the directory')
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        else:
            shutil.rmtree(dir_path)
            os.mkdir(dir_path)
        logger.info('****************************************************************************************************')

