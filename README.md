![Index page](/static/wireframe/index.jpg)

![Other pages](/static/wireframe/home.jpg)

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

- ![PC](/static/wireframe/Symbols.pdf)

## FEATURES

**Nav Bar**
 The Nav Bar is fixed at all times, includes a logo and links to 'Symbols'-aka index, 'Home', 'Countries', 'Log In' and 'Register' when not logged in, and 'Symbols', 'Home', 'Countries', 'New Symbol' and 'Log Out' when
logged in. It also collapses on mobile screens. 

**Log In / Register options**
 There are Log in and Registration options in both the collapsable nav bar and standard nav bar.

**Countries**
 The Countries page allows a user to see what countries currently are in the database to avoid useless search for countless of countries with symbols. 

**New Symbol**
 The New symbol allows to insert Country name, Symbol name, Symbol Image and Symbol Description, all fields are mandatory. 

**Footer**
 I dont have a standard footer at the bottom, instead I have a Content Author div at the right side of the screen for mobile and tablets and when viewed from mobiles at the bottom of the page. Content Author section includes social links taking you to the developers GitHub and LinkedIn pages and copyright information with my name.

**Features to be Implemented**

- Edit and Delete only your content.

- Alphabetical search when there are hundreds of countries, currently it is not feasable for a few countries.

- View all symbols by clicking on a country name.

- Adding a country flag image in countries page.

- Saving images on database instead of having them by url, for images on url might be removed which would cause symbol image to disapear.

## TECHNOLOGIES USED

A brief overview of the languages, frameworks, and other tools I've used on this project:

- [Gitpod]
- [CSS3]
- [Bootstrap]
- [Flask]
- [MongoDB]

## TESTING

#### VALIDATORS

- [HTML Validation](https://validator.w3.org/)
- [CSS Validation](https://jigsaw.w3.org/css-validator/)
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)

#### ISSUES

- No errors for style.css and index.css
- There are 8 errors in base.html related to (Illegal character in path segment: { is not allowed).
- All other html documents have errors related to (Illegal character in path segment: { is not allowed).
- All other html documents have errors related to missing (lang and head elements)Using as per advisement prettier beautifier, however, this beautifier uses a lot of spacing and some may think I have overdone it myself, this is not a case.

#### Manual Testing

Manual testing completed by the developer on Desktop, Sony Xperia and Ipad Pro.

1. **Navbar/navigation**
    - When not logged in, the navbar shows - 'Symbols', 'Home', 'Countries', 'Login', 'Register'.
    - Once registered or logged in, the navbar shows - 'Symbols', 'Home', 'Countries', 'New Symbol', 'Logout'.
    - When viewing the site on mobile devices, the navbar becomes a dropdown from a toggle button in the top right hand corner. 
    - At all times the Navbar is fixed to the top of the screen so you can see it at all times. 

2. **Footer**
    - There are a GitHub and LinkedIn icon, when you click on the icons it opens a seperate browser taking you to the developers profiles. 

3. **Log In**
    - Try to Log In leaving one or/and both input fields empty - you will get an error message saying 'Please fill in this field'
    - Try to Log In with credentials having not registered yet - a flash message appears saying 'Login Unsuccessful. Please check your credentials'.
    - Click on the link underneath the form 'Sign up Now', you are taken to the registration page to sign up. 
    - Having already registered, try to log in with either the username inccorect - a flash message appears saying 'Login Unsuccessful. Please check your credentials'.
    - Log in with your correct credentials - you are taken to the homepage and a flash message appaers saying 'You have been logged in!'.

4. **Register**
    - Try to Register leaving one or/and both input fields empty - you will get an error message saying 'Please fill in this field'
    - Try to register with a existing user log in credentials - you will get a flash message saying 'This username is already taken! Please try a different username!'. 
    - Register as a new user with unique information, you will be directed to login page and a flash message will appear saying 'Your account has been created successfuly! You can now Login!'.

5. **Home**
    - When in 'Home' page and you are logged in you can delete or edit content.
    - You click on 'Edit' and it takes you to an 'Edit Book' form, all of the original information autofilled.
    - You are able to change one or all fields. 
    - Try to Edit a book but leave one or/and more input fields empty - you will get an error message saying 'Please fill out this form'.
    - Once edited, click edit book, it takes you to your 'My Books' view with the new version of the book replacing the old. 
    - In 'My Books' click on 'Delete', the book disappears in 'My books' and also on the homepage. 

6. **New Symbol**
    - When you click on 'New Symbol' in the navbar, it takes you to a new form where all fields are required to be filled.
    - Try and submit the form with one of the input fields missing - you will get an error saying 'Please fill out this form'. Do this for every input field. You will get an error
    for every input field except, 'Rating' (as it's default is 5), Comments and 'Share' (as it's default is off).
    - Fill out the form correctly and add, you will be directed to 'Home' page and flash message will appear saying {symbol_name} has been successfuly added to {country_name}.


## DEPLOYMENT

Deployment and source control was entirely done via GitPod and stored on herokuapp and Github.
My repository can be found here:

#### REPO: [https://github.com/kydzoster/symbols](https://github.com/kydzoster/symbols)**

The live site can be found here:

#### HEROKU: [https://simbols.herokuapp.com/](https://simbols.herokuapp.com/)**

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