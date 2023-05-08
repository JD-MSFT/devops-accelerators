# Welcome to my Greeter App!

The Greeter Application will ask for your name and job title, and return a customized response!

# Developer Details

## Start the application locally
python -m venv env
source env/Scripts/activate
pip install -r requirements.txt
python app.py

This application uses feature flags to more granularly control deployments. Be sure to include an .env file- check example.env for reference.

## Automation
The dev.workflow is a CI process which will check code for linting, formatting, and ensure it passes unit tests. Configure Black Formatter locally, and regularly check that your unit tests are passing (python -m pytest).

When happy with any changes in a feature branch, create a Pull Request to development. If accepted, the changes will be reflected in the staging App Service url.