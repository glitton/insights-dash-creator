# Insights Dashboard Creator

This script uses the New Relic API Explorer to automatically add pre-built dashboards to customers' Insights account.

## Preqrequisites

- Install Python 3+ although this script will also work with python 2.7
  _Note: In most cases, your computer should already have python 2.7 installed (particularly if you are on a Mac). If not, you will need to do some Google research to install._
- Install pip (python install tool) - `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` - `python get-pip.py`

## Install

- Download or git clone this repo into a working directory
  `git clone https://source.datanerd.us/glitton/create-insights-dashboard`
- Add your customers' admin API key and rpm account id to the client_secrets.sh file
- Install Project Requirements

      	*The quickest way to do this is via the following command:*
      	- `cd <PATH_TO_INSIGHTS_DASHBOARD_CREATOR PROJECT>`
      	- `sudo pip install -r requirements.txt`

      	*The much better way to do this is to isolate these packages in a virtual environment:*
      	- `cd <PATH_TO_INSIGHTS_DASHBOARD_CREATOR PROJECT>`
      	- `pip install virtualenv`
      	- `virtualenv env`
      	- `source env/bin/activate`
      	- `pip install -r requirements.txt`

## Launch

1. Navigate to the project repo and type `source env/bin/activate` (if you created a virtual environment which is recommended).
2. Tie in your customer's API key and rpm account id to the project by typing `source client_secrets.sh`.
3. Launch the script by typing `python create_dashboard.py`.

## Results

- Watch terminal for 200 OK Request sent message
- View the new dashboards in your customer's Insights account.
