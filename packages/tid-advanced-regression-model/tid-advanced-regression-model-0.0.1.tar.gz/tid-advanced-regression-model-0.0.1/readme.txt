First install tox:
-pip install tox

To run the test:
-tox run -e test_package

To train:
-tox run -e train

To build:
1. First install build:
-python3 -m pip install --upgrade build

2. Build the package:
-python3 -m build