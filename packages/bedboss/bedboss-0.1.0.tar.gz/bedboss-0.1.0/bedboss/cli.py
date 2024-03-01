from ubiquerg import VersionInHelpParser
from argparse import ArgumentParser
import logmuse
import pypiper

from bedboss._version import __version__
from bedboss.const import DEFAULT_BEDBASE_API_URL, DEFAULT_BEDBASE_CACHE_PATH


def build_argparser() -> ArgumentParser:
    """
    BEDboss parser

    :retrun: Tuple[pipeline, arguments]
    """
    parser = VersionInHelpParser(
        prog="bedboss",
        description="Warehouse of pipelines for BED-like files: "
        "bedmaker, bedstat, and bedqc.",
        epilog="",
        version=__version__,
    )

    subparser = parser.add_subparsers(dest="command")
    sub_all = subparser.add_parser(
        "all", help="Run all bedboss pipelines and insert data into bedbase"
    )
    sub_all_pep = subparser.add_parser(
        "insert",
        help="Run all bedboss pipelines using one PEP and insert data into bedbase",
    )
    sub_make = subparser.add_parser(
        "make",
        help="A pipeline to convert bed, bigbed, bigwig or bedgraph "
        "files into bed and bigbed formats",
    )

    sub_qc = subparser.add_parser("qc", help="Run quality control on bed file (bedqc)")
    sub_stat = subparser.add_parser(
        "stat",
        help="A pipeline to read a file in BED format and produce metadata "
        "in JSON format.",
    )

    sub_bunch = subparser.add_parser(
        "bunch",
        help="A pipeline to create bedsets (sets of BED files) that will be retrieved from bedbase.",
    )

    sub_index = subparser.add_parser(
        "index", help="Index not indexed bed files and add them to the qdrant database "
    )

    subparser.add_parser(
        "requirements-check", help="Check if all requirements are installed"
    )

    sub_all.add_argument(
        "--outfolder",
        required=True,
        help="Pipeline output folder [Required]",
        type=str,
    )

    sub_all.add_argument(
        "-s",
        "--sample-name",
        required=True,
        help="name of the sample used to systematically build the output name [Required]",
        type=str,
    )
    sub_all.add_argument(
        "-f", "--input-file", required=True, help="Input file [Required]", type=str
    )
    sub_all.add_argument(
        "-t",
        "--input-type",
        required=True,
        help="Input type [Required] options: (bigwig|bedgraph|bed|bigbed|wig)",
        type=str,
    )
    sub_all.add_argument(
        "-g",
        "--genome",
        required=True,
        help="reference genome (assembly) [Required]",
        type=str,
    )
    sub_all.add_argument(
        "-r",
        "--rfg-config",
        required=False,
        help="file path to the genome config file(refgenie)",
        type=str,
    )
    sub_all.add_argument(
        "--chrom-sizes",
        help="a full path to the chrom.sizes required for the bedtobigbed conversion",
        type=str,
        required=False,
    )
    sub_all.add_argument(
        "-n",
        "--narrowpeak",
        help="whether it's a narrowpeak file",
        action="store_true",
    )
    sub_all.add_argument(
        "--standardize",
        help="Standardize bed files: remove non-standard chromosomes and headers if necessary Default: False",
        action="store_true",
    )
    sub_all.add_argument(
        "--check-qc",
        help="Check quality control before processing data. Default: True",
        action="store_false",
    )
    sub_all.add_argument(
        "--open-signal-matrix",
        type=str,
        required=False,
        default=None,
        help="a full path to the openSignalMatrix required for the tissue "
        "specificity plots",
    )
    sub_all.add_argument(
        "--ensdb",
        type=str,
        required=False,
        default=None,
        help="A full path to the ensdb gtf file required for genomes not in GDdata ",
    )
    sub_all.add_argument(
        "--bedbase-config",
        dest="bedbase_config",
        type=str,
        help="a path to the bedbase configuration file [Required]",
        required=True,
    )
    sub_all.add_argument(
        "--treatment",
        required=False,
        help="A treatment of the bed file",
        type=str,
    )
    sub_all.add_argument(
        "--cell-type",
        required=False,
        help="A cell type of the bed file",
        type=str,
    )
    sub_all.add_argument(
        "--description",
        required=False,
        help="A description of the bed file",
        type=str,
    )
    sub_all.add_argument(
        "--no-db-commit",
        dest="db_commit",
        action="store_false",
        help="skip the JSON commit to the database [Default: False]",
    )
    sub_all.add_argument(
        "--just-db-commit",
        action="store_true",
        help="Do not save the results locally",
    )
    sub_all.add_argument(
        "--upload_qdrant",
        action="store_false",
        help="whether to execute qdrant indexing",
    )
    sub_all.add_argument(
        "--upload-pephub",
        action="store_true",
        help="upload to pephub",
    )

    # all-pep
    sub_all_pep.add_argument(
        "--bedbase-config",
        dest="bedbase_config",
        type=str,
        help="a path to the bedbase configuration file [Required]",
        required=True,
    )
    sub_all_pep.add_argument(
        "--pep",
        dest="pep",
        required=True,
        help="path to the pep file or pephub registry path containing pep [Required]",
        type=str,
    )
    sub_all_pep.add_argument(
        "--output-folder",
        dest="output_folder",
        required=True,
        help="Pipeline output folder [Required]",
        type=str,
    )
    sub_all_pep.add_argument(
        "-r",
        "--rfg-config",
        required=False,
        help="file path to the genome config file(refgenie)",
        type=str,
    )
    sub_all_pep.add_argument(
        "--check-qc",
        help="Check quality control before processing data. Default: True",
        action="store_false",
    )
    sub_all_pep.add_argument(
        "--standardize",
        help="Standardize bed files: remove non-standard chromosomes and headers if necessary Default: False",
        action="store_true",
    )
    sub_all_pep.add_argument(
        "--create-bedset",
        help="Create bedset using pep samples. Name of the bedset will be based on  pep name.Default: False",
        action="store_true",
    )
    sub_all_pep.add_argument(
        "--upload_qdrant",
        action="store_false",
        help="whether to execute qdrant indexing",
    )
    sub_all_pep.add_argument(
        "--ensdb",
        type=str,
        required=False,
        default=None,
        help="A full path to the ensdb gtf file required for genomes not in GDdata ",
    )
    sub_all_pep.add_argument(
        "--no-db-commit",
        dest="db_commit",
        action="store_false",
        help="skip the JSON commit to the database [Default: False]",
    )
    sub_all_pep.add_argument(
        "--just-db-commit",
        action="store_true",
        help="just commit the JSON to the database",
    )
    sub_all_pep.add_argument(
        "--force_overwrite",
        action="store_true",
        help="Weather to overwrite existing records. [Default: False]",
    )
    sub_all_pep.add_argument(
        "--upload-s3",
        action="store_true",
        help="Weather to upload bed, bigbed, and statistics to s3. "
        "Before uploading you have to set up all necessury env vars: "
        "AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_ENDPOINT_URL. [Default: False]",
    )
    sub_all_pep.add_argument(
        "--upload-pephub",
        action="store_true",
        help="upload to pephub",
    )

    # bed_qc
    sub_qc.add_argument(
        "--bedfile",
        help="a full path to bed file to process [Required]",
        required=True,
    )
    sub_qc.add_argument(
        "--outfolder",
        help="a full path to output log folder. [Required]",
        required=True,
    )

    # bed_maker

    sub_make.add_argument(
        "-f",
        "--input-file",
        required=True,
        help="path to the input file [Required]",
        type=str,
    )
    sub_make.add_argument(
        "--outfolder",
        required=True,
        help="Pipeline output folder [Required]",
        type=str,
    )
    sub_make.add_argument(
        "-n",
        "--narrowpeak",
        help="whether it's a narrowpeak file",
        action="store_true",
    )
    sub_make.add_argument(
        "-t",
        "--input-type",
        required=True,
        help="input file format (supported formats: bedGraph, bigBed, bigWig, wig) [Required]",
        type=str,
    )
    sub_make.add_argument(
        "-g",
        "--genome",
        required=True,
        help="reference genome [Required]",
        type=str,
    )
    sub_make.add_argument(
        "-r",
        "--rfg-config",
        required=False,
        default=None,
        help="file path to the genome config file",
        type=str,
    )
    sub_make.add_argument(
        "-o",
        "--output-bed",
        required=True,
        help="path to the output BED files [Required]",
        type=str,
    )
    sub_make.add_argument(
        "--output-bigbed",
        required=True,
        help="path to the folder of output bigBed files [Required]",
        type=str,
    )
    sub_make.add_argument(
        "-s",
        "--sample-name",
        required=True,
        help="name of the sample used to systematically build the output name [Required]",
        type=str,
    )
    sub_make.add_argument(
        "--chrom-sizes",
        help="A full path to the chrom.sizes required for the bedtobigbed conversion [optional]",
        default=None,
        type=str,
        required=False,
    )
    sub_make.add_argument(
        "--standardize",
        help="Standardize bed files: remove non-standard chromosomes and headers if necessary Default: False",
        action="store_true",
    )
    # bed_stat
    sub_stat.add_argument(
        "--bedfile", help="a full path to bed file to process [Required]", required=True
    )
    sub_stat.add_argument(
        "--genome",
        dest="genome",
        type=str,
        required=True,
        help="genome assembly of the sample [Required]",
    )

    sub_stat.add_argument(
        "--outfolder",
        required=True,
        help="Pipeline output folder [Required]",
        type=str,
    )
    sub_stat.add_argument(
        "--bigbed",
        type=str,
        required=False,
        default=None,
        help="a full path to the bigbed files",
    )
    sub_stat.add_argument(
        "--open-signal-matrix",
        type=str,
        required=False,
        default=None,
        help="a full path to the openSignalMatrix required for the tissue "
        "specificity plots",
    )

    sub_stat.add_argument(
        "--ensdb",
        type=str,
        required=False,
        default=None,
        help="a full path to the ensdb gtf file required for genomes not in GDdata ",
    )

    sub_bunch.add_argument(
        "--bedbase-config",
        dest="bedbase_config",
        type=str,
        required=True,
        help="a path to the bedbase configuration file [Required]",
    )
    sub_bunch.add_argument(
        "--bedset-name",
        dest="bedset_name",
        type=str,
        required=True,
        help="a name of the bedset [Required]",
    )

    sub_bunch.add_argument(
        "--bedset-pep",
        dest="bedset_pep",
        type=str,
        required=True,
        help="bedset pep path or pephub registry path containing bedset pep [Required]",
    )
    sub_bunch.add_argument(
        "--base-api",
        dest="bedbase_api",
        type=str,
        default=f"{DEFAULT_BEDBASE_API_URL}",
        required=False,
        help=f"Bedbase API to use. Default is {DEFAULT_BEDBASE_API_URL}",
    )

    sub_bunch.add_argument(
        "--cache-path",
        dest="cache_path",
        type=str,
        default=f"{DEFAULT_BEDBASE_CACHE_PATH}",
        required=False,
        help=f"Path to the cache folder. Default is {DEFAULT_BEDBASE_CACHE_PATH}",
    )
    sub_bunch.add_argument(
        "--heavy",
        dest="heavy",
        action="store_true",
        help="whether to use heavy processing (Calculate and crate plots using R script). ",
    )

    sub_index.add_argument(
        "--bedbase-config",
        dest="bedbase_config",
        type=str,
        required=True,
        help="a path to the bedbase configuration file [Required]",
    )

    sub_index.add_argument(
        "--bedbase-api",
        dest="bedbase_api",
        type=str,
        required=False,
        default=DEFAULT_BEDBASE_API_URL,
        help=f"URL of the Bedbase API [Default: {DEFAULT_BEDBASE_API_URL}]",
    )

    for sub in [sub_all_pep, sub_all, sub_make, sub_stat, sub_qc]:
        sub_all_pep = pypiper.add_pypiper_args(sub)

    return logmuse.add_logging_options(parser)
