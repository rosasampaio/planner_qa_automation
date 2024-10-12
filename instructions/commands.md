# Run the test
## Pytest 
- It's a library to testing in Python. It has the main features to know the result about a test scenario.
- It's a powerful tool to test the code.

```
pytest   --alluredir allure-results  -n 2

python3 -m allure server allure-results 

pytest -v --gherkin-terminal-reporter 

```
This command will run all the tests in the project and generate the Allure report in the `allure-results` directory.

# Allure 
- Install from https://allurereport.org/docs/install/

```
allure --version
allure generate --clean
allure open  


```

