# Python-RPA-Project
Containerized RPA challenge project (rpachallenge.com) made on VSCode with a little help from a mentor.
The project has the below folder structure. In order to run this project, you need to create virtual environment inside this project and install the requirements files. Then create .env file and add your credentials to MongoDB. To run this robot, write "python run.py 0 1 -e dev" in terminal. 

### Project structure

The project should adhere to the below folder structure. Folders should only contain files of the denoted type(s), following the naming conventions.

    .
    ├── libraries               # For implementing keywords that interact with target systems
    │   ├── SystemALibrary.py
    │   ├── SystemBLibrary.py
    │   └── utils.py
    ├── pipelines               # Jenkins pipelines
    │   ├── Jenkinsfile
    │   └── process.groovy
    ├── resources               # Configuration and other resources
    │   ├── settings.py
    │   ├── settings_helpers.py
    │   └── keywords.resource
    ├── scripts                 # Batch/shell cripts for running setup, tests and the process
    │   └── start.(cmd|sh)
    ├── stages                  # Robot workflow split into stages
    │   ├── Stage0.py
    │   └── StageN.py
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
