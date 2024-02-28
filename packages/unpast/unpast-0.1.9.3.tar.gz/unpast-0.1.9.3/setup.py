# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['unpast', 'unpast.utils']

package_data = \
{'': ['*']}

install_requires = \
['fisher==0.1.10',
 'jenkspy==0.2.0',
 'kneed>=0.8.3,<0.9.0',
 'matplotlib-venn==0.11.6',
 'numba==0.55.2',
 'numpy==1.22.3',
 'pandas==1.4.2',
 'python-louvain==0.15',
 'scikit-learn==1.1.0',
 'scikit-network==0.25.0',
 'scipy==1.7.3',
 'statsmodels==0.13.2']

entry_points = \
{'console_scripts': ['run_unpast = unpast.run_unpast:main']}

setup_kwargs = {
    'name': 'unpast',
    'version': '0.1.9.3',
    'description': 'A novel method for unsupervised patient stratification.',
    'long_description': '# UnPaSt\n\nUnPaSt is a novel method for identification of differentially expressed biclusters.\n\n![alt text](./poster/DESMOND2_steps2.png)\n\n\n## Requirements:\n<pre>\nPython:\n    fisher==0.1.10\n    jenkspy==0.2.0\n    matplotlib-venn==0.11.6\n    numba==0.55.2\n    numpy==1.22.3\n    scikit-learn==1.1.0\n    scikit-network==0.25.0\n    scipy==1.7.3\n    statsmodels==0.13.2\n    pandas==1.4.2\n    python-louvain==0.15\n    statsmodels==0.13.2\n\nR:\n    WGCNA>=1.70-3\n    limma>=3.42.2\n</pre>\n\n\n## Installation\n* UnPaSt can be installed using `pip`, `poetry`, or run using `Docker`, or as a script (see examples section). Follow the appropriate instructions below for your preferred method. You need to have R and **Python 3.8-3.10** installed.\n\n1. Using **pip**: \\\n    To install the project using `pip`, first make sure you have `pip` installed on your system. If you haven\'t installed it already, you can find the installation instructions [here](https://pip.pypa.io/en/stable/installation/). \\\n    Once `pip` is installed, you can install UnPaSt by running the following command:\n\n    ```bash\n    pip install unpast\n    ```\n    Run it:\n    ```bash\n    run_unpast -h\n    ```\n    **Dependencies**. To use this package, you will need to have R and the [WGCNA library](https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/) and [limma](https://bioconductor.org/packages/release/bioc/html/limma.html) installed. You can easily install these dependencies by running the following command after installing unpast:\n    ```bash\n    python -m unpast.install_r_dependencies\n\n    # or you can install it directly\n    R -e "install.packages(\'BiocManager\'); BiocManager::install(c(\'WGCNA\', \'limma\'))"\n    ```\n\n2. Installation using **Poetry**: \\\n    To install the package using Poetry, first make sure you have Poetry installed, clone the repo and run:\n    ```bash\n    poetry add unpast\n    ```\n    Run it:\n    ```bash\n    poetry run run_unpast -h\n    ```\n    **Dependencies**. To use this package, you will need to have R and the [WGCNA library](https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/) and [limma](https://bioconductor.org/packages/release/bioc/html/limma.html) installed. You can easily install these dependencies by running the following command after installing unpast:\n    ```bash\n    poetry run python -m unpast.install_r_dependencies\n\n    # or you can install it directly\n    R -e "install.packages(\'BiocManager\'); BiocManager::install(c(\'WGCNA\', \'limma\'))"\n    ```\n3. Running with **Docker**: \\\n    You can also run the package using Docker. First, pull the Docker image:\n    ```bash\n    docker pull freddsle/unpast:latest\n    ```\n    Next, run the UnPaSt:\n    ```bash\n    docker run -v /your/data/path/:/user_data/ freddsle/unpast:latest --exprs /user_data/exprs.tsv --out_dir /user_data/out_dir/\n    ```\n\n\n## Examples\n* UnPaSt requires a tab-separated file with features (e.g. genes) in rows, and samples in columns. Feature and sample names must be unique. \n\n<pre>\n\ncd test;\nmkdir -p results;\n\n# running UnPaSt with default parameters and example data\npython ../run_unpast.py --exprs scenario_B500.exprs.tsv.gz --basename results/scenario_B500\n\n# with different binarization and clustering methods\npython ../run_unpast.py --exprs scenario_B500.exprs.tsv.gz --basename results/scenario_B500 --binarization ward --clustering Louvain\n\n# help\npython run_unpast.py -h\n</pre>\n\n## Outputs\n* \\<basename\\>.[parameters].biclusters.tsv - a .tsv table with found biclsuters, where \n    - the first line starts from \'#\' and stores parameters\n    - each following line represents a bicluster\n    - SNR column contains SNR of a bicluster \n    - columns "n_genes" and "n_samples" provide the numbers of genes and samples, respectively \n    - "gene","sample" contain gene and sample names respectively\n    - "gene_indexes" and  "sample_indexes" - 0-based gene and sample indexes in the input matrix.\n* binarized expressions, background distributions of SNR for each bicluster size and binarization statistics [if clustering is WGCNA,  or  \'--save_binary\' flag is added]\n\n## About \nUnPaSt is an unconstrained version of DESMOND method ([repository](https://github.com/ozolotareva/DESMOND), [publication](https://academic.oup.com/bioinformatics/article/37/12/1691/6039116?login=true))\n\nMajor modifications:\n * it does not require the network of feature interactions \n * UnPaSt clusters individual features instead of pairs of features\n * uses 2-means, hierarchicla clustering or GMM for binarization of individual gene expressions\n * SNR threshold for featuer selection is authomatically determined; it depends on bicluster size in samples and user-defined p-value cutoff\n \n## License\nFree for non-for-profit use. For commercial use please contact the developers. \n',
    'author': 'Olga Zolotareva (ozolotareva)',
    'author_email': 'None',
    'maintainer': 'Olga Zolotareva (ozolotareva)',
    'maintainer_email': 'None',
    'url': 'https://github.com/ozolotareva/DESMOND2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
