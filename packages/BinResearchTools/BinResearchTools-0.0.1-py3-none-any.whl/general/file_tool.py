import json
import os
from loguru import logger


def check_dir(dir_path):
    """
    check if the dir_path exists and is a directory

    :param dir_path: a directory path
    :return: a normalized and absolute path
    """
    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"Directory not found: {dir_path}, create it first.")
    if not os.path.isdir(dir_path):
        raise NotADirectoryError(f"{dir_path} is not a directory.")
    return os.path.normpath(os.path.abspath(dir_path))


def check_save_path(file_path):
    """
    check if the file_path belongs to a valid dir and has a .json extension
    :param file_path: a file path
    :return: a normalized and absolute path
    """
    dir_path, file_name = os.path.split(file_path)
    dir_path = check_dir(dir_path)

    pure_name, ext = os.path.splitext(file_name)
    if not ext:
        raise ValueError(f"File name should have an extension: {file_name}")

    if ext != '.json':
        raise ValueError(f"File extension should be .json: {file_name}")

    return os.path.join(dir_path, file_name)


def save_as_json(data, file_path, encoding='utf-8', output_log=False):
    """
    save data to a json file
    set output_log to True to print the file path

    :param data:
    :param file_path:
    :param encoding:
    :param output_log:
    :return:
    """
    file_path = check_save_path(file_path)
    logger.info(f"Saving data to {file_path}")
    if output_log:
        logger.info(f"Saving data to {file_path}")
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, indent=4)
    if output_log:
        logger.info(f"Data saved to {file_path}")
