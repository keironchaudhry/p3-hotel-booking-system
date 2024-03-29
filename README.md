# Los Santos Reservation Application

![amiresposive-heroku](https://user-images.githubusercontent.com/78651133/178527987-096bc711-4a41-4b6a-8833-ec15ac4e4a9a.jpg)

The Los Santos Reservation Application is a console-based application which allows the user to fill out a form to formalise a reservation for a ficticious hotel, the information of which is sent to and updated on a spreadsheet row. The user interface for this project is entirely text-based and is run on a text terminal.

The application begins with a main menu, giving the user the option to find out information for room types and contact information for the establishment. The user is then able to proceed and officialise a reservation by filling out key information, those being their name, age, number of guests, e-mail address, room type, check-in date and check-out date. Based on this information, a total price is calculated, and the reservation information is displayed to the user and is then sent to a Google Sheets form where it appended onto a corresponding row. 

This project is the third in a series of five that must be completed in order to receive a diploma in Software Development from [Code Institute](https://codeinstitute.net/global/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+ROW+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=15207113220&hsa_grp=130324141420&hsa_ad=581817633110&hsa_src=g&hsa_tgt=aud-1602480256028:kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwt7SWBhAnEiwAx8ZLaiysHOvTv_fv50_dJV1M0VQ97gpB6x147RSwbBFnIgYEorNXsoXm9RoCMq8QAvD_BwE). 

A live version of the project can be found here: https://los-santos-hotel-app.herokuapp.com/

## **Requirements**

To create a Python based application using libraries/API that takes user input data, parses the information and validates it, handles potential user errors and exports said data into an appropriate dataset file. 

Such data information should be able to provide actionable insights, in this case, reservation information by the user.

# Table of content

* [UX](#ux)
     * [User demographics](#user-demographic)
     * [User goals](#user-goals)
          * [User applicant](#user-applicant)
          * [Establishment user](#establishment-user)
     * [Design](#design)
* [Features](#features)
     * [Application features](#application-features)
     * [Main menu landing page](#main-menu-landing-page)
     * [Room information](#room-information)
     * [Contact details](#contact-details)
     * [Exiting the application](#exiting-the-application)
     * [Making a reservation](#making-a-reservation)
     * [User error](#user-error)
* [Technologies used](#technologies-used)
     * [Coding languages](#coding-languages)
     * [Python libraries and API](#python-libraries-and-api)
     * [Storing data](#storing-data)
* [Testing](#testing)
     * [Fixed bugs](#fixed-bugs)
     * [Validator testing](#validator-testing)
* [Development and deployment](#development-and-deployment)
* [Credits](#credits)
* [Acknowledgments](#acknowledgments)

# UX 

## **User Demographic**

This application has been designed for people wanting to make a reservation at the Los Santos Hotel establishment. As specified in the application, only consenting adults over the age of 18 can make a reservation. 

The application also serves the establishment, as it receives the full information and details of the client in their database.

## **User Goals**

To be able to make a reservation, receive confirmation from the application of the reservation made and for the establishment to receive that information.

### **User applicant**

* I want to find out contact details for the establishment.
* I want to know information regarding the rooms.
* I want to be able to make a reservation.
* I want to be able to receive confirmation of my reservation from the same application.

### **Establishment User**

* I want clear, appropriate data input.
* I want to limit the user applicant input, such as age or quantity of guests.
* I want to receive an update in establishment database of the client reservation.

## **Design**

The Los Santos Reservation Application required no graphical design due to the nature of the application itself, instead thought has gone into the logic design of the application with relation to requesting input, input validating, updating an external document using an API and assisting the user through the application using clear guidance and supplying said user with confirmation of their entered input. 

The diagram of the logic map is as shown:

![diagram logic_page-0001](https://user-images.githubusercontent.com/78651133/179033901-df318c43-87ea-4649-9589-787a12f8d055.jpg)

# Features

## **Application features**

The application consists of two main principal features, gaining information about the establishment and making a reservation.

### **Main menu landing page**

The user is presented with the menu page, giving them options at the start of the application.

![landing-page](https://user-images.githubusercontent.com/78651133/178565073-44b590f7-c6a7-4eee-b7cf-30c7eb945f0d.jpg)

### **Room information**

If the user chooses option 2 by entering the number 2 as input, they are taken to the room information page as shown. 

![room-desc-1](https://user-images.githubusercontent.com/78651133/178565173-94b68844-c426-4964-8eb5-fa31a545e6ed.jpg)

![room-desc-2](https://user-images.githubusercontent.com/78651133/178565198-c5f7d334-685d-4be2-9074-352943a2eb16.jpg)

### **Contact details**

Shoulder the user choose option 3 entering the same as input, they are taken then to the contact details where they are provided with the appropriate information.

![contact-details](https://user-images.githubusercontent.com/78651133/178566398-53f50769-adaa-4e4c-8b6c-e9194b9e0b9f.jpg)

### **Exiting the application**

Should the user choose option 4 by entering the same as input, they are able to exit the application. This is highlighted in blue so as to stand out with importance.

![exiting-page](https://user-images.githubusercontent.com/78651133/178566455-c38d6ebc-2aab-49bc-96bf-6445ba46121b.jpg)

### **Making a reservation**

Should the user choose option 1 via the same numeric input, the principal program begins, first asking for a full name, validating the input, then requesting the age and validating the data. The user is informed that the information is being updated after each step. Notable is the use of the colour cyan (using import termcolor) for the informative descriptions and the default Python terminal white when requesting user input, making it easier for the user to visually navigate through the terminal.

![reservation-1](https://user-images.githubusercontent.com/78651133/178733178-b6058ecf-6932-4c06-bba9-bcb03b0c546e.jpg)
![reservation-2](https://user-images.githubusercontent.com/78651133/178733196-b28506a2-032b-482b-857c-c9011b142a1d.jpg)
![reservation-3](https://user-images.githubusercontent.com/78651133/178733209-8855517f-fedb-4d95-9dc1-6f86be298c51.jpg)

Next the numbers of guests is requested, which is validated, as well as the e-mail address request. Certain script standards are met so as to validate whether an e-mail is authentic or not, such as the use of an @ sign. As with the previous samples, the program gives the user clear examples of how input should be given.

![reservation-4](https://user-images.githubusercontent.com/78651133/178738275-895d3087-b7f6-47cb-9bbd-10088a1d60a0.jpg)
![reservation-5](https://user-images.githubusercontent.com/78651133/178738277-3de08b06-3fea-4e2b-83a3-d6e26e74c14c.jpg)

The room choice specification is then requested, as well as the check-in dates and check-out dates. Room choice is validated for integers and the dates are validated using datetime import. The check-in and check-out date are then used, specifically the day elements, in a subtraction to work out the total price, which is returned to the user for their information.

![reservation-6](https://user-images.githubusercontent.com/78651133/178739358-cf1dc144-a5da-48f6-a8b2-da0050d2e2c1.jpg)
![reservation-7](https://user-images.githubusercontent.com/78651133/178739361-ca20917f-8a50-4f87-871f-4eb0eae14b69.jpg)

Finally the reservation is finalised and is presented to the user as confirmation. The information is presented in the colour green to let the user know that the reservation is a go-ahead and has been successful. A thank you message is then emitted and the user is informed the application is now closing down.

![reservation-8](https://user-images.githubusercontent.com/78651133/178740014-dd2a3fa9-c080-4947-85e8-501c03c5b3be.jpg)

The data from the user then updated onto the next empty Google Sheets row. 

![google sheets sample](https://user-images.githubusercontent.com/78651133/178742993-df62d804-664c-4369-9f72-9041af9a9f3a.jpg)

### **User error**

The application is also able to catch user error and request appropriate data. The use of red text also helps to visually indicate to the user that an error has also occurred.

Some samples are the following:

![error example](https://user-images.githubusercontent.com/78651133/178813609-1ce10b03-2629-4b4e-a05a-925570391616.jpg)
![error age sample](https://user-images.githubusercontent.com/78651133/178813614-dfc4c461-4da9-4cb7-9a6a-7890da1262d7.jpg)
![error email sample](https://user-images.githubusercontent.com/78651133/178813615-7051e03a-2a37-48dd-b635-0611b2c369e2.jpg)

# Technologies used

### **Coding languages**

* [Python](https://www.python.org/)
* [HTML](https://html.com/) - Included in the Code Institute template
* [CSS](https://en.wikipedia.org/wiki/CSS) - Included in the Code Institute template
* [JavaScript](https://www.javascript.com/) - Included in the Code Institute template

### **Python libraries and API**

* [Re](https://docs.python.org/3/library/re.html)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [Sys](https://docs.python.org/3/library/sys.html)
* [Termcolor](https://pypi.org/project/termcolor/)
* [Gspread](https://docs.gspread.org/en/latest/)
* [Google Auth](https://google-auth.readthedocs.io/en/master/)

### **Storing data**

* [Google Sheets](https://www.google.com/sheets/about/)
* [Google Drive](https://www.google.com/drive/)

# Testing

Testing and checking application functionality has been carried out continuously over the development of the project.

### **Fixed bugs**

* Validators for checking full name and e-mail address stopped responding.
     * Issue fixed, a Python formatter had changed the code, therefore I returned it to previous code.

* Updating the Google Sheets with user information would throw an error
     * Through trial and error, bug was eventually fixed, using inspiration from the [Love Sandwiches](https://github.com/keironchaudhry/love-sandwiches/blob/dc0c7603b44eb9a174a0eb3cd9bd443151b33270/run.py#L65) project.

* When the program terminates after confirmation of reservation, several None values appear before closing.
     * Added a sys.exit at the end of the principal program function to close the application cleanly.

* Lines were over the 79 character limit.
     * Went through all the corresponding lines of code and ammended them.

* Lots of trailing white spaces were detected.
     * Went through the corresponding lines of code and rectified the white spacing.

* Check-in and check-out dates would not print onto Google Sheets, threw multiple errors.
     * Already converted datetime inputs had to be reconverted back into strings to append onto Google Sheets.

* Age function would return colossal inputs beyond 100 years of age.
     * Modified the age function to cap maximum age input, for example > 100 years old. 

* Name, age, guest quantity and e-mail functions would return incorrect input despite calling out errors.
     * Corrected this by moving all if statements into the While loop of each function and having invalid input return False.
     
* Check-in function would accept dates in the past.
     * Amended this by defining a variable with the date of today and limiting input beyond that. 

* Check-out function would accept dates in the past beyond the check-in date, causing irregular calculations.
     * Amended this by limiting user input into the past beyond check-in date, today's date and created a maximum date to stop user input too far into the future.

### **Validator Testing**

Code has been tested and corrected via the PEP8 Online Validator http://pep8online.com/.

# Development and deployment

The development environment used for this project was Gitpod. Regular commits and pushes to Github have been employed to be able to track and trace the development process of the website. The Gitpod environment for this particular project was created using a template provided by Code Institute.

The live version of this project is deployed using [Heroku](https://heroku.com).

The following is the procedure for how this project was deployed via Heroku:

A requirements.txt needs to be created in the same folder as the .py file in Gitpod. This needs to have a list of necessary libraries the project needs to run as a Heroku Application.

Then move onto the following:

* Log in to Heroku (or create an account if otherwise)
* Click on New in the Heroku dashboard and select ”Create new app”
* Give the application an original name, choose your region and click “Create App”
* In the settings tab for the new application two Config Vars are necessary:
    * One is named CREDS and contains the credentials key for Google Drive API
    * One is name PORT and has the value of 8000
* Two buildpack scripts were added: Python and Nodejs (in that order)
* Go to "Deploy" section, and click the Github icon in 'Deployment Method' and connect
* In this case, this project was set to 'Automatic Deploys'.
* Deployment should then be completed within a brief time span and link readily available. 

After those steps were taken the application was deployed at the following link: https://los-santos-hotel-app.herokuapp.com/

# Credits

Various websites have been consulted during the development of this project. All code has been credited in code comments within the project.

The following have proved incredibly helpful:

* [Google Sheets for Developers](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append) for insight and further information on Google Sheets updating.

* [Geeks for Geeks](https://www.geeksforgeeks.org/) for insight on how to validate certain inputs, such as full names and e-mail addresses.

* [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) by Code Institute for guidance on how to develop this project.

# Acknowledgments

For inspiration, guidance and inputs, thank you to:

Sandeep Aggarwal

* Absolutely fantastic mentor at Code Institute with brilliant insight into back-end software development.

Jack Crymble

* Friend and guide, thank you for your knowledge and insight!

Jody Murray

* Fellow student and colleague, thank you for your input and constant support!
