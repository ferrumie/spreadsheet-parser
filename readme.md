# Team-Granite-Backend
A Spreadsheet Parser

## Run the App: 
- Fork this repository
- Clone to your local machine
- `cd` into the repository and create a virtual environment
- activate the environmment
- Then run `pip  install -r requirement.txt`
- This will download all the dependencies for this application.
<br/>
- <b> Note: Add the name of your virtual environment to the .gitignore file</b>

## Using the service
- We have Pandas as part of the dependencies. 
- Make sure you import pandas. You can import pandas as pd.
- To read the excel run, use this function `pd.read_excel('name of file.xlsx')`
- Please make sure you read the file into a variable, acceptable variable names include `d_frame, df, data_frame, etc.`
- To read the data frame into another another file, use this function `d_frame.to_json(name of file.csv)`
- For more information on how to manipulate data using pandas visit `https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html`

## Contribute guide
If you're in team-granite-backend:
- Add the main repository as an upstream `git remote add upstream https://github.com/hngi/spreadsheet-parser.git`
- Pull the latest version of the repo `git fetch upstream`
- follow this guide `https://medium.com/@topspinj/how-to-git-rebase-into-a-forked-repo-c9f05e821c8a` if lost.
- Create a feature branch with your feature name, e.g: `<user-pagination>`
- Create the your feature locally and commit
- Send a PR after you have test your feature locally with Postman
- Tell us in your PR in bullet points what you have added
- Add yourself as a user to the database (this will eventually count for contribution points)

### requirement.txt content
-alabaster==0.7.12
-asgiref==3.2.9
-astroid==2.4.2
-Babel==2.8.0
-backcall==0.2.0
-beautifulsoup4==4.9.1
-bs4==0.0.1
-certifi==2020.4.5.2
-chardet==3.0.4
-colorama==0.4.3
-coreapi==2.3.3
-coreschema==0.0.4
-coverage==5.1
-cycler==0.10.0
-decorator==4.4.2
-Django==3.0.7
-django-cors-headers==3.4.0
-django-extensions==2.2.9
-django-filter==2.3.0
-django-jenkins==0.110.0
-django-rest-swagger==2.2.0
-djangorestframework==3.11.0
-docutils==0.16
-et-xmlfile==1.0.1
-html5==0.0.9
-idna==2.9
-imagesize==1.2.0
-ipdb==0.13.2
-ipython==7.15.0
-ipython-genutils==0.2.0
-isort==4.3.21
-itypes==1.2.0
-jdcal==1.4.1
-jedi==0.17.0
-Jinja2==2.11.2
-kiwisolver==1.2.0
-lazy-object-proxy==1.4.3
-MarkupSafe==1.1.1
-matplotlib==3.2.1
-mccabe==0.6.1
-mock==4.0.2
-numpy==1.18.5
-openapi-codec==1.3.2
-openpyxl==3.0.3
-packaging==20.4
-pandas==1.0.4
-parso==0.7.0
-pep8==1.7.1
-pickleshare==0.7.5
-prompt-toolkit==3.0.5
-Pygments==2.6.1
-pylint==2.5.3
-pyparsing==2.4.7
-python-dateutil==2.8.1
-pytz==2020.1
-requests==2.23.0
-responses==0.10.15
-scipy==1.4.1
-seaborn==0.10.1
-simplejson==3.17.0
-six==1.15.0
-snowballstemmer==2.0.0
-soupsieve==2.0.1
-Sphinx==3.1.1
-sphinx-rtd-theme==0.4.3
-sphinxcontrib-applehelp==1.0.2
-sphinxcontrib-devhelp==1.0.2
-sphinxcontrib-htmlhelp==1.0.3
-sphinxcontrib-jsmath==1.0.1
-sphinxcontrib-qthelp==1.0.3
-sphinxcontrib-serializinghtml==1.1.4
-sqlparse==0.3.1
-toml==0.10.1
-traitlets==4.3.3
-uritemplate==3.0.1
-urllib3==1.25.9
-wcwidth==0.2.4
-webencodings==0.5.1
-wrapt==1.12.1

