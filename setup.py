from distutils.core import setup

setup(
    name="odyssey",
    version="0.1",
    packages=["odyssey"],
    install_requires=[
		"pytest",
		"sphinx",
		"google-cloud-bigquery",
		"parso",
		"joblib",
		"sphinxcontrib-napoleon",
		"nbsphinx",
		"ipython",
    ],
    author="Alan (Yanlin) Duan",
    author_email="duanyanl97@gmail.com",
    description="Tools for analyzing python package usage on GitHub through Google BigQuery",
    license="MIT",
    keywords="package usage analysis BigQuery GitHub",
    url="https://github.com/alan97/odyssey",
)