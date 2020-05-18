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

* [Symbols Desktop]()
* [Home Desktop]()    
* [Countries Desktop]()
* [Log in Desktop]()
* [Register Desktop]()
* [New Symbol Desktop]()
* [Logout Desktop]()

* [Symbols Mobile]()
* [Home Mobile]()    
* [Countries Mobile]()
* [Log in Mobile]()
* [Register Mobile]()
* [New Symbol Mobile]()
* [Logout Mobile]()


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

* [Materialize](https://getbootstrap.com/)
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
* When signing up to the site I am currently only asking for a 'Username' and 'Password' to set up. As there is no purchasing from the site, I currently do not need anymore
    of their personal information. 
2. To be able to find new books I haven't read before.
* On the homepage is a library of all the books users have uploaded and decided to share. 
3. To be able to see the Genre and rating of new books so there is enough information for me to decide whether I would enjoy it. 
* Each book is displayed on a card, on this card are tabs displaying more information about the books. These fields have been set as 'required', so there will always be
  Genre and Rating information on each book on the site. 
4. To be able to navigate around the site with ease.
* The site's navigation bar is fixed therefore it is very obvious how to navigate from page to page. Also there is an option to 'Register' in the footer.
5. To be able to edit or delete my added books with ease.
* In the 'My Books' view, each book has an 'Edit' or 'Delete' button, when you choose to edit a book, it is required to input your username, this way the book will stay in 
  your 'My Books' view, and replace the old version of the book. 
6. To know that I am the only person able to edit my books that I have added.
* The Edit and Delete buttons only show up in the 'My Books' view, and you can only see 'My Books' when you are logged in. The books shows in the 'My Books' view, are only
  the books you have uploaded whilst being logged in. 
7. To know my books will be saved when I log out, so when I revisit the site, my books are still there.
* All books are save inthe MongoDB Atlas databse therefore will always be rendered to the site if added to the database. 

#### Manual Testing

Below is a checklist completed by the developer and 2 third parties. The checklist was completed on all devise sizes. 

1. Navbar/navigation
* When not logged in, the navbar shows - 'Home', 'Log In', 'Register'.
* Once registered or logged in, the navbar shows - 'Home', 'Add Book', 'My Books', 'Log Out'.
* When viewing the site on medium or small screens, the navbar becomes a dropdown from a toggle button in the top left hand corner. 
* At all times the Navbar is fixed to the top of the screen so you can see it at all times. 

2. Footer
* In the footer you have a link called 'Register' that takes you to the 'Register Form'. 
* There are also a GitHub and LinkedIn icon, when you click on the icons it opens a seperate browser taking you to the developers profiles. 
* Above the footer is an up arrow, once clicked it takes you back to the top of the homepage. 

3. Log In
* Try to Log In leaving one or/and both input fields empty - you will get an error message saying 'Please fill out this form'
* Try to Log In with credentials having not registered yet - an error message appears saying 'Incorrect username/password'.
* Click on the link underneath the form 'Sign up here', you are taken to the registration page to sign up. 
* Having already registered, try to log in with either the username inccorect - an error message appears saying 'This username does not exist'. I haven't specified which for added security. 
* Log in with your correct credentials - you are taken to the homepage and now have the option to 'Add Book' or view 'My Books' in the navbar. 

4. Register
* Try to Regitser leaving one or/and both input fields empty - you will get an error message saying 'Please fill out this form'
* Try to register with a existing user log in credentials, both username and password, and then just the correct username, and just the correct password - you will get an error saying 'This username already exists'. 
* Register as a new user with unique information, you will be taken to the homepage, you will have an 'Add Book' and a 'My Books' view, the 'My Books' view is empty. 
* Fill out the 'Add Book' form, click share, log out, log back in with your new user information. You will see you added book in your 'My Books' view and on the homepage. 

5. My Books
* When in your 'My Books' view, you have 'Edit' and 'Delete' buttons below each of your book entries.
* You click on 'Edit' and it takes you to an 'Edit Book' form, all of the original information autofilled.
* You are able to change one or all fields. 
* Try to Edit a book but leave one or/and more input fields empty - you will get an error message saying 'Please fill out this form'.
* Once edited, click edit book, it takes you to your 'My Books' view with the new version of the book replacing the old. 
* In 'My Books' click on 'Delete', the book disappears in 'My books' and also on the homepage. 

6. Add Book
* When you click on 'Add Book' in the navbar, it takes you to a form headed 'Add Book'
* Try and submit the form with one of the input fields missing - you will get an error saying 'Please fill out this form'. Do this for every input field. You will get an error
for every input field except, 'Rating' (as it's default is 5), Comments and 'Share' (as it's default is off).
* Fill out the form correctly and click share, your new book will render in your 'My Books' view and the homepage. Do this again and do not share, the book will only render on
your 'My Books' view. 

#### Bugs discovered during manual testing from a third party

No bugs or problems from the third party manual testing.

#### Bugs Disovered during manual testing from the developer

1. TESTING RESPONSIVENESS 
* When on looking at the site on Google Dev tools on the responsive mode, the carousel on the front page doesn't seem to change size like it should when you change screen sizes.
You have to refresh every time to see how the carousel actually looks on that screen size. Still have not solved this issue as it doesn't seem to be a problem with my code. 
All sizes given to the carousel are correct and are user friendly and responsive on all screens. 
* Solution - I spoke to my mentor Spencer Barriball about this, we think it is a bug within the carousel itself and I was told not to worry as it renders
properly and has been styled properly on my side so will look fine on each devise for the user. 

## Deployment

#### I developed this project using the GitPod, committing to Git and pushing to GitHub via the locally installed Git commands. 

#### The following steps are how to create an app in heroku and connect it to 

- Login to heroku and go into your personal apps.
- Click **New** in the top right corner and create a new app, pick your closest region.
- In your CLI associate the heroku application as our remote master branch - heroku git:remote - a [app name]

#### The following steps run through how I deployed this project to [Heroku.](https://dashboard.heroku.com/) 

- Add a requirements file (list of applications heroku requires to run the app) - **pip3 freeze --local > requirements.txt**
- Git add and commit requirements file
- Add a Procfile (we need to tell heroku which file is used as our entry point to the app) - **echo web: python app.py > Procfile**
- Git add and commit requirements file
- Push to Github and Heroku - **git push origin master && git push heroku master**
- Tell Heroku to get the app up and running - **heroku ps:scale web=1**
- Go to settings in Heroku - Reveal config vars - Put in IP and PORT values (remember if the values are IP: 0.0.0.0, PORT: 5000)
- Open app. 

#### Running this project locally... 

1. Log into your GitHub
2. Find the repository via this link [I-brary](https://github.com/sw1ckham/i-brary)
3. Click on **clone or download**, copy the clone URL under **clone with HTTPS**.
4. Open up your IDE, and open **git bash**
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type **git clone**, and then paste the URL you copied. example: **$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY**
7. Press Enter. Your local clone will be created.

## Credits

### Content

All content written in this project was written by the developer.

### Media

- I sourced all photos for the books from online mainly google images and copied the image url. 

- All icons came from [Materialize's library](https://materializecss.com/icons.html) 

### Code 
* Retrieved the [code](https://materializecss.com/cards.html) for my books cards from materialze and Edited.  
* This [Stack Overflow post](https://stackoverflow.com/questions/50671682/center-align-items-in-materializecss-row) helped me center the cards on index.html.*
* I used [CSS matic](https://www.cssmatic.com/box-shadow) to create my box shadows
* I used [W3 Schools](https://www.w3schools.com/tags/att_textarea_maxlength.asp) to help me work out how to apply a max-length to a text area.
* I used [Autoprefixer](https://autoprefixer.github.io/) to add broswer prefixes to my CSS code. 

### Acknowledgements

Thank you very much to my mentor Spencer who helped me throughout. 
Also to the student care tutors Tim, Stephen, Samantha, Cormac and Kevin. 
'Igor' on Slack who was always quick to lend a hand. 

