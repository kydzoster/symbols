# Task Manager
#### CI walkthrough project


## Steps for deployment

##### 1. Create a New project on Heroku
##### 2. ***heroku login*** in Terminal
##### 3. ***heroku apps*** in terminal to check if connection has been established
##### 4. ***git init*** in Terminal
##### 5. Copy ***heroku git:remote -a task-menegeris*** from heroku to set it up in Heroku
##### 6. Create a requirements.txt ***pip3 freeze --local > requirements.txt***
##### 7. ***git add .*** in Terminal
##### 8. ***git commit -m""*** in Terminal
##### 9. Deploy on heroku ***git push heroku master***
##### 10. Create a ***echo web: python app.py > Procfile***
##### 11. add, commit and push to heroku
##### 12. run it ***heroku ps:scale web=1***
##### 13. go to heroku Settings > Reveal config Vars add IP 0.0.0.0 and PORT 5000



## Installations

##### 1. Install ***pip3 install flask-pymongo*** for flask to be able to work with MongoDB
##### 2. Install ***pip3 install dnspython*** for new style connection string for MongoDB

## Libraries, Templates

##### 1. https://materializecss.com/collapsible.html -Accordion, collapsible task bars-
##### 2. https://material.io/resources/icons/?icon=expand_more&style=baseline -Icons from Material.io-
##### 3. Added few more categories in MangoDB Atlas
##### 4. https://materializecss.com/text-inputs.html -Icon Prefixes from Form Templates-
##### 5. https://materializecss.com/switches.html -styled switches-
##### 6. https://materializecss.com/pickers.html -Date picker-
##### 7. https://materializecss.com/select.html -Select options-
##### 8. https://materializecss.com/buttons.html -Submit button-