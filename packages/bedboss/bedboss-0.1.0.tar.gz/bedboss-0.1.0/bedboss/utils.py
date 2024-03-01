import os
import logging
import urllib.request
import re
from bbconf import BedBaseConf


_LOGGER = logging.getLogger("bedboss")


def extract_file_name(file_path: str) -> str:
    """
    Extraction bed file name from file path (Whether it is .bed or .bed.gz)
    e.g. /path/to/file_name.bed.gz -> file_name

    :param file_path: full file path
    :return: file name without extension
    """
    file_name = os.path.basename(file_path)
    if file_name.split(".")[-1] == "gz":
        file_name = file_name.split(".")[0:-2]

    else:
        file_name = file_name.split(".")[0:-1]
    file_name = re.sub("[^A-Za-z0-9]+", "_", "_".join(file_name))
    return file_name


def standardize_genome_name(input_genome: str) -> str:
    """
    Standardizing user provided genome

    :param input_genome: standardize user provided genome, so bedboss know what genome
    we should use
    :return: genome name string
    """
    input_genome = input_genome.strip()
    # TODO: we have to add more genome options and preprocessing of the string
    if input_genome == "hg38" or input_genome == "GRCh38":
        return "hg38"
    elif input_genome == "hg19" or input_genome == "GRCh37":
        return "hg19"
    elif input_genome == "mm10":
        return "mm10"
    # else:
    #     raise GenomeException("Incorrect genome assembly was provided")
    else:
        return input_genome


def download_file(url: str, path: str, no_fail: bool = False) -> None:
    """
    Download file from the url to specific location

    :param url: URL of the file
    :param path: Local path with filename
    :param no_fail: If True, do not raise exception if download fails
    :return: NoReturn
    """
    _LOGGER.info(f"Downloading remote file: {url}")
    _LOGGER.info(f"Local path: {os.path.abspath(path)}")
    try:
        urllib.request.urlretrieve(url, path)
        _LOGGER.info("File downloaded successfully!")
    except Exception as e:
        _LOGGER.error("File download failed.")
        if not no_fail:
            raise e
        _LOGGER.error("File download failed. Continuing anyway...")


def check_db_connection(bedbase_config: str) -> bool:
    """
    Check if the database connection is working

    :param bedbase_config: path to the bedbase config file
    :return: True if connection is successful, False otherwise
    """
    _LOGGER.info("Checking database connection...")
    if not os.path.exists(bedbase_config):
        raise FileNotFoundError(f"Bedbase config file {bedbase_config} was not found.")
    else:
        _LOGGER.info(f"Bedbase config file {bedbase_config} was found.")
    try:
        BedBaseConf(bedbase_config)
        _LOGGER.info("Database connection is successful.")
        return True
    except Exception as e:
        _LOGGER.error(f"Database connection failed. Error: {e}")
        return False


def convert_unit(size_in_bytes: int) -> str:
    """
    Convert the size from bytes to other units like KB, MB or GB

    :param int size_in_bytes: size in bytes
    :return str: File size as string in different units
    """
    if size_in_bytes < 1024:
        return str(size_in_bytes) + "bytes"
    elif size_in_bytes in range(1024, 1024 * 1024):
        return str(round(size_in_bytes / 1024, 2)) + "KB"
    elif size_in_bytes in range(1024 * 1024, 1024 * 1024 * 1024):
        return str(round(size_in_bytes / (1024 * 1024))) + "MB"
    elif size_in_bytes >= 1024 * 1024 * 1024:
        return str(round(size_in_bytes / (1024 * 1024 * 1024))) + "GB"
