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



