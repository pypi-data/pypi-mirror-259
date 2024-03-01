#!/usr/bin/env python3

import pypiper
import os

import logging
import tempfile
import pandas as pd
import gzip
import shutil
from refgenconf import (
    RefGenConf as RGC,
    select_genome_config,
    RefgenconfError,
    CFG_ENV_VARS,
    CFG_FOLDER_KEY,
)
from refgenconf.exceptions import MissingGenomeError
from yacman.exceptions import UndefinedAliasError
from ubiquerg import is_command_callable
from geniml.io import RegionSet

from bedboss.bedclassifier.bedclassifier import get_bed_type
from bedboss.bedqc.bedqc import bedqc
from bedboss.exceptions import RequirementsException, BedBossException

from bedboss.const import (
    BEDGRAPH_TEMPLATE,
    BED_TEMPLATE,
    BIGWIG_TEMPLATE,
    BIGBED_TEMPLATE,
    WIG_TEMPLATE,
    GZIP_TEMPLATE,
    STANDARD_CHROM_LIST,
    BED_TO_BIGBED_PROGRAM,
    BIGBED_TO_BED_PROGRAM,
    QC_FOLDER_NAME,
    REFGENIE_ENV_VAR,
)

_LOGGER = logging.getLogger("bedboss")


class BedMaker:
    """
    Python Package to convert various genomic region files to bed file
    and generate bigbed file for visulization.
    """

    def __init__(
        self,
        input_file: str,
        input_type: str,
        output_bed: str,
        output_bigbed: str,
        sample_name: str,
        genome: str,
        rfg_config: str = None,
        chrom_sizes: str = None,
        narrowpeak: bool = False,
        standardize: bool = False,
        check_qc: bool = True,
        pm: pypiper.PipelineManager = None,
    ):
        """
        Pypiper pipeline to convert supported file formats into
        BED format and bigBed format. Currently supported formats*:
            - bedGraph
            - bigBed
            - bigWig
            - wig
        :param input_file: path to the input file
        :param input_type: a [bigwig|bedgraph|bed|bigbed|wig] file that will be
                           converted into BED format
        :param output_bed: path to the output BED files
        :param output_bigbed: path to the output bigBed files
        :param sample_name: name of the sample used to systematically build the
                            output name
        :param genome: reference genome
        :param rfg_config: file path to the genome config file
        :param chrom_sizes: a full path to the chrom.sizes required for the
                            bedtobigbed conversion
        :param narrowpeak: whether the regions are narrow (transcription factor
                           implies narrow, histone mark implies broad peaks)
        :param standardize: whether standardize bed file. (includes standardizing chromosome names and
            sanitize file first rows if they exist) Default: False
            Additionally, standardize chromosome names.
            If true, filter the input file to contain only
            the standard chromosomes, remove regions on
            ChrUn chromosomes
        :param check_qc: run quality control during bedmaking
        :param pm: pypiper object
        :return: noReturn
        """

        # Define file paths
        self.input_file = input_file
        self.input_type = input_type.lower()
        self.output_bed = output_bed
        self.output_bigbed = output_bigbed
        self.file_name = os.path.basename(input_file)
        self.file_id = os.path.splitext(self.file_name)[0]
        self.input_extension = os.path.splitext(self.file_name)[1]

        self.sample_name = sample_name
        self.genome = genome
        self.chrom_sizes = chrom_sizes
        self.check_qc = check_qc
        self.rfg_config = rfg_config
        self.standardize = standardize

        # Define whether input file data is broad or narrow peaks
        self.narrowpeak = narrowpeak
        self.width = "bdgbroadcall" if not self.narrowpeak else "bdgpeakcall"

        # check if output bed is file or folder:
        self.output_bed_extension = os.path.splitext(self.output_bed)[1]
        if self.output_bed_extension == "":
            self.output_bed = os.path.join(
                self.output_bed,
                f"{os.path.splitext(os.path.splitext(os.path.split(input_file)[1])[0])[0]}"
                ".bed.gz",
            )
            self.output_bed_extension = os.path.splitext(self.output_bed)[1]

        # Set output folders:
        # create one if doesn't exist
        if self.input_type != "bed":
            if self.input_extension == ".gz":
                self.output_bed = (
                    os.path.splitext(os.path.splitext(self.output_bed)[0])[0]
                    + ".bed.gz"
                )
            else:
                self.output_bed = os.path.splitext(self.output_bed)[0] + ".bed.gz"
        else:
            if self.input_extension != ".gz" and self.output_bed_extension != ".gz":
                self.output_bed = self.output_bed + ".gz"
            else:
                self.output_bed = self.output_bed

        self.bed_parent = os.path.dirname(self.output_bed)
        if not os.path.exists(self.bed_parent):
            _LOGGER.info(
                f"Output directory does not exist. Creating: {self.bed_parent}"
            )
            os.makedirs(self.bed_parent)

        if not os.path.exists(self.output_bigbed):
            _LOGGER.info(
                f"BigBed directory does not exist. Creating: {self.output_bigbed}"
            )
            os.makedirs(self.output_bigbed)

        if not pm:
            self.logs_name = "bedmaker_logs"
            self.logs_dir = os.path.join(
                self.bed_parent, self.logs_name, self.sample_name
            )
            if not os.path.exists(self.logs_dir):
                _LOGGER.info("bedmaker logs directory doesn't exist. Creating one...")
                os.makedirs(self.logs_dir)
            self.pm = pypiper.PipelineManager(
                name="bedmaker",
                outfolder=self.logs_dir,
                recover=True,
                multi=True,
            )
        else:
            self.pm = pm

        # self.make()

    def make(self) -> dict:
        """
        Create bed and BigBed files.
        This is main function that executes every step of the bedmaker pipeline.
        """
        _LOGGER.info(f"Got input type: {self.input_type}")
        # converting to bed.gz if needed
        self.make_bed()
        try:
            bed_type, bed_format = get_bed_type(self.input_file)
        except Exception:
            # we need this exception to catch the case when the input file is not a bed file
            bed_type, bed_format = get_bed_type(self.output_bed)
        if self.check_qc:
            try:
                bedqc(
                    self.output_bed,
                    outfolder=os.path.join(self.bed_parent, QC_FOLDER_NAME),
                    pm=self.pm,
                )
            except Exception as e:
                raise BedBossException(
                    f"Quality control failed for {self.output_bed}. Error: {e}"
                )

        self.make_bigbed(bed_type=bed_type)

        return {
            "bed_type": bed_type,
            "bed_format": bed_format,
            "genome": self.genome,
            "digest": RegionSet(self.output_bed).identifier,
        }

    def make_bed(self) -> None:
        """
        Convert the input file to BED format by construct the command based
        on input file type and execute the command.
        """

        _LOGGER.info(f"Converting {os.path.abspath(self.input_file)} to BED format.")
        temp_bed_path = os.path.splitext(self.output_bed)[0]

        # creat cmd to run that convert non bed file to bed file
        if not self.input_type == "bed":
            _LOGGER.info(f"Converting {self.input_file} to BED format")

            # Use the gzip and shutil modules to produce temporary unzipped files
            if self.input_extension == ".gz":
                temp_input_file = os.path.join(
                    os.path.dirname(self.output_bed),
                    os.path.splitext(self.file_name)[0],
                )
                with gzip.open(self.input_file, "rb") as f_in:
                    with open(temp_input_file, "wb") as f_out:
                        shutil.copyfileobj(f_in, f_out)
                self.pm.clean_add(temp_input_file)

            # creating cmd for bedGraph files
            if self.input_type == "bedGraph":
                if not is_command_callable("macs2"):
                    raise RequirementsException(
                        "To convert bedGraph file You must first install "
                        "macs2 and add it to your PATH. "
                        "Instruction: "
                        "https://pypi.org/project/MACS2/"
                    )
                else:
                    cmd = BEDGRAPH_TEMPLATE.format(
                        input=self.input_file,
                        output=temp_bed_path,
                        width=self.width,
                    )
            # creating cmd for bigWig files
            elif self.input_type == "bigWig":
                if not is_command_callable("bigWigToBedGraph"):
                    raise RequirementsException(
                        "To convert bigWig file You must first install "
                        "bigWigToBedGraph and add it to your PATH. "
                        "Instruction: "
                        "https://genome.ucsc.edu/goldenpath/help/bigWig.html"
                    )
                else:
                    cmd = BIGWIG_TEMPLATE.format(
                        input=self.input_file,
                        output=temp_bed_path,
                        width=self.width,
                    )
            # creating cmd for wig files
            elif self.input_type == "wig":
                if not self.chrom_sizes:
                    self.chrom_sizes = self.get_chrom_sizes()

                # define a target for temporary bw files
                temp_target = os.path.join(self.bed_parent, self.file_id + ".bw")
                if not is_command_callable("wigToBigWig"):
                    raise RequirementsException(
                        "To convert wig file You must first install "
                        "wigToBigWig and add it in your PATH. "
                        "Instruction: "
                        "https://genome.ucsc.edu/goldenpath/help/bigWig.html"
                    )
                else:
                    self.pm.clean_add(temp_target)
                    cmd1 = WIG_TEMPLATE.format(
                        input=self.input_file,
                        intermediate_bw=temp_target,
                        chrom_sizes=self.chrom_sizes,
                        width=self.width,
                    )

                if not is_command_callable("bigWigToBedGraph"):
                    raise RequirementsException(
                        "To convert bigWig file You must first install "
                        "bigWigToBedGraph and add it in your PATH. "
                        "Instruction: "
                        "https://genome.ucsc.edu/goldenpath/help/bigWig.html"
                    )
                else:
                    cmd2 = BIGWIG_TEMPLATE.format(
                        input=temp_target,
                        output=temp_bed_path,
                        width=self.width,
                    )
                    cmd = [cmd1, cmd2]
            # creating cmd for bigBed files
            elif self.input_type == "bigBed":
                if not is_command_callable(BIGBED_TO_BED_PROGRAM):
                    raise RequirementsException(
                        "To convert bigBed file You must first install "
                        "bigBedToBed and add it in your PATH. "
                        "Instruction: "
                        "https://genome.ucsc.edu/goldenpath/help/bigBed.html"
                    )
                else:
                    cmd = BIGBED_TEMPLATE.format(
                        input=self.input_file, output=temp_bed_path
                    )
            else:
                raise NotImplementedError(
                    f"'{self.input_type}' format is not supported"
                )
            # add cmd to create the gz file
            if self.input_extension != ".gz":
                gzip_cmd = GZIP_TEMPLATE.format(unzipped_converted_file=temp_bed_path)
                if not isinstance(cmd, list):
                    cmd = [cmd]
                cmd.append(gzip_cmd)
        # creating cmd for bed files
        else:
            if self.standardize:
                self.copy_with_standardization()

            else:
                if self.input_extension == ".gz":
                    cmd = BED_TEMPLATE.format(
                        input=self.input_file, output=self.output_bed
                    )
                else:
                    cmd = [
                        BED_TEMPLATE.format(
                            input=self.input_file,
                            output=os.path.splitext(self.output_bed)[0],
                        ),
                        GZIP_TEMPLATE.format(
                            unzipped_converted_file=os.path.splitext(self.output_bed)[0]
                        ),
                    ]
                self.pm.run(cmd, target=self.output_bed)

        self.pm._cleanup()

    def copy_with_standardization(self):
        df = None
        max_rows = 5
        row_count = 0
        while row_count <= max_rows:
            try:
                df = pd.read_csv(
                    self.input_file, sep="\t", header=None, nrows=4, skiprows=row_count
                )
                if row_count > 0:
                    _LOGGER.info(
                        f"Skipped {row_count} rows while standardization {self.input_file}"
                    )
                break
            except (pd.errors.ParserError, pd.errors.EmptyDataError) as e:
                if row_count <= max_rows:
                    row_count += 1
        if not isinstance(df, pd.DataFrame):
            raise BedBossException(
                reason=f"Bed file is broken and could not be parsed due to CSV parse error."
            )
        df = df.dropna(axis=1)
        _LOGGER.info("Standardizing chromosomes...")
        df = df[df.loc[:, 0].isin(STANDARD_CHROM_LIST)]
        df.to_csv(
            self.output_bed, compression="gzip", sep="\t", header=False, index=False
        )

    def make_bigbed(self, bed_type: str = None) -> None:
        """
        Generate bigBed file for the BED file.

        :param bed_type: bed type to be used for bigBed file generation "bed{bedtype}+{n}" [Default: None]
        """
        _LOGGER.info(f"Generating bigBed files for: {self.input_file}")

        bedfile_name = os.path.split(self.output_bed)[1]
        fileid = os.path.splitext(os.path.splitext(bedfile_name)[0])[0]
        # Produce bigBed (big_narrow_peak) file from peak file
        big_narrow_peak = os.path.join(self.output_bigbed, fileid + ".bigBed")
        if not self.chrom_sizes:
            try:
                self.chrom_sizes = self.get_chrom_sizes()
            except MissingGenomeError:
                _LOGGER.error(f"Could not find Genome in refgenie. Skipping...")
                self.chrom_sizes = ""

        temp = os.path.join(self.output_bigbed, next(tempfile._get_candidate_names()))

        if not os.path.exists(big_narrow_peak):
            self.pm.clean_add(temp)

            if not is_command_callable(f"{BED_TO_BIGBED_PROGRAM}"):
                raise RequirementsException(
                    "To convert bed to BigBed file You must first install "
                    "bedToBigBed add in your PATH. "
                    "Instruction: "
                    "https://genome.ucsc.edu/goldenpath/help/bigBed.html"
                )
            if bed_type is not None:
                cmd = f"zcat {self.output_bed} | sort -k1,1 -k2,2n > {temp}"
                self.pm.run(cmd, temp)

                cmd = f"{BED_TO_BIGBED_PROGRAM} -type={bed_type} {temp} {self.chrom_sizes} {big_narrow_peak}"
                try:
                    _LOGGER.info(f"Running: {cmd}")
                    self.pm.run(cmd, big_narrow_peak, nofail=True)
                except Exception as err:
                    _LOGGER.error(
                        f"Fail to generating bigBed files for {self.input_file}: "
                        f"unable to validate genome assembly with Refgenie. "
                        f"Error: {err}"
                    )
            else:
                cmd = (
                    "zcat "
                    + self.output_bed
                    + " | awk '{ print $1, $2, $3 }'| sort -k1,1 -k2,2n > "
                    + temp
                )
                self.pm.run(cmd, temp)
                cmd = f"{BED_TO_BIGBED_PROGRAM} -type=bed3 {temp} {self.chrom_sizes} {big_narrow_peak}"

                try:
                    self.pm.run(cmd, big_narrow_peak, nofail=True)
                except Exception as err:
                    _LOGGER.info(
                        f"Fail to generating bigBed files for {self.input_file}: "
                        f"unable to validate genome assembly with Refgenie. "
                        f"Error: {err}"
                    )
            self.pm._cleanup()

    def get_rgc(self) -> RGC:
        """
        Get refgenie config file.

        :return str: rfg_config file path
        """
        if not self.rfg_config:
            _LOGGER.info("Creating refgenie genome config file...")
            cwd = os.getenv(REFGENIE_ENV_VAR, os.getcwd())
            self.rfg_config = os.path.join(cwd, "genome_config.yaml")

        # get path to the genome config; from arg or env var if arg not provided
        refgenie_cfg_path = select_genome_config(
            filename=self.rfg_config, check_exist=False
        )

        if not refgenie_cfg_path:
            raise OSError(
                "Could not determine path to a refgenie genome configuration file. "
                f"Use --rfg-config argument or set the path with '{CFG_ENV_VARS}'."
            )
        if isinstance(refgenie_cfg_path, str) and not os.path.exists(refgenie_cfg_path):
            # file path not found, initialize a new config file
            _LOGGER.info(
                f"File '{refgenie_cfg_path}' does not exist. "
                "Initializing refgenie genome configuration file."
            )
            rgc = RGC(entries={CFG_FOLDER_KEY: os.path.dirname(refgenie_cfg_path)})
            rgc.initialize_config_file(filepath=refgenie_cfg_path)
        else:
            _LOGGER.info(
                "Reading refgenie genome configuration file from file: "
                f"{refgenie_cfg_path}"
            )
            rgc = RGC(filepath=refgenie_cfg_path)

        return rgc

    def get_chrom_sizes(self) -> str:
        """
        Get chrom.sizes file with Refgenie.

        :return str: chrom.sizes file path
        """

        _LOGGER.info("Determining path to chrom.sizes asset via Refgenie.")
        # initalizing refginie config file
        rgc = self.get_rgc()

        try:
            # get local path to the chrom.sizes asset
            chrom_sizes = rgc.seek(
                genome_name=self.genome,
                asset_name="fasta",
                tag_name="default",
                seek_key="chrom_sizes",
            )
            _LOGGER.info(chrom_sizes)
        except (UndefinedAliasError, RefgenconfError):
            # if no local chrom.sizes file found, pull it first
            _LOGGER.info("Could not determine path to chrom.sizes asset, pulling")
            rgc.pull(genome=self.genome, asset="fasta", tag="default")
            chrom_sizes = rgc.seek(
                genome_name=self.genome,
                asset_name="fasta",
                tag_name="default",
                seek_key="chrom_sizes",
            )

        _LOGGER.info(f"Determined path to chrom.sizes asset: {chrom_sizes}")

        return chrom_sizes


def make_all(
    input_file: str,
    input_type: str,
    output_bed: str,
    output_bigbed: str,
    sample_name: str,
    genome: str,
    rfg_config: str = None,
    chrom_sizes: str = None,
    narrowpeak: bool = False,
    standardize: bool = False,
    check_qc: bool = True,
    pm: pypiper.PipelineManager = None,
    **kwargs,
):
    """
    Maker of bed and bigbed files.

    Pipeline to convert supported file formats into
    BED format and bigBed format. Currently supported formats*:
        - bedGraph
        - bigBed
        - bigWig
        - wig
    :param input_file: path to the input file
    :param input_type: a [bigwig|bedgraph|bed|bigbed|wig] file that will be
                       converted into BED format
    :param output_bed: path to the output BED files
    :param output_bigbed: path to the output bigBed files
    :param sample_name: name of the sample used to systematically build the
                        output name
    :param genome: reference genome
    :param rfg_config: file path to the genome config file
    :param chrom_sizes: a full path to the chrom.sizes required for the
                        bedtobigbed conversion
    :param narrowpeak: whether the regions are narrow (transcription factor
                       implies narrow, histone mark implies broad peaks)
    :param standardize: whether standardize bed file. (includes standardizing chromosome names and
        sanitize file first rows if they exist) Default: False
        Additionally, standardize chromosome names.
        If true, filter the input file to contain only
        the standard chromosomes, remove regions on
        ChrUn chromosomes
    :param check_qc: run quality control during bedmaking
    :param pm: pypiper object
    :return: dict with generated bed metadata:
        {
            "bed_type": bed_type. e.g. bed, bigbed
            "bed_format": bed_format. e.g. narrowpeak, broadpeak
            "genome": genome of the sample,
            "digest": bedfile identifier,
        }
    """
    return BedMaker(
        input_file=input_file,
        input_type=input_type,
        output_bed=output_bed,
        output_bigbed=output_bigbed,
        sample_name=sample_name,
        genome=genome,
        rfg_config=rfg_config,
        chrom_sizes=chrom_sizes,
        narrowpeak=narrowpeak,
        standardize=standardize,
        check_qc=check_qc,
        pm=pm,
        **kwargs,
    ).make()
