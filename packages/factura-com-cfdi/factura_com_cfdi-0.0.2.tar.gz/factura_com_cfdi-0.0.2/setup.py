import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.2'
PACKAGE_NAME = 'factura_com_cfdi'
AUTHOR = 'Alexis Yafel Garcia'
AUTHOR_EMAIL = 'a.yafel10@gmail.com'
URL = 'https://github.com/Lexharden'

LICENSE = 'MIT'
DESCRIPTION = 'Librería que consume la API de factura.com para generar facturas fiscales en México.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = ['certifi==2024.2.2',
                    'charset-normalizer==3.3.2',
                    'idna==3.6',
                    'requests==2.31.0',
                    'urllib3==2.2.1']

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    keywords=['factura', 'factura.com', 'API', 'facturación electrónica', 'México', 'CFDI', 'Timbrado'],
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
