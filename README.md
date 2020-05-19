<div style="text-align: center;">

# Database for Pagan Symbols

<p>DPS(Database for Pagan Symbols) is a fully responsive, user based, database for pagan symbols.
You can search for any Country and see if database contains any symbols for that country. 
If that country canot be found, that means that there are no symbols for that country, then you have an option to add one.
To add, edit or delete symbols, you have to be logged in.</p>

</div>


## Tabel of Contents

[**Project Goals**](#project-goals)

[**User Goals**](#user-goals)

[**User Stories**](#user-stories)

[**Design Choices**](#design-choices)

[**Wireframes**](#wireframes)

[**Features**](#features)

[**Technologies used**](#technologies-used)

[**Testing**](#testing)

[**Deployment**](#deployment)

[**Credits**](#credits)


## UX

### Project Goals

To create a site that contains all Pagan symbols in one database.
To allow the user to read and add a Pagan Symbols not only for his/her country, but also for other countries.

### User Goals

I want to have a place online where I or anyone else could store Pagan Symbols and learn about other countries Pagan symbols. 

### User Stories

As a user I want...

* To be able to register quickly without the site taking any unnecessary information.
* To be able to find country and it's Pagan Symbols.
* To be able to see the list of countries currently in database.
* To be able to navigate around the site with ease.
* To be able to read, add, edit or delete any symbols in database.

### Design Choices

I have decided to go for a simple Bootstrap design. The demographic of my users are anyone interested in Pagan Symbols.
Therefore, site should be easy on eye, with no bright or flashing colours.

1. Font
* The font I chose was 'Skranji' due to it's 'Pagan looks' for Headings and Roboto for other text. 

2. Colours
* I chose SteelBlue as my main colour because it is known as a very calm colour.
* I chose #fafafa background for its simplicity and dark headings
* I chose blue delete button and greedn edit button
* I chose green flash messages for success and red for errors

3. Styling
* Bootstrap.


## Wireframes 

All Wireframes were made using [Balsamiq](https://balsamiq.com/)

* [Symbols Desktop (pdf)]()

* [Symbols Mobile (pdf)]()


## Features

+ Nav Bar
 The Nav Bar is fixed at all times, includes a logo and links to 'Symbols'-aka index, 'Home', 'Countries', 'Log In' and 'Register' when not logged in, and 'Symbols', 'Home', 'Countries', 'New Symbol' and 'Log Out' when
logged in. It also collapses on mobile screens. 

+ Log In / Register options.
 There are Log in and Registration options in both the collapsable nav bar and standard nav bar.

+ Countries.
 The Countries page allows a user to see what countries currently are in the database to avoid useless search for countless of countries with symbols. 

+ New Symbol.
 The New symbol allows to insert Country name, Symbol name, Symbol Image and Symbol Description, all fields are mandatory. 

+ Footer.
 The Footer includes copyright information in regards to the site and social links taking you to the developers GitHub and LinkedIn pages.


## Features left to Implement

+ Edit and Delete only your content.

+ Alphabetical search when there are hundreds of countries, currently it is not feasable for a few countries.

+ View all symbols by clicking on a country name.

+ Adding a country flag image in countries page.

+ Saving images on database instead of having them by url, for images on url might be removed which would cause symbol image to disapear.


## Technologies used

* HTML5
* CSS3
* Python

* [MongoDB](https://www.mongodb.com/)

* [Bootstrap](https://getbootstrap.com/)
* Jquery
* flask
* flask_pymongo
* bson.objectid
* brycpyt

* [Google Fonts](https://fonts.google.com/)
* [The W3C Markup Validation Service](https://validator.w3.org/)
* [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/)

* [GitPod](https://gitpod.io/workspaces/)
* [GitHub](https://github.com/kydzoster)


## Testing

I began my testing using.. 

- [HTML WC3 Markup Validation Service.](https://validator.w3.org/)
- [CSS WC3 Markup Validation Service](https://jigsaw.w3.org/css-validator/)

#### CSS Validation bugs:

- No errors for style.css

#### HTML Validation bugs:

- There are 8 errors in base.html related to (Illegal character in path segment: { is not allowed).
- All other html documents have errors related to (Illegal character in path segment: { is not allowed).
- All other html documents have errors related to missing (lang and head elements)

#### Client Stories Testing

1. To be able to register quickly without the site taking any unneccesary information.
* When signing up to the site I am currently only asking for a 'Username' and 'Password' to be able to edit or create content.
2. To be able to find country containing any symbols.
* Index page aka Symbols page contains search bar, home page contains all symbols in the database and Countries page contains only countries currently in the database.
3. To be able to navigate around the site with ease.
* The site's navigation bar is fixed therefore it is very obvious how to navigate from page to page.
4. To be able to edit or delete enties, only available when logged in.
* To edit or delete symbol can be done only from Home page.
5. To be able to add content when discovered that country does not exist, this will offer to add it if you are logged-in and transfer you to add symbol page, otherwise it will offer to log in if not logged in.
 
#### Manual Testing

Manual testing completed by the developer on Desktop, Sony Xperia and Ipad Pro.

1. Navbar/navigation
* When not logged in, the navbar shows - 'Symbols', 'Home', 'Countries', 'Login', 'Register'.
* Once registered or logged in, the navbar shows - 'Symbols', 'Home', 'Countries', 'New Symbol', 'Logout'.
* When viewing the site on mobile devices, the navbar becomes a dropdown from a toggle button in the top right hand corner. 
* At all times the Navbar is fixed to the top of the screen so you can see it at all times. 

2. Footer
* There are a GitHub and LinkedIn icon, when you click on the icons it opens a seperate browser taking you to the developers profiles. 
* Above the footer is an up arrow, once clicked it takes you back to the top of the homepage. 

3. Log In
* Try to Log In leaving one or/and both input fields empty - you will get an error message saying 'Please fill in this field'
* Try to Log In with credentials having not registered yet - a flash message appears saying 'Login Unsuccessful. Please check your credentials'.
* Click on the link underneath the form 'Sign up Now', you are taken to the registration page to sign up. 
* Having already registered, try to log in with either the username inccorect - a flash message appears saying 'Login Unsuccessful. Please check your credentials'.
* Log in with your correct credentials - you are taken to the homepage and a flash message appaers saying 'You have been logged in!'.

4. Register
* Try to Register leaving one or/and both input fields empty - you will get an error message saying 'Please fill in this field'
* Try to register with a existing user log in credentials - you will get a flash message saying 'This username is already taken! Please try a different username!'. 
* Register as a new user with unique information, you will be directed to login page and a flash message will appear saying 'Your account has been created successfuly! You can now Login!'.

5. Home
* When in 'Home' page and you are logged in you can delete or edit content.
* You click on 'Edit' and it takes you to an 'Edit Book' form, all of the original information autofilled.
* You are able to change one or all fields. 
* Try to Edit a book but leave one or/and more input fields empty - you will get an error message saying 'Please fill out this form'.
* Once edited, click edit book, it takes you to your 'My Books' view with the new version of the book replacing the old. 
* In 'My Books' click on 'Delete', the book disappears in 'My books' and also on the homepage. 

6. New Symbol
* When you click on 'New Symbol' in the navbar, it takes you to a new form where all fields are required to be filled.
* Try and submit the form with one of the input fields missing - you will get an error saying 'Please fill out this form'. Do this for every input field. You will get an error
for every input field except, 'Rating' (as it's default is 5), Comments and 'Share' (as it's default is off).
* Fill out the form correctly and add, you will be directed to 'Home' page and flash message will appear saying {symbol_name} has been successfuly added to {country_name}.


## Deployment

#### I developed this project using the GitPod, committing to Git and pushing to GitHub via the locally installed Git commands. 


## Credits

### Content

All content written in this project was written by the developer.

### Media

- Symbol images are URL from web.

### Acknowledgements

Big thanks to Slack users, especially to 'Igor' for helping with symbol insert code.
Huge help received from discord communities, without their help I would have not been able to improve my coding and understanding of flask.
Thank you youtube for countles examples of user authentication and searchbar.