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
- Pull the latest version of the repo `git pull`
- Create a feature branch with your feature name, e.g: `<user-pagination>`
- Create the your feature locally and commit
- Send a PR after you have test your feature locally with Postman
- Tell us in your PR in bullet points what you have added
- Add yourself as a user to the database (this will eventually count for contribution points)

### requirement.txt content
- asgiref==3.2.8
- beautifulsoup4==4.9.1
- bs4==0.0.1
- cycler==0.10.0
- Django==3.0.7
- et-xmlfile==1.0.1
- html5==0.0.9
- jdcal==1.4.1
- kiwisolver==1.2.0
- matplotlib==3.2.1
- numpy==1.18.5
- openpyxl==3.0.3
- pandas==1.0.4
- pep8==1.7.1
- pyparsing==2.4.7
- python-dateutil==2.8.1
- pytz==2020.1
- scipy==1.4.1
- seaborn==0.10.1
- six==1.15.0
- soupsieve==2.0.1
- sqlparse==0.3.1
- webencodings==0.5.1
