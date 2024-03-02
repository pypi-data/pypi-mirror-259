from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name             = 'GeoScraper',
    packages         = ['GeoScraper'],
    version          = '0.0.1',
    description      = 'Very user friendly library to parse OpenSourceMap data either from an XML file (i.e. *.osm), from an OSM API URL, or from a user specified bounding box',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author           = 'Power_Broker',
    author_email     = 'gitstuff2@gmail.com',
    url              = 'https://github.com/PowerBroker2/GeoScraper',
    download_url     = 'https://github.com/PowerBroker2/GeoScraper/archive/0.0.1.tar.gz',
    keywords         = ['geospacial', 'map', 'maps', 'mapping', 'osm', 'openstreetmap'],
    classifiers      = [],
    install_requires = ['xmltodict', 'simplekml']
)
