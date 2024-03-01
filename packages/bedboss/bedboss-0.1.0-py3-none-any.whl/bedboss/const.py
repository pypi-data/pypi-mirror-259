import os

DEFAULT_BEDBASE_API_URL = "https://api.bedbase.org"
# DEFAULT_BEDBASE_API_URL = "http://localhost:8000/api"

HOME_PATH = os.getenv("HOME")
if not HOME_PATH:
    HOME_PATH = os.path.expanduser("~")

OPEN_SIGNAL_FOLDER_NAME = "openSignalMatrix"
OPEN_SIGNAL_URL = "http://big.databio.org/open_chromatin_matrix/"

OS_HG38 = "openSignalMatrix_hg38_percentile99_01_quantNormalized_round4d.txt.gz"
OS_HG19 = "openSignalMatrix_hg19_percentile99_01_quantNormalized_round4d.txt.gz"
OS_MM10 = "openSignalMatrix_mm10_percentile99_01_quantNormalized_round4d.txt.gz"

BED_FOLDER_NAME = "bed_files"
BIGBED_FOLDER_NAME = "bigbed_files"
OUTPUT_FOLDER_NAME = "output"
BEDSTAT_OUTPUT = "bedstat_output"
QC_FOLDER_NAME = "bed_qc"

# bedmaker

BED_TO_BIGBED_PROGRAM = "bedToBigBed"
# BED_TO_BIGBED_PROGRAM = "/home/bnt4me/virginia/repos/bedbase_all/bedboss/bedToBigBed"
BIGBED_TO_BED_PROGRAM = "bigBedToBed"


# COMMANDS TEMPLATES
# bedGraph to bed
BEDGRAPH_TEMPLATE = "macs2 {width} -i {input} -o {output}"
# bigBed to bed
BIGBED_TEMPLATE = f"{BIGBED_TO_BED_PROGRAM} {{input}} {{output}}"
# bigWig to bed
BIGWIG_TEMPLATE = (
    "bigWigToBedGraph {input} /dev/stdout | macs2 {width} -i /dev/stdin -o {output}"
)

WIG_TEMPLATE = "wigToBigWig {input} {chrom_sizes} {intermediate_bw} -clip"
# bed default link
# bed_template = "ln -s {input} {output}"
BED_TEMPLATE = "cp {input} {output}"
# gzip output files
GZIP_TEMPLATE = "gzip {unzipped_converted_file} "

# CONSTANTS
# Creating list of standard chromosome names:
STANDARD_CHROM_LIST = ["chr" + str(chr_nb) for chr_nb in list(range(1, 23))]
STANDARD_CHROM_LIST[len(STANDARD_CHROM_LIST) :] = ["chrX", "chrY", "chrM"]

# bedqc
MAX_FILE_SIZE = 1024 * 1024 * 1024 * 2
MAX_REGION_NUMBER = 5000000
MIN_REGION_WIDTH = 10

# bedstat

# bedbuncher
DEFAULT_BEDBASE_CACHE_PATH = "./bedabse_cache"

BEDBOSS_PEP_SCHEMA_PATH = "https://schema.databio.org/pipelines/bedboss.yaml"
REFGENIE_ENV_VAR = "REFGENIE"

BED_PEP_REGISTRY = "databio/allbeds:bedbase"
