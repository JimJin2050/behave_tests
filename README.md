# behave_tests
1. Install relate python package with pip
pip install -r requirements.txt

2. Execute test cases
behave
or
behave --tags="regression"

3. Generate reports

modify behave.ini

setup allure:
    for macos: brew install allure
    for others, please refer to: https://docs.qameta.io/allure/

install python package:
    pip install allure-behave

generate allure format output:
    behave -f allure_behave.formatter:AllureFormatter -o reports/ ./features
 
show test report:
    allure serve reports/