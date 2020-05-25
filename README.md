![Home page](/static/wireframe/home.jpg)

#### **[Live Site](https://simbols.herokuapp.com/)**

# Pagan Symbol Database

Pagan Symbol Database is a fully responsive, user based, database for pagan symbols.

You can search for any Country and see if database contains any symbols for that country. 

If that country canot be found, that means that there are no symbols for that country inside our Database, then you have an option to add one.

To add, edit or delete symbols, you have to be logged in.

---

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Framework**](#framework)
    - [**Color Scheme**](#color-scheme)
    - [**Mockups**](#Mockups)

2. [**Features**](#features)
    - [**Features to be Implemented**](#Features-to-be-Implemented)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Issues**](#issues)
    - [**Manual Testing**](#manual-testing)

5. [**Deployment**](#deployment)
    - [**Repo**](#repo)
    - [**Heroku**](#heroku)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

## UX

#### PROJECT GOALS

To create a site that contains all Pagan symbols in one database.
To allow the user to read and add a Pagan Symbols not only for his/her country, but also for other countries.

#### USER STORIES

As a user I want to be able to:

- find country and it's Pagan Symbols.
- see the list of countries currently in database.
- navigate around the site with ease.
- register quickly without the site taking any unnecessary information.
- read, add, edit or delete any symbols in database.

#### FRAMEWORK

- **Bootstrap**: I prefer to use Bootstrap as it is easy and have consistency. It is complemented with custom css.

#### COLOR SCHEME

- SteelBlue(5f788a) as my main colour for navbar.
- fafafa for background.
- 444444 for headings.
- 161616 for body text.
* Boostrap colours:
    - Blue as info for Delete button.
    - Green as success for Edit, Search and success messages.
    - Red as danger for error messages

#### MOCKUPS
All Wireframes were made using [Balsamiq](https://balsamiq.com/)
Link is not broken, its in pdf format and has rendering problems, but when clicked on it will open it.
- ![PC](/static/wireframe/Symbols.pdf)

## FEATURES

**Nav Bar**
 The Nav Bar is fixed at all times, includes a brand name 'Symbols'-aka index, 'Home', 'Countries', 'Log In' and 'Register' when not logged in, and 'Symbols', 'Home', 'Countries', 'New Symbol' and 'Log Out' when
logged in. It also collapses on mobile screens. 

**Log In / Register options**
 There are Log in and Registration options in both the collapsable nav bar and standard nav bar.

**Countries**
 The Countries page allows a user to see what countries currently are in the database to avoid useless search for countless of countries with symbols. 

**New Symbol**
 The New symbol allows to insert Country name, Symbol name, Symbol Image and Symbol Description, all fields are mandatory. 

**Footer**
 I dont have a standard footer at the bottom, instead I have a Content Author div at the right side of the screen for mobile and tablets and when viewed from mobiles at the bottom of the page. Content Author section includes social links taking you to the developers GitHub and LinkedIn pages and copyright information with developers name.

**Search**
At this moment you can search only for a Country name, other names will promt for adding them if these names are not already in Database.

**Features to be Implemented**

- Edit and Delete only your content.

- Alphabetical search when there are hundreds of countries, currently it is not feasable for a few countries.

- View all symbols under that country when clicked on its name.

- Adding a country flag image in countries page.

- Saving images on database instead of having them by url, for images on url might be removed which would cause symbol image to disapear.

## TECHNOLOGIES USED

A brief overview of the languages, frameworks, and other tools I've used on this project:

- [Gitpod](https://www.gitpod.io/) - Gitpod is an online IDE(Integrated development environment) which can be launched from any GitHub page. Within seconds, Gitpod provides you with a fully working development environment, including a VS Code-powered IDE and a cloud-based Linux container configured specifically for the project at hand.
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language like HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask is a lightweight WSGI(Web Server Gateway Interface) web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
- [MongoDB](https://www.mongodb.com/) - MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.

## TESTING

#### VALIDATORS

- [HTML Validation](https://validator.w3.org/)
- [CSS Validation](https://jigsaw.w3.org/css-validator/)
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)

#### ISSUES

- During development time, Gitpod did not recognised flask or pymongo. To resolve that problem I had to use same project as a development and as a testing field with multiple codes from diferent angles with their respective libraries, eg. Alchemy.
- No errors for style.css and index.css
- There are 8 errors in base.html related to (Illegal character in path segment: { is not allowed).
- All other html documents have errors related to (Illegal character in path segment: { is not allowed).
- All other html documents have errors related to missing (lang and head elements).

#### Manual Testing

Manual testing completed by the developer on Desktop, Sony Xperia and Ipad Pro.

1. **Navbar/navigation**
    - When not logged in, the navbar shows - 'Symbols', 'Home', 'Countries', 'Login', 'Register'.
    - Once registered or logged in, the navbar shows - 'Symbols', 'Home', 'Countries', 'New Symbol', 'Logout', searchbar.
    - When viewing the site on mobile devices, the navbar becomes a dropdown from a toggle button in the top right hand corner. 
    - At all times the Navbar is fixed to the top of the screen so you can see it at all times. 

2. **Content Author**
    - There are a GitHub and LinkedIn icon, when you click on the icons it opens a seperate browser taking you to the developers profiles. 

3. **Log In**
    - Try to Log In leaving one or/and both input fields empty - you will get an error message saying *'Please fill in this field'*
    - Try to Log In with credentials having not registered yet - a flash message appears saying *'Login Unsuccessful. Please check your credentials'*.
    - Click on the link underneath the form *'Sign up Now'*, you are taken to the registration page to sign up. 
    - Having already registered, try to log in with either the username inccorect - a flash message appears saying *'Login Unsuccessful. Please check your credentials'*.
    - Log in with your correct credentials - you are taken to the homepage and a flash message appaers saying *'You have been logged in!'*.

4. **Register**
    - Try to Register leaving one or/and both input fields empty - you will get an error message saying *'Please fill in this field'*
    - Try to register with an existing user log in credentials - you will get a flash message saying *'This username is already taken! Please try a different username!'*. 
    - Register as a new user with unique username, you will be directed to login page and a flash message will appear saying *'Your account has been created successfuly! You can now Login!'*.

5. **Home**
    - When in 'Home' page and you are logged in you can delete or edit content.
    - You click on 'Edit' and it takes you to an 'Edit Symbol' form, all of the original information autofilled except image url.
    - Try to Edit a Symbol but leave one or/and more input fields empty - you will get an error message saying *'Please fill in this field'*.
    - Once edited, click *update*, it takes you to your 'Home' page with the new version of the Symbol replacing the old. 
    - In 'Home' click on 'Delete', the Symbol disappears from 'Home' page. 

6. **New Symbol**
    - When you click on 'New Symbol' in the navbar, it takes you to a new form where all fields are required to be filled.
    - Try and submit the form with one of the input fields missing - you will get an error saying *'Please fill out this field'*.
    - Fill out the form and click on 'Add Symbol', you will be directed to 'Home' page and flash message will appear saying {symbol_name} has been successfuly added to {country_name}.

7. **searchbar**
    - When you use searchbar on index page or any other page where searchbar is accessible, you type in Country name, if typed any other name it will say *This name is not in our DataBase, would you like to **add** it?*

## DEPLOYMENT

Deployment and source control was entirely done via GitPod and stored on herokuapp and Github.
My repository can be found here:

#### REPO: [https://github.com/kydzoster/symbols](https://github.com/kydzoster/symbols)**

The live site can be found here:

#### HEROKU: [https://simbols.herokuapp.com/](https://simbols.herokuapp.com/)**
To replicate follow these steps:

    + Inside Github, right hand side, click on the green button *Gitpod*
    + wait untill it opens, when code has been uploaded on your Gitpod execute command:    
        pip3 install -r requirements.txt
    + Next, go to [Heroku](https://dashboard.heroku.com/apps) and create an account if you dont have one, then:

        - 1. Create a New project on Heroku
        - 2. ***heroku login*** in Gitpod Terminal
        - 3. ***heroku apps*** in terminal to check if connection has been established
        - 4. ***git init*** in Terminal
        - 5. ***git add .*** in Terminal
        - 6. ***git commit -m""*** in Terminal
        - 7. Copy ***heroku git:remote -a yourappnamegoeshere*** from heroku to set it up in Heroku
        - 8. Deploy on heroku ***git push heroku master***
        - 9. run it ***heroku ps:scale web=1***
        - 10. go to heroku Settings > Reveal config Vars add IP 0.0.0.0 and PORT 5000
        - 11. deploy from heroku

## CREDITS

#### CONTENT

Content in this project was written by developer.
#### MEDIA

- Symbol images are URL from web.

#### ACKNOWLEDGEMENTS

- Big thanks to Slack user 'Igor' for helping with symbol insert code and other codes.

- Huge help received from discord communities, without their help I would have not been able to improve my coding and understanding of flask.

- Thank you youtube for countles examples of user authentication and searchbar.

    **Specific Sources**
    - User login/register system (https://www.youtube.com/watch?v=vVx1737auSE&t=903s)

    - Data centric module from Code Institute