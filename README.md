# Zadatak 1

For the test to run, `python3` needs to be installed:
Other dependencies that need to be installed are: `pytest`, `pytest-html` and `selenium`.

In order to install them go to the folder `Intis-zadatak-python` that was cloned from the repository and run:

    pip install selenium  
    pip install pytest  
    pip install pytest-html

 inside a terminal to install the selenium module.

To run the test execute the following command in the terminal:

    python -m pytest .\test.py --html=report.html
The test can be run in headless or headed mode.
To change which mode will be run edit the test.py file on line 9.
To run in headless mode set the headless variable to `True`.
To run in headed mode set the headless variable to `False`.

The report will be generated in the folder and named: `report.html`