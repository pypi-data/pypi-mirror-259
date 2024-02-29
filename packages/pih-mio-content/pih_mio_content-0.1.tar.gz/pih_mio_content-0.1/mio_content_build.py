import shutil
import os
import importlib.util
import sys
from setuptools import setup

import ipih
from pih import PIH
from pih.tools import j

#########################################################################################################
folder = "//pih/facade/dist/mio_content"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as error:
        print("Failed to delete %s. Reason: %s" % (file_path, error))

#This call to setup() does all the work
setup(
    name=j((PIH.NAME, "mio", "content"), "_"),
    version="0.1",
    description="PIH MIO content",
    long_description_content_type="text/markdown",
    url="https://pacifichosp.com/",
    author="Nikita Karachentsev",
    author_email="it@pacifichosp.com",
    license="MIT",
    classifiers=[],
    packages=["MobileHelperContent"],
    include_package_data=True,
    install_requires=["pih"]
)