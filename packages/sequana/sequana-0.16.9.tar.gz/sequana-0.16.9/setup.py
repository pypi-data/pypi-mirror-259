# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cython',
 'enrichment',
 'images',
 'kraken',
 'main',
 'modules_report',
 'multiqc',
 'plots',
 'scripts',
 'scripts.main',
 'sequana',
 'sequana.cython',
 'sequana.enrichment',
 'sequana.kraken',
 'sequana.modules_report',
 'sequana.multiqc',
 'sequana.plots',
 'sequana.resources',
 'sequana.resources.css',
 'sequana.resources.data',
 'sequana.resources.doc',
 'sequana.resources.doc.rnadiff_compare',
 'sequana.resources.doc.rnaseq_0',
 'sequana.resources.doc.rnaseq_0.sample1',
 'sequana.resources.doc.rnaseq_0.sample1.feature_counts_0',
 'sequana.resources.doc.rnaseq_0.sample1.feature_counts_1',
 'sequana.resources.doc.rnaseq_0.sample1.feature_counts_2',
 'sequana.resources.doc.rnaseq_0.sample2.feature_counts_0',
 'sequana.resources.doc.rnaseq_0.sample2.feature_counts_1',
 'sequana.resources.doc.rnaseq_0.sample2.feature_counts_2',
 'sequana.resources.examples',
 'sequana.resources.images',
 'sequana.resources.js',
 'sequana.resources.snpeff',
 'sequana.resources.templates',
 'sequana.resources.testing',
 'sequana.scripts',
 'sequana.scripts.main',
 'sequana.utils',
 'sequana.viz',
 'utils',
 'viz']

package_data = \
{'': ['*'],
 'sequana.resources': ['scripts/*'],
 'sequana.resources.doc': ['rnadiff/*', 'rnadiff/code/*', 'rnadiff/counts/*']}

install_requires = \
['adjusttext>=0.8,<0.9',
 'bioservices>=1.11.2,<2.0.0',
 'brokenaxes>=0.5.0,<0.6.0',
 'bx-python>=0.10.0,<0.11.0',
 'click>=8.1.7,<9.0.0',
 'colorlog>=6.8.0,<7.0.0',
 'colormap>=1.0.6,<2.0.0',
 'cython>=3.0.7,<4.0.0',
 'deprecated>=1.2.14,<2.0.0',
 'easydev>=0.12.1,<0.13.0',
 'gseapy>=1.1.1,<2.0.0',
 'itolapi>=4.1.2,<5.0.0',
 'matplotlib-venn>=0.11.9,<0.12.0',
 'matplotlib<3.8.2',
 'multiqc<1.18',
 'plotly>=5.18.0,<6.0.0',
 'pysam>=0.22.0,<0.23.0',
 'rich-click>=1.7.2,<2.0.0',
 'scikit-learn>=1.3.2,<2.0.0',
 'scipy<1.11.4',
 'seaborn>=0.13.1,<0.14.0',
 'selenium>=4.16.0,<5.0.0',
 'snakemake<8',
 'statsmodels>=0.14.1,<0.15.0',
 'tqdm>=4.66.1,<5.0.0',
 'upsetplot>=0.9.0,<0.10.0',
 'vcfpy>=0.13.6,<0.14.0',
 'xlrd>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['sequana = sequana.scripts.main.main:main',
                     'sequana_coverage = sequana.scripts.coverage:main',
                     'sequana_substractor = sequana.scripts.substractor:main',
                     'sequana_taxonomy = sequana.scripts.taxonomy:main'],
 'multiqc.hooks.v1': ['before_config = sequana.multiqc.config:load_config'],
 'multiqc.modules.v1': ['sequana_bamtools_stats = '
                        'sequana.multiqc.bamtools_stats:MultiqcModule',
                        'sequana_coverage = '
                        'sequana.multiqc.coverage:MultiqcModule',
                        'sequana_isoseq = sequana.multiqc.isoseq:MultiqcModule',
                        'sequana_isoseq_qc = '
                        'sequana.multiqc.isoseq_qc:MultiqcModule',
                        'sequana_kraken = sequana.multiqc.kraken:MultiqcModule',
                        'sequana_laa = sequana.multiqc.laa:MultiqcModule',
                        'sequana_pacbio_qc = '
                        'sequana.multiqc.pacbio_qc:MultiqcModule',
                        'sequana_quality_control = '
                        'sequana.multiqc.quality_control:MultiqcModule'],
 'sequana.module': ['sequana_coverage = '
                    'sequana.modules_report.coverage:CoverageModule',
                    'sequana_summary = '
                    'sequana.modules_report.summary:SummaryModule',
                    'sequana_variant_calling = '
                    'sequana.modules_report.variant_calling:VariantCallingModule']}

setup_kwargs = {
    'name': 'sequana',
    'version': '0.16.9',
    'description': 'A set of standalone application and pipelines dedicated to NGS analysis',
    'long_description': 'SEQUANA\n############\n\n\n.. image:: https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)\n   :target: http://bioconda.github.io/recipes/sequana/README.html\n\n.. image:: https://badge.fury.io/py/sequana.svg\n    :target: https://pypi.python.org/pypi/sequana\n\n.. image:: https://github.com/sequana/sequana/actions/workflows/main.yml/badge.svg?branch=main\n    :target: https://github.com/sequana/sequana/actions/workflows/main.yml\n\n.. image:: https://coveralls.io/repos/github/sequana/sequana/badge.svg?branch=main\n    :target: https://coveralls.io/github/sequana/sequana?branch=main\n\n.. image:: http://readthedocs.org/projects/sequana/badge/?version=main\n    :target: http://sequana.readthedocs.org/en/latest/?badge=main\n    :alt: Documentation Status\n\n.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg\n   :target: http://joss.theoj.org/papers/10.21105/joss.00352\n   :alt: JOSS (journal of open source software) DOI\n\n.. image:: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C3.10-blue.svg\n    :target: https://pypi.python.org/pypi/sequana\n    :alt: Python 3.8 | 3.9 | 3.10 | 3.11\n\n.. image:: https://img.shields.io/github/issues/sequana/sequana.svg\n    :target: https://github.com/sequana/sequana/issues\n    :alt: GitHub Issues\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n\n\n:How to cite: Citations are important for us to carry on developments.\n    For Sequana library (including the pipelines), please use\n\n    Cokelaer et al, (2017), \'Sequana\': a Set of Snakemake NGS pipelines, Journal of\n    Open Source Software, 2(16), 352, `JOSS DOI doi:10.21105/joss.00352 <https://joss.theoj.org/papers/10.21105/joss.00352>`_\n\n    For the **genome coverage** tool (sequana_coverage):  Dimitri Desvillechabrol, Christiane Bouchier,\n    Sean Kennedy, Thomas Cokelaer. Sequana coverage: detection and characterization of genomic\n    variations using running median and mixture models. GigaScience, 7(12), 2018.\n    https://doi.org/10.1093/gigascience/giy110\n    Also available on bioRxiv (DOI: http://biorxiv.org/content/early/2016/12/08/092478)\n\n    For **Sequanix**: Dimitri Desvillechabrol, Rachel Legendre, Claire Rioualen,\n    Christiane Bouchier, Jacques van Helden, Sean Kennedy, Thomas Cokelaer.\n    Sequanix: A Dynamic Graphical Interface for Snakemake Workflows\n    Bioinformatics, bty034, https://doi.org/10.1093/bioinformatics/bty034\n    Also available on bioRxiv (DOI: https://doi.org/10.1101/162701)\n\n\n**Sequana** includes a set of pipelines related to NGS (new generation sequencing) including quality control, variant calling, coverage, taxonomy, transcriptomics. We also ship **Sequanix**, a graphical user interface for Snakemake pipelines.\n\n\n\n.. list-table:: Pipelines and tools available in the Sequana project\n    :widths: 15 35 20 15 15\n    :header-rows: 1\n\n    * - **name/github**\n      - **description**\n      - **Latest Pypi version**\n      - **Test passing**\n      - **apptainers**\n    * - `sequana_pipetools <https://github.com/sequana/sequana_pipetools>`_\n      - Create and Manage Sequana pipeline\n      - .. image:: https://badge.fury.io/py/sequana-pipetools.svg\n            :target: https://pypi.python.org/pypi/sequana_pipetools\n      - .. image:: https://github.com/sequana/sequana_pipetools/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/sequana_pipetools/actions/workflows/main.yml\n      -  Not required\n    * - `sequana-wrappers <https://github.com/sequana/sequana-wrappers>`_\n      - Set of wrappers to build pipelines\n      - Not on pypi\n      - .. image:: https://github.com/sequana/sequana-wrappers/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/sequana-wrappers/actions/workflows/main.yml\n      - Not required\n    * - `demultiplex <https://github.com/sequana/demultiplex>`_\n      - Demultiplex your raw data\n      - .. image:: https://badge.fury.io/py/sequana-demultiplex.svg\n            :target: https://pypi.python.org/pypi/sequana-demultiplex\n      - .. image:: https://github.com/sequana/demultiplex/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/demultiplex/actions/workflows/main.yml\n      - License restriction\n    * - `denovo <https://github.com/sequana/denovo>`_\n      - denovo sequencing data\n      - .. image:: https://badge.fury.io/py/sequana-denovo.svg\n            :target: https://pypi.python.org/pypi/sequana-denovo\n      - .. image:: https://github.com/sequana/denovo/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/denovo/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/denovo/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/denovo/actions/workflows/apptainer.yml\n    * - `fastqc <https://github.com/sequana/fastqc>`_\n      - Get Sequencing Quality control\n      - .. image:: https://badge.fury.io/py/sequana-fastqc.svg\n            :target: https://pypi.python.org/pypi/sequana-fastqc\n      - .. image:: https://github.com/sequana/fastqc/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/fastqc/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/fastqc/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/fastqc/actions/workflows/apptainer.yml\n    * - `LORA <https://github.com/sequana/lora>`_\n      - Map sequences on target genome\n      - .. image:: https://badge.fury.io/py/sequana-lora.svg\n            :target: https://pypi.python.org/pypi/sequana-lora\n      - .. image:: https://github.com/sequana/lora/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/lora/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/lora/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/lora/actions/workflows/apptainer.yml\n    * - `mapper <https://github.com/sequana/mapper>`_\n      - Map sequences on target genome\n      - .. image:: https://badge.fury.io/py/sequana-mapper.svg\n            :target: https://pypi.python.org/pypi/sequana-mapper\n      - .. image:: https://github.com/sequana/mapper/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/mapper/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/mapper/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/mapper/actions/workflows/apptainer.yml\n    * - `nanomerge <https://github.com/sequana/nanomerge>`_\n      - Merge barcoded (or unbarcoded) nanopore fastq and reporting\n      - .. image:: https://badge.fury.io/py/sequana-nanomerge.svg\n            :target: https://pypi.python.org/pypi/sequana-nanomerge\n      - .. image:: https://github.com/sequana/nanomerge/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/nanomerge/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/nanomerge/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/nanomerge/actions/workflows/apptainer.yml\n    * - `pacbio_qc <https://github.com/sequana/pacbio_qc>`_\n      - Pacbio quality control\n      - .. image:: https://badge.fury.io/py/sequana-pacbio-qc.svg\n            :target: https://pypi.python.org/pypi/sequana-pacbio-qc\n      - .. image:: https://github.com/sequana/pacbio_qc/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/pacbio_qc/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/pacbio_qc/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/pacbio_qc/actions/workflows/apptainer.yml\n    * - `ribofinder <https://github.com/sequana/ribofinder>`_\n      - Find ribosomal content\n      - .. image:: https://badge.fury.io/py/sequana-ribofinder.svg\n            :target: https://pypi.python.org/pypi/sequana-ribofinder\n      - .. image:: https://github.com/sequana/ribofinder/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/ribofinder/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/ribofinder/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/ribofinder/actions/workflows/apptainer.yml\n    * - `rnaseq <https://github.com/sequana/rnaseq>`_\n      - RNA-seq analysis\n      - .. image:: https://badge.fury.io/py/sequana-rnaseq.svg\n            :target: https://pypi.python.org/pypi/sequana-rnaseq\n      - .. image:: https://github.com/sequana/rnaseq/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/rnaseq/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/rnaseq/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/rnaseq/actions/workflows/apptainer.yml\n    * - `variant_calling <https://github.com/sequana/variant_calling>`_\n      - Variant Calling\n      - .. image:: https://badge.fury.io/py/sequana-variant-calling.svg\n            :target: https://pypi.python.org/pypi/sequana-variant-calling\n      - .. image:: https://github.com/sequana/variant_calling/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/variant_calling/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/variant_calling/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/variant_calling/actions/workflows/apptainer.yml\n    * - `multicov <https://github.com/sequana/multicov>`_\n      - Coverage (mapping)\n      - .. image:: https://badge.fury.io/py/sequana-multicov.svg\n            :target: https://pypi.python.org/pypi/sequana-multicov\n      - .. image:: https://github.com/sequana/multicov/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/multicov/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/coverage/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/coverage/actions/workflows/apptainer.yml\n    * - `laa <https://github.com/sequana/laa>`_\n      - Long read Amplicon Analysis\n      - .. image:: https://badge.fury.io/py/sequana-laa.svg\n            :target: https://pypi.python.org/pypi/sequana-laa\n      - .. image:: https://github.com/sequana/laa/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/laa/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/laa/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/laa/actions/workflows/apptainer.yml\n    * - `revcomp <https://github.com/sequana/revcomp>`_\n      - reverse complement of sequence data\n      - .. image:: https://badge.fury.io/py/sequana-revcomp.svg\n            :target: https://pypi.python.org/pypi/sequana-revcomp\n      - .. image:: https://github.com/sequana/revcomp/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/revcomp/actions/workflows/main.yml\n      - .. image:: https://github.com/sequana/revcomp/actions/workflows/apptainer.yml/badge.svg\n            :target: https://github.com/sequana/revcomp/actions/workflows/apptainer.yml\n    * - `downsampling <https://github.com/sequana/downsampling>`_\n      - downsample sequencing data\n      - .. image:: https://badge.fury.io/py/sequana-downsampling.svg\n            :target: https://pypi.python.org/pypi/sequana-downsampling\n      - .. image:: https://github.com/sequana/downsampling/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/downsampling/actions/workflows/main.yml\n      - Not required\n    * - `depletion <https://github.com/sequana/depletion>`_\n      - remove/select reads mapping a reference\n      - .. image:: https://badge.fury.io/py/sequana-downsampling.svg\n            :target: https://pypi.python.org/pypi/sequana-depletion\n      - .. image:: https://github.com/sequana/depletion/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/depletion/actions/workflows/main.yml\n      -\n\n\n\n\n\n.. list-table:: Pipelines not yet released\n    :widths: 20 40 20 20\n    :header-rows: 1\n\n    * - **name/github**\n      - **description**\n      - **Latest Pypi version**\n      - **Test passing**\n    * - `trf <https://github.com/sequana/trf>`_\n      - Find repeats\n      - .. image:: https://badge.fury.io/py/sequana-trf.svg\n            :target: https://pypi.python.org/pypi/sequana-trf\n      - .. image:: https://github.com/sequana/trf/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/trf/actions/workflows/main.yml\n    * - `multitax <https://github.com/sequana/multitax>`_\n      - Taxonomy analysis\n      - .. image:: https://badge.fury.io/py/sequana-multitax.svg\n            :target: https://pypi.python.org/pypi/sequana-multitax\n      - .. image:: https://github.com/sequana/multitax/actions/workflows/main.yml/badge.svg\n            :target: https://github.com/sequana/multitax/actions/workflows/main.yml\n\n**Please see the** `documentation <http://sequana.readthedocs.org>`_ for an\nup-to-date status and documentation.\n\n\nContributors\n============\n\nMaintaining Sequana would not have been possible without users and contributors.\nEach contribution has been an encouragement to pursue this project. Thanks to all:\n\n.. image:: https://contrib.rocks/image?repo=sequana/sequana\n    :target: https://github.com/sequana/sequana/graphs/contributors\n\n\n\nChangelog\n~~~~~~~~~\n\n========= ==========================================================================\nVersion   Description\n========= ==========================================================================\n0.16.9    * Major fix on PCA and add batch effect plots in RNAdiff analysis\n          * count matrix and DESeq2 output files\' headers fixed with missing index\n            (no impact on analysis but only for those willing to use the CSV files\n            in excel)\n          * Taxonomy revisited to save taxonomy.dat in gzipped CSV format.\n0.16.8    * update IEM for more testing\n          * better handling of error in RNADiff\n          * Add new methods for ribodesigner\n0.16.7    * Stable release (fix doc), deprecated.\n0.16.6    * Refactor IEM to make it more robust with more tests.\n0.16.5    * refactor to use pyproject instead of setuptools\n          * remove pkg_resources (future deprecation)\n          * remove unused requirements (cookiecutter, adjusttext, docutuils, mock,\n            psutil, pykwalify)\n          * cleanup resources (e.g. moving canvas/bar.py into viz)\n0.16.4    * hot fixes on RNAdiff reports and enrichments\n0.16.3    * Remove all rules (see https://github.com/sequana/sequana-wrappers)\n            instead\n          * add precommit for developers and applied to all modules and doc\n          * Fix wrong import for sequana standalone (regression)\n0.16.2    * save coverage PNG image (regression)\n          * Update taxonomy/coverage standalone (regression) and more tests\n0.16.1    * hotfix missing module\n0.16.0    * add mpileup module\n          * homogenization enrichment + fixup rnadiff\n          * Complete refactoring of sequana coverage module.\n            Allow sequana_coverage to handle small eukaryotes in a more memory\n            efficient way.\n          * use click for the sequana_taxonomy and sequana_coverage and\n            sequana rnadiff command\n          * Small fixup on homer, idr and phantom modules (for chipseq pipeline)\n0.15.4    * add plot for rnaseq/rnadiff\n0.15.3    * add sequana.viz.plotly module. use tqdm in bamtools module\n          * KEGG API changed. We update sequana to use headless server and keep\n            the feature of annotated and colored pathway.\n          * Various improvements on KEGG enrichment including saving pathways,\n            addition --comparison option in sequana sub-command, plotly plots, etc\n0.15.2    * ribodesigner can now accept an input fasta with no GFF assuming the\n            fasta already contains the rRNA sequences\n          * Fix IEM module when dealing with double indexing\n          * Fix anchors in HTML reports (rnadiff module)\n          * refactorise compare module to take several rnadiff results as input\n          * enrichment improvements (export KEGG and GO as csv files\n0.15.1    * Fix creation of images directory in modules report\n          * add missing test related to gff\n          * Fix #804\n0.15.0    * add logo in reports\n          * RNADiff reports can now use shrinkage or not (optional)\n          * remove useless rules now in sequana-wrappers\n          * update main README to add LORA in list of pipelines\n          * Log2FC values are now **shrinked log2FC** values in volcano plot\n            and report table. "NotShrinked" columns for Log2FC and Log2FCSE\n            prior shrinkage are displayed in report table.\n0.14.6    * add fasta_and_gff_annotation module to correct fasta and gff given a\n            vcf file.\n          * add macs3 module to read output of macs3 peak detector.\n          * add idr module to read results of idr analysis\n          * add phantom module to compute phantom peaks\n          * add homer module to read annotation files from annotatePeaks\n0.14.5    * move start_pipeline standalone in\n            https://github.com/sequana/sequana_pipetools\n          * update snpeff module to allows build command to have options\n0.14.4    * hotfix bug on kegg colorised pathways\n          * Fix the hover_name in rnadiff volcano plot to include the\n            index/attribute.\n          * pin snakemake to be >=7.16\n0.14.3    * new fisher metric in variant calling\n          * ability to use several feature in rnaseq/rnadiff\n          * pin several libaries due to regression during installs\n0.14.2    * Update ribodesigner\n0.14.1    * Kegg enrichment: add gene list \'all\' and fix incomplete annotation case\n          * New uniprot module for GO term enrichment and enrichment\n            refactorisation (transparent for users)\n0.14.0    * pinned click>=8.1.0 due to API change (autocomplete)\n          * moved tests around to decrease packaging from 16 to 4Mb\n          * ribodesigner: new plots, clustering and notebook\n0.13.X    * Remove useless standalones or moved to main **sequana** command\n          * Move sequana_lane_merging into a subcommand (sequana lane_merging)\n          * General cleanup of documentation, test and links to pipelines\n          * add new ribodesigner subcommand\n0.12.7    * Fix memory leak in len() of FastA class\n0.12.6    * remove some rules now in https://github.com/sequana/sequana-wrappers\n0.12.5    * refactorisation of VCF tools/modules to use vcfpy instead of pyVCF\n0.12.4    * complete change log before 0.12.4 in the github /doc/Changelog.txt\n========= ==========================================================================\n',
    'author': 'Thomas Cokelaer',
    'author_email': 'thomas.cokelaer@pasteur.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
