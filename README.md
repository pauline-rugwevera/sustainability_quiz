# SUSTAINABILITY QUIZ
Are you walking the talk when it comes to sustainability? The sustainability quiz is a game built using python to test the users their understanding of what sustainability is all about.

[Link to live website](https://sustainability-quiz-app.herokuapp.com/)
# UX
* The sustainability quiz is a quiz game intended for anyone who understands or willing to understand how things like global warming, enviromental issues are posing concerns to the current and future generations and how exactly businesses have to respond to address these issues so they remain sustainable. I tried to make sure the questions are short, precise and funny for the users.

## Site Goals
- To educate users about sustainability through a funny quiz
- To provide users with a range of randomised questions each time they play
- To provide users ability to see how they perfomed

## User Stories
### New user
- As a new user, I want to understand more about sustainability
- As a new user, I want to compare my knowledgge against other users
- As a new user, I want to play a unique quiz game

### Returning user
- Users will be looking to see if any additional functionality has been added

# Features

# Testing

# Deployment

My game was deployed via Heroku as follows:
- Sign in to Heroku
- Select New and Create New App
- For app name, I put sustainability-quiz-app and chose Europe for region then create app
- Select the created app from the dashboard and navigate to Settings
- Scroll down to config vars and click reveal config vars, I set two Config Vars, one is CREDS.json file, and the other is to set the PORT to 8000
- Scroll down and buildpack button. Select python as the first buildpack and node.js as the second
- Navigate to Deploy tab at the top of the page
- For the deployment method, select Github. If access hasn't already been configured, do this from Account settings > Applications > Third-party Services.
- Enter the repository name, I put sustainability-quiz-app and selected search then click connect
- Confirm the correct branch and choose either to automatically or manually deploy your app. In this case I manually deployed so I clicked manual deploy.
- The build process will begin and a message "Your app was successfully deployed" will appear and a link to the live site

# Credit
## Content
The following sites were used for the quiz questions:

- https://assets.new.siemens.com/siemens/assets/api/uuid:51501a0c-4856-4f7e-a84f-d313b9781067/5-2-sustainability-quiz-answers.pdf

- https://www.theguardian.com/global/2017/jul/30/lucy-siegle-great-green-quiz

- https://www.yeovalley.co.uk/sustainability-quiz/

- https://mcqslearn.com/o-level/environmental-management/environmental-sustainability-mcqs.php


## Code
The time this python module came by, I was still wrapping around my mind with Javascript and jumping from it to python gave me some hard time. I went through various blogs and tutorials just to understand a few concepts before embarking on this project. Most stuff was too complicated for a python newbie however there is my favourite web development and python youtuber who made me understand what I wanted to do in a matter of a few minutes, thanks to[Giraffe Academy](https://www.youtube.com/watch?v=SgQhwtIoQ7o&list=LL&index=6&t=160s) with Mike Dane. 

The code to validate the user input name is from [Stackoverflow](https://stackoverflow.com/questions/36432954/python-validation-to-ensure-input-only-contains-characters-a-z). At first I used the if else statements however the second time a user entered an invalid input it would pass through which was not ideal.

To understand the gspread, first had to go through Code Institute's love sandwiches tutorial twice then went through [gspread](https://docs.gspread.org/en/latest/) documentation to get a full grasp.

## Acknowledgements
- Love sandwiches tutorial
- If there is one thing Code Institute has done best for its students, is its slack community
- My mentor