# Python-RPA-Project
RPA challenge project (rpachallenge.com) was made on VSCode with a little help from a mentor.
The project has the below folder structure. In order to run this project, you need to create virtual environment inside this project and install the requirements files. Then create .env file and add your credentials to MongoDB. To run this robot, write "python run.py 0 1 -e dev" in terminal. 

### What does this robot do?
The purpose of the robot is to insert data to form on web page. The robot goes to RPA Challenge site: https://rpachallenge.com/. Fetches personal data from 10 persons on CSV file and inserts their information into form and pushes Submit button after every submittion.


### Project structure

The project should adhere to the below folder structure. Folders should only contain files of the denoted type(s), following the naming conventions.

    .
    ├── libraries               # For implementing keywords that interact with target systems
    │   ├── LibraryBase.py
    │   ├── RPAChallengeLibrary.py
    │   └── utils.py
    ├── pipelines               # Jenkins pipelines
    │   ├── Jenkinsfile
    │   └── process.groovy
    ├── resources               # Configuration and other resources
    |   |__ locators.py
    │   ├── settings.py
    │   ├── settings_helpers.py
    │   └── keywords.resource
    ├── scripts                 # Batch/shell scripts for running setup, tests and the process
    │   └── start.(cmd|sh)
    ├── stages                  # Robot workflow split into stages
    │   ├── Stage0.py
    │   └── Stage1.py
    |   |__ Stage2.py
    ├── tasks                   # Robot Framework workflows
    │   └── main.robot
    ├── tests                   # Unit tests
    │   └── test.py
    ├── .gitignore
    ├── .pylintrc
    ├── .rflintargs
    ├── requirements.txt
    ├── requirements-dev.txt
    ├── requirements-tests.txt
    ├── run.py
    ├── setup.cfg
    ├── setup.py
    |__ .env
    └── README.md
