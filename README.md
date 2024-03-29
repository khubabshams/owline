**Live Site:** https://owline.herokuapp.com

**Developed by:** [Khubab Shamsuddin](https://www.linkedin.com/in/kshamse/)

<kbd>[<img src="docs/owline-logo.png" alt="Owline logo" title="Owline Live Site" width="200"/>](https://owline.herokuapp.com)</kbd>


![Ownline multi-screens](docs/amiresponsive.PNG)

# Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Goals](#goals)
  - [User's Goals](#users-goals)
  - [Site Owner's Goals](#site-owners-goals)
- [User Stories](#user-stories)
  - [Anonymous User](#anonymous-user)
  - [Logged-in User](#logged-in-user)
  - [Admin User](#admin-user)
  - [Site Owner](#site-owner)
- [Design](#design)
  - [Frontend](#frontend)
    - [Colours](#colours)
    - [Font](#font)
  - [Backend](#backend)
    - [Data Models](#data-models)
- [Technologies](#technologies)
  - [Django Framework](#django-framework)
  - [Python](#python)
  - [Other Software and Tools](#other-software-and-tools)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Navbar](#navbar)
    - [Signup](#signup)
    - [Login](#login)
    - [Notifications](#notifications)
    - [Search Questions](#search-questions)
    - [Ask Questions](#ask-questions)
    - [Answer Questions](#answer-questions)
    - [Imporve Question/ Answer](#imporve-question-answer)
    - [Delete Question/ Answer](#delete-question-answer)
    - [Register Votes](#register-votes)
    - [Accept Answers](#accept-answers)
    - [Contact Us](#contact-us)
    - [Inbox](#inbox)
    - [Footer](#footer)
  - [Features Left to Implement](#features-left-to-implement)
    - [Tags](#tags)
    - [Reply to User Messages](#reply-to-user-messages)
- [Validations](#validations)
  - [Python](#python-1)
  - [Javascript](#javascript)
  - [HTML](#html)
  - [CSS](#css)
  - [Accessability](#accessability)
  - [Lighthouse](#lighthouse)
- [Testing](#testing)
  - [Manual Testing of User Stories](#manual-testing-of-user-stories)
  - [Automated Testing](#automated-testing)
- [Configurations](#configurations)
  - [Login Credentials](#login-credentials)
  - [Fork This Repository](#fork-this-repository)
  - [Make Local Clone](#make-local-clone)
- [Credits](#credits)
  - [Media](#media)
  - [Documentations](#documentations)
  - [Code](#code)
  - [Errors Solving](#errors-solving)


# Overview

Owline is an online forum for all internet users. People can find answers to their questions or help others by answering their inquiries. Users can also improve posted content and promote a question or an answer positively or negatively. Admin users can organise and control content by removing irrelevant, out-of-point, and disturbing posts.

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Goals

## User's Goals

1. Read questions and explore answers.
2. Search and ask questions.
3. Answer others' questions and discuss topics.

## Site Owner's Goals

1. Provide an online discussion platform.
2. Build a direct simple website that fulfill the users' needs.
3. Create a direct channel of messaging with the users.

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# User Stories

## Anonymous User

1. I can view and filter the listed questions so that I will be able to read them. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
2. I can be able to open a question's details so that I can read the answers. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
3. I can sign up so that I can access more of the site's features. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
4. I can logged in so that I can ask or answer questions. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
5. I can search for specific questions so that I will avoid question duplication. ![could have](https://img.shields.io/badge/could%20have-grey?style=flat)

## Logged-in User

6. I can ask a question so that I can get an answer. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
7. I can edit a question so that it is more clearly answered. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
8. I can answer a question so that my answer could help someone. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
9. I can edit an answer so that they are more clarified and updated. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
10. I can accept one of my questions' answers so that other users know it helped me. ![could have](https://img.shields.io/badge/could%20have-grey?style=flat)
11. I can upvote or downvote a question or answer to show how much this question or answer is helpful. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
12. I can see the vote score of my questions and answers on my profile, so I'll be encouraged to create more helpful questions and answers. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
13. I can contact the site's admin so that I can report an issue with the website or its content. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)

## Admin User

14. I can delete duplicated or irrelevant questions so that users focus on answering valuable ones. ![could have](https://img.shields.io/badge/could%20have-grey?style=flat)
15. I can delete the irrelevant answers so that they won't distract users. ![could have](https://img.shields.io/badge/could%20have-grey?style=flat)
16. I can reply to users' messages so that I provide them with the required feedback and support. ![won't have](https://img.shields.io/badge/won't%20have-red?style=flat)

## Site Owner

17. I want users to be able to open the site on their mobile phone or tablet so that they'll have the same experience as on a desktop. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
18. I want users to be able to open any page wherever they are so that navigating through the site will be easy. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
19. I want users to be able to get feedback on their actions so that they'll know if their action was successfully completed or failed. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
20. I want users to see the site's text fonts and colours clearly so that they can focus on the content without distraction. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
    
[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Design

## Frontend

### Colours

The colour scheme created for the site is contrasted, which provides better accessibility and helps the user have a comfortable experience.
<details>
  <summary>The Colour Scheme</summary>

![colour scheme](docs/colour-scheme.PNG)
</details>

### Font

The font used in this site is "Lato," which is a sans-serif, clean font that's commonly used in blogs and writing.
Different styles of the Lato font have been used:

<details>
  <summary>Headers and Titles</summary>

![header and footer](docs/font-lato-300-light.PNG)
</details>

<details>
  <summary>Navbar, Footer, Questions and Answers</summary>

![navbar and footer](docs/font-lato-400.PNG)
</details>

## Backend

### Data Models

Models have been developed following OOP concepts, trying to secure better maintenance and reduce redundancy.

<details>
  <summary>Models' Details</summary>
 
  - Classes `BasePost`, `Question` and `Answer` developed in `forum` app, `Message` in `contact_us` and `Profile` in `home` app.
  - `BasePost` is the parent class of `Answer`  and `Question`, it contains their main attributes.
  - `Profile` is created to extend built-in `User` class features; a `Profile` record is created and linked with `User` each time the latter is created.
  - Each model, except `Profile` and `BasePost`, has different types of generic views developed.
  - Unit tests for `forum` app are created by inheriting the main test class, which contains test setup and inherits built-in `TestCase`.  
</details>

<details>
  <summary>Class Diagram For Models</summary>

![models' class diagram](docs/class-diagram.PNG)
</details>

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Technologies

## Django Framework

- Django Python Web Framework has been used to develop this site.
- Version: 3.2.18

## Python

- is the programming language used to develop the models and views of this site.
- Version: 3.8.11

## Other Software and Tools

- [Django Markup](https://pypi.org/project/django-markupfield/): used to create markdown-supported text fields.
- [Coverage](https://pypi.org/project/coverage/): used to check the coverage of the automation testing of the Python classes.
- [Pycodestyle](https://pypi.org/project/pycodestyle/): is used to hint syntax errors and warnings in Python code.
- [Bootstrap](https://getbootstrap.com): is used for styling and providing an appealing site.
- [Badge Generator](https://badgesgenerator.com/): is used to generate markdown badges for Readme's user stories.
- [Markdown All in One Extension](https://open-vsx.org/vscode/item?itemName=yzhang.markdown-all-in-one): used to help in writing the readme.
- [Github](https://github.com/): used as a version control management tool.
- [Gitpod](https://www.gitpod.io): used as a development environment.
- [Heroku](https://www.heroku.com/): is used to deploy this site.
- [ElephantSQL](https://www.elephantsql.com/): used as a PostgreSQL database service.
- [Cloudinary](https://cloudinary.com/): is used to provide storage for the static files.
- [Dia](http://dia-installer.de/): used to design models' class diagrams.
- [Canva](https://www.canva.com/): used to design the logo and the colour scheme.
- [Font Awesome](https://fontawesome.com/): icons provided by Font Awesome were used in this site.
- [Freepik](https://www.freepik.com/): is used to get illustration images.
- [Cool Symbol](https://coolsymbol.com/): used to copy text symbols.
- [Google Fonts](fonts.google.com): the used font is imported from the Google Fonts library.
- [Quillbot](https://quillbot.com/grammar-check) and [Grammarly](https://app.grammarly.com/): used to fix spelling and grammar mistakes.
- [Am I Responsive](https://ui.dev/amiresponsive): used to generate multi-screen site previews.
- [Favicon Generator](https://www.favicon-generator.org/): used to create favicons suitable for different device dimensions.
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/): used to discover errors in CSS stylesheets.
- [Nu Html Checker](https://validator.w3.org/nu/): used to discover errors in HTML syntax.
- [WAVE](https://wave.webaim.org/): has been used as an accessibility evaluation tool.
- [Google Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/): is used to generate reports for performance, accessibility, best practises, and SEO.
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/): used to test website responsiveness and debug styling issues.
- [JSHint](https://jshint.com/): used to find Javascript code errors.

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Features

## Existing Features

### Navbar

- The navbar contains links to all site features such as the home page, account options, search and create questions, and admins' message inbox.It was developed to be responsive and simple.
- _user stories covered: 17,18_

<details>
<summary>Navbar on Desktop</summary>

![navbar desktop](docs/Screenshots/nav-desktop.PNG)
</details>
<details>
<summary>Navbar on Mobile</summary>

![navbar mobile](docs/Screenshots/nav-mobile.PNG)
</details>

### Signup

- Users with no accounts can sign up with a single form and a straightforward process. They'll need only to enter the username, email, password and a passowrd confirmation.
- _user story covered: 3_

<details>
<summary>Singup on Desktop</summary>

![signup desktop](docs/Screenshots/signup-desktop.PNG)
</details>
<details>
<summary>Singup on Mobile</summary>

![signup mobile](docs/Screenshots/signup-mobile.PNG)
</details>

### Login

- To be able to use most sites' features, users have to be logged in. The process requires only entering a username and password and whether they want to keep their accounts logged in by clicking on the 'Remember Me' option.
- _user stories covered: 4_

<details>
<summary>Login on Desktop</summary>

![login desktop](docs/Screenshots/login-desktop.PNG)
</details>
<details>
<summary>Login on Mobile</summary>

![login mobile](docs/Screenshots/login-mobile.PNG)
</details>

### Notifications

- Messages are shown on each user action to let them know whether their action succeeded or failed and what happened when it didn't work.
- _user stories covered: 19_

<details>
<summary>Notifications on Desktop</summary>

![notification success desktop](docs/Screenshots/notification-success-desktop.PNG)
![notification failed desktop](docs/Screenshots/notification-failed-desktop.PNG)
</details>
<details>
<summary>Notifications on Mobile</summary>

![notification success mobile](docs/Screenshots/notification-success-mobile.PNG)
![notification failed mobile](docs/Screenshots/notification-failed-mobile.PNG)
</details>

### Search Questions

- Users can search for specific questions by entering some keywords. This will help users by saving time to get answers, and admins by avoiding the need to duplicate questions.
- _user stories covered: 1,2,5_

<details>
<summary>Search on Desktop</summary>

![search desktop](docs/Screenshots/search-desktop.PNG)
</details>
<details>
<summary>Search on Mobile</summary>

![search mobile](docs/Screenshots/search-mobile.PNG)
</details>

### Ask Questions

- Logged-in Users who cannot find an available answer to their question by searching can create a new question and wait for other users replies.
- They need to enter the title of the question, which is a brief description of what they are asking, and the body, which is an explanation in details of their issue or problem.
- _user stories covered: 6_

<details>
<summary>Question on Desktop</summary>

![question desktop](docs/Screenshots/question-create-desktop.PNG)
</details>
<details>
<summary>Question on Mobile</summary>

![question mobile](docs/Screenshots/question-create-mobile.PNG)
</details>

### Answer Questions

- Logged-in Users who are knowledgeable about the topic of the question can respond to it to assist the asker and other readers who are experiencing similar problems. 
- _user stories covered: 8_

<details>
<summary>Answer on Desktop</summary>

![answer desktop](docs/Screenshots/answer-create-desktop.PNG)
</details>
<details>
<summary>Answer on Mobile</summary>

![answer mobile](docs/Screenshots/answer-create-mobile.PNG)
</details>

### Imporve Question/ Answer

- Unclear questions are more likely to be answered correctly, and unclear answers won't provide the asker with the information needed. Logged-in users can update each other's questions or answers to simplify them and provide more clarity.
- _user stories covered: 7,9_

<details>
<summary>Question Update on Desktop</summary>

![question options desktop](docs/Screenshots/question-desktop.PNG)

![question update desktop](docs/Screenshots/question-update-desktop.PNG)
</details>
<details>
<summary>Question Update on Mobile</summary>

![question options mobile](docs/Screenshots/question-mobile.PNG)
![question update mobile](docs/Screenshots/question-update-mobile.PNG)
</details>

<details>
<summary>Answer Update on Desktop</summary>

![answer options desktop](docs/Screenshots/answer-desktop.PNG)

![answer update desktop](docs/Screenshots/answer-update-desktop.PNG)
</details>
<details>
<summary>Answer Update on Mobile</summary>

![answer options mobile](docs/Screenshots/answer-mobile.PNG)

![answer update mobile](docs/Screenshots/answer-update-mobile.PNG)
</details>

### Delete Question/ Answer

- Deleting out of topic or duplicated questions or answers will help organising the content on site and control the language used on it.
- _user stories covered: 14,15_

<details>
<summary>Question Delete on Desktop</summary>

![question options desktop](docs/Screenshots/question-desktop.PNG)

![question delete desktop](docs/Screenshots/question-delete-desktop.PNG)
</details>
<details>
<summary>Question Delete on Mobile</summary>

![question options mobile](docs/Screenshots/question-mobile.PNG)

![question delete mobile](docs/Screenshots/question-delete-mobile.PNG)
</details>

<details>
<summary>Answer Delete on Desktop</summary>

![answer options desktop](docs/Screenshots/answer-desktop.PNG)

![answer delete desktop](docs/Screenshots/answer-delete-desktop.PNG)
</details>
<details>
<summary>Answer Delete on Mobile</summary>

![answer options mobile](docs/Screenshots/answer-mobile.PNG)

![answer delete mobile](docs/Screenshots/answer-delete-mobile.PNG)
</details>

### Register Votes

- Voting are used in this site to provide a feedback on question or answer. Logged-in users can upvote or downvote depends on their experience with the answer or the way a question is presented.
- Users can see the vote score of their questions and answers attached to their usernames.
- _user stories covered: 11,12_

<details>
<summary>Question Upvote on Desktop</summary>

![question upvote desktop](docs/Screenshots/upvote-question-desktop.PNG)
</details>
<details>
<summary>Question Upvote on Mobile</summary>

![question upvote mobile](docs/Screenshots/upvote-question-mobile.PNG)
</details>
<details>
<summary>Question Downvote on Desktop</summary>

![question downvote desktop](docs/Screenshots/downvote-question-desktop.PNG)
</details>
<details>
<summary>Question Downvote on Mobile</summary>

![question downvote mobile](docs/Screenshots/downvote-question-mobile.PNG)
</details>

<details>
<summary>Answer Upvote on Desktop</summary>

![answer upvote desktop](docs/Screenshots/upvote-answer-desktop.PNG)
</details>
<details>
<summary>Answer Upvote on Mobile</summary>

![answer upvote mobile](docs/Screenshots/upvote-answer-mobile.PNG)
</details>
<details>
<summary>Answer Downvote on Desktop</summary>

![answer downvote desktop](docs/Screenshots/downvote-answer-desktop.PNG)
</details>
<details>
<summary>Answer Downvote on Mobile</summary>

![answer downvote mobile](docs/Screenshots/downvote-answer-mobile.PNG)
</details>

### Accept Answers

- Answers can be accepted by questions' owners, which make it easier for other users to distinguish the best answer, which has helped the asker more.
- _user stories covered: 10_

<details>
<summary>Answer Accept on Desktop</summary>

![answer accept desktop](docs/Screenshots/answer-desktop.PNG)
</details>
<details>
<summary>Answer Accept on Mobile</summary>

![answer accept mobile](docs/Screenshots/answer-mobile.PNG)
</details>

### Contact Us

- Logged-in users can send messages directly to the sites' administrators, providing feedback or reporting an issue on the site.
- _user stories covered: 13_

<details>
<summary>Message on Desktop</summary>

![message desktop](docs/Screenshots/message-desktop.PNG)
</details>
<details>
<summary>Message on Mobile</summary>

![message mobile](docs/Screenshots/message-mobile.PNG)
</details>

### Inbox
- Admin users can find users' messages in the inbox and therefore investigate users' issues and reply to their inquiries.
- _user stories covered: 13,16_

<details>
<summary>Inbox on Desktop</summary>

![inbox desktop](docs/Screenshots/inbox-desktop.PNG)
</details>
<details>
<summary>Inbox on Mobile</summary>

![inbox mobile](docs/Screenshots/inbox-mobile.PNG)
</details>

### Footer

- Positioned at the bottom of the sites' pages, the footer contains links to Home, Contact Us, and the developer's LinkedIn profile, in addition to the copyright statement.
- _user stories covered: 17,18_

<details>
<summary>Footer on Desktop</summary>

![footer desktop](docs/Screenshots/footer-desktop.PNG)
</details>
<details>
<summary>Footer on Mobile</summary>

![footer mobile](docs/Screenshots/footer-mobile.PNG)
</details>

## Features Left to Implement

### Tags

- Tags could be developed later, so that user could use them on question creation, which may help other users filter questions and find questions related easier.

### Reply to User Messages

- The ability to reply to users' messages through the site itself will make things easier for admins, so they won't need to use an external mail service.
  
[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Validations

The site has been checked against a variety of validators, and it passed all of them after discovered errors were fixed.

## Python

Pycodestyle is used to discover and solve all Python errors and warnings.
<details>
<summary>Pycodestyle Result</summary>

![pycodestyle result](docs/Validators/pycodestyle-result.PNG)
</details>

## Javascript

Jshint is used to validate the Javascript code, and it passed successfully.
<details>
<summary>JShint Result</summary>

![jshint result](docs/Validators/jshint-check.PNG)
</details>

## HTML

Nu HTML Checker is used to validate the HTML syntax, and all related errors have been resolved.
<details>
<summary>Nu HTML Checker Results</summary>

![nu html checker index result](docs/Validators/html-checker-forum-index.PNG)
![nu html checker question result](docs/Validators/html-checker-question.PNG)
</details>

## CSS

Jigsaw W3C CSS Checker is used to check the CSS stylesheets, and they passed the check without errors.
<details>
<summary>Jigsaw W3C CSS Results</summary>

![jigsaw w3c css index result](docs/Validators/jigsaw-w3c-css-checker-forum-index.PNG)
![jigsaw w3c css question result](docs/Validators/jigsaw-w3c-css-checker-question.PNG)
</details>

## Accessability

WAVE Web Accessibility Evaluation tool has been used to discover and fix contrast errors and follow web best practises.
<details>
<summary>WAVE Tools Results</summary>

![wave index result](docs/Validators/wave-accessability-forum.PNG)
![wave question result](docs/Validators/wave-accessability-question.PNG)
![wave inbox result](docs/Validators/wave-accessability-inbox.PNG)
![wave message result](docs/Validators/wave-accessability-message.PNG)
</details>

## Lighthouse

The Google Chrome Lighthouse tool used to generate reports for the sites' pages regards their performance, accessibility, best practises, and SEO on the desktop and mobile.
<details>
<summary>Lighthouse Results</summary>

__Desktop__
![lighthouse desktop index result](docs/Validators/lighthouse-desktop-index.PNG)
![lighthouse desktop question result](docs/Validators/lighthouse-desktop-question.PNG)
![lighthouse desktop question create result](docs/Validators/lighthouse-desktop-question-create.PNG)
![lighthouse desktop inbox result](docs/Validators/lighthouse-desktop-inbox.PNG)
![lighthouse desktop message result](docs/Validators/lighthouse-desktop-message.PNG)

__Mobile__
![lighthouse mobile index result](docs/Validators/lighthouse-mobile-index.PNG)
![lighthouse mobile question result](docs/Validators/lighthouse-mobile-question.PNG)
![lighthouse mobile question create result](docs/Validators/lighthouse-mobile-question-create.PNG)
![lighthouse mobile inbox result](docs/Validators/lighthouse-mobile-inbox.PNG)
![lighthouse mobile message result](docs/Validators/lighthouse-mobile-message.PNG)
</details>

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Testing

## Manual Testing of User Stories

__1. I can view and filter the listed questions so that I will be able to read them:__

| Step                                                                 | Expected Result                                                                                                                | Actual Result     |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| Open https://owline.herokuapp.com/                                   | Home page loads with questions list                                                                                            | Works as expected |
| Enter keywords in the search input to filter questions and hit enter | URL will change to https://owline.herokuapp.com/forum/search/ and only questions with at least one keyword will be on the list | Works as expected |
| When a keyword is not found in all questions                         | URL will change to https://owline.herokuapp.com/forum/search/ and a message of "Sorry, There's no question found!" shows       | Works as expected |

<details>
  <summary>Screenshots</summary>
  
__Navbar -> Home__
  ![navbar home](docs/Screenshots/nav-desktop.PNG)

__Questions List__
  ![questions list](docs/Screenshots/question-list-desktop.PNG)

__Search__
  ![search](docs/Screenshots/search-desktop.PNG)

__Search Succeeded__
  ![search success](docs/Screenshots/search-success.PNG)

__Question Not Found__
  ![search not found](docs/Screenshots/search-not-found.PNG)
</details>
<hr>

__2. I can be able to open a question's details so that I can read the answers:__
  
| Step                                          | Expected Result                                                   | Actual Result     |
| --------------------------------------------- | ----------------------------------------------------------------- | ----------------- |
| Open `Home` and click on one of the questions | The question page loads with its full content and related answers | Works as expected |

<details>
  <summary>Screenshots</summary>
  
__Navbar -> Home__
  ![navbar home](docs/Screenshots/nav-desktop.PNG)

__Questions List__
  ![questions list](docs/Screenshots/question-list-desktop.PNG)

__Question Details__
  ![question details](docs/Screenshots/question-details.PNG)
</details>
<hr>

__3. I can sign up so that I can access more of the site's features:__

| Step                                                                                                      | Expected Result                                      | Actual Result     |
| --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------- |
| From the navbar click on the user icon, `Account` on mobile and choose `Signup`                           | Signup form loads                                    | Works as expected |
| Enter the `username`, `email`, `password`, and `password confirmation` then click on the `Sign Up` button | Signup succeeded and the user notified and logged in | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Navbar -> Signup__
  ![navbar signup](docs/Screenshots/nav-desktop.PNG)

__Signup__
  ![signup](docs/Screenshots/signup-desktop.PNG)

__Signup Succeded__
  ![signup success](docs/Screenshots/signup-success.PNG)
</details>
<hr>

__4. I can log in so that I can ask or answer questions:__

| Step                                                                           | Expected Result                       | Actual Result     |
| ------------------------------------------------------------------------------ | ------------------------------------- | ----------------- |
| From the navbar click on the user icon, `Account` on mobile and choose `Login` | Login form loads                      | Works as expected |
| Enter the `username` and the `password` then click on `Sign In` button         | Login succeeded and the user notified | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Navbar -> Login__
  ![navbar login](docs/Screenshots/nav-desktop.PNG)

__Login__
  ![login](docs/Screenshots/login-desktop.PNG)

__Login Succeded__
  ![login success](docs/Screenshots/login-success.PNG)
</details>
<hr>

__5. I can search for specific questions so that I will avoid question duplication:__
 
| Step                                                                                 | Expected Result                                                                                                                | Actual Result     |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| Open `Home` and Enter keywords in the search input to filter questions and hit enter | URL will change to https://owline.herokuapp.com/forum/search/ and only questions with at least one keyword will be on the list | Works as expected |
| When a keyword is not found in all questions                                         | URL will change to https://owline.herokuapp.com/forum/search/ and a message of "Sorry, There's no question found!" shows       | Works as expected |

<details>
  <summary>Screenshots</summary>
  
__Navbar -> Home__
  ![navbar home](docs/Screenshots/nav-desktop.PNG)

__Questions List__
  ![questions list](docs/Screenshots/question-list-desktop.PNG)

__Search__
  ![search](docs/Screenshots/search-desktop.PNG)

__Search Succeeded__
  ![search success](docs/Screenshots/search-success.PNG)

__Question Not Found__
  ![search not found](docs/Screenshots/search-not-found.PNG)
</details>
<hr>

__6. I can ask a question so that I can get an answer:__
 
| Step                                                                | Expected Result                     | Actual Result     |
| ------------------------------------------------------------------- | ----------------------------------- | ----------------- |
| Open `Home` and click the `Ask Question` button                     | Question create form loads          | Works as expected |
| Enter question `Title` and `Body` then click on the `Submit` button | Question created and its page loads | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Navbar -> Ask Question__
  ![navbar ask question](docs/Screenshots/nav-desktop.PNG)

__Question Create Form__
  ![question create form](docs/Screenshots/question-create-desktop.PNG)

__Question__
  ![question](docs/Screenshots/question-desktop.PNG)
</details>
<hr>

__7. I can edit a question so that it is more clearly answered:__
  
| Step                                                                                                                                                  | Expected Result                                                           | Actual Result     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------- |
| Open `Home` and click on the question, which needs to update then on the question page click on the `More Actions` menu on right and choose `Improve` | Question update form loads                                                | Works as expected |
| Modify question `Title` or `Body` or both of them, then click on the `Submit` button                                                                  | Question updated and its page loads with `modified by [username]` comment | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Navbar -> Home__
  ![navbar home](docs/Screenshots/nav-desktop.PNG)

__Questions List__
  ![questions list](docs/Screenshots/question-list-desktop.PNG)

__Question__
  ![question](docs/Screenshots/question-desktop.PNG)

__Question Update Form__
  ![question update form](docs/Screenshots/question-update-desktop.PNG)

__Question Updated__
  ![question updated](docs/Screenshots/question-updated-desktop.PNG)
</details>
<hr>

__8. I can answer a question so that my answer could help someone:__
  
| Step                                                                                                                       | Expected Result                                 | Actual Result     |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| Click on the question, which needs to answer then on the bottom of the page fill in the `Answer's Body` and click `Submit` | Question page reloads with a new answer created | Works as expected |

<details>
<summary>Screenshots</summary>

__Questions List__
  ![questions list](docs/Screenshots/question-list-desktop.PNG)

__Question__
  ![question](docs/Screenshots/question-desktop.PNG)

__Answer Create Form__
  ![answer create form](docs/Screenshots/answer-create-desktop.PNG)
</details>
<hr>

__9.  I can edit an answer so that they are more clarified and updated:__
  
| Step                                                                                                 | Expected Result                                                                             | Actual Result     |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------- |
| On the answer that needs to be updated click on the `More Actions` menu on right and choose `Update` | Answer update form loads                                                                    | Works as expected |
| Modify the answer `Body`, then click on the `Submit` button                                          | Question page reloads and the answer is updated and commented with `modified by [username]` | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Question__
  ![question](docs/Screenshots/question-details.PNG)

__Answer Update Form__
  ![answer update form](docs/Screenshots/answer-update-desktop.PNG)

__Answer Updated__
  ![answer updated](docs/Screenshots/answer-updated-desktop.PNG)
</details>
<hr>

__10.  I can accept one of my questions' answers so that other users know it helped me:__
    
| Step                                                                                                                                       | Expected Result                                | Actual Result     |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ----------------- |
| Open the question page and go down for answers, on the answer need to accept click on the `More Actions` menu on right and choose `Accept` | Question page reloads with the answer accepted | Works as expected |

<details>
<summary>Screenshots</summary>

__Question__
![question](docs/Screenshots/question-details.PNG)

__Answer__
![answer](docs/Screenshots/answer-desktop.PNG)

__Answer Accepted__
![answer accepted](docs/Screenshots/answer-accepted.PNG)

</details>
<hr>

__11.  I can upvote or downvote a question or answer to show how much this question or answer is helpful:__
    
| Step                                                                                  | Expected Result                                                               | Actual Result     |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------- |
| Open the question page and click on the `Arrows` on the left, left-down on mobile     | Question page reloads with vote increased/ decreased and user notified        | Works as expected |
| Open the question page and go down for answers click on the `Thumbs` on the left-down | Question page reloads with an answer upvoted/ downvoted and the user notified | Works as expected |

<details>
<summary>Screenshots</summary>

__Question__
![question](docs/Screenshots/question-details.PNG)

__Question Vote__
![question vote](docs/Screenshots/upvote-question-desktop.PNG)
  
__Answer Vote__
![answer vote](docs/Screenshots/upvote-answer-desktop.PNG)

__Vote Signed__
![vote signed](docs/Screenshots/notification-success-desktop.PNG)

</details>
<hr>

__12.   I can see the vote score of my questions and answers on my profile, so I'll be encouraged to create more helpful questions and answers:__

| Step                           | Expected Result                                                                       | Actual Result     |
| ------------------------------ | ------------------------------------------------------------------------------------- | ----------------- |
| Open a question or answer post | Beside the username, the total number of votes he got appears as `Username [number]v` | Works as expected |

<details>
<summary>Screenshots</summary>

__Question__
![question](docs/Screenshots/question-details.PNG)

__Profile Votes__
![profile votes](docs/Screenshots/profile-votes.PNG)
</details>
<hr>

__13.  I can contact the site's admin so that I can report an issue with the website or its content:__
    
| Step                                                                                | Expected Result            | Actual Result     |
| ----------------------------------------------------------------------------------- | -------------------------- | ----------------- |
| Click on `Contact Us`                                                               | Contact Us form page loads | Works as expected |
| Enter `email`, `body`, and `name`, which is an optional input, then click on `Send` | Home page loads            | Works as expected |

<details>
<summary>Screenshots</summary>

__Contact Us__
![contact us](docs/Screenshots/contactus-navbar.PNG)

__Message Create Form__
![message create](docs/Screenshots/message-create-desktop.PNG)

__Message Created__
![message created](docs/Screenshots/message-desktop.PNG)
</details>

__14.  I can delete duplicated or irrelevant questions so that users focus on answering valuable ones:__

| Step                                                                                                                                                 | Expected Result                         | Actual Result     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ----------------- |
| Open `Home` and click on the question, which needs to delete then on the question page click on the `More Actions` menu on right and choose `Remove` | Question delete confirmation form loads | Works as expected |
| Click on `Confirm` button                                                                                                                            | Question deleted and `Home` page load   | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Navbar -> Home__
  ![navbar home](docs/Screenshots/nav-desktop.PNG)

__Questions List__
  ![questions list](docs/Screenshots/question-list-desktop.PNG)

__Question__
  ![question](docs/Screenshots/question-desktop.PNG)

__Question Delete Confirmation Form__
  ![question delete form](docs/Screenshots/question-delete-desktop.PNG)
</details>
<hr>


__15.  I can delete the irrelevant answers so that they won't distract users:__

| Step                                                                                                                                       | Expected Result                          | Actual Result     |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- | ----------------- |
| Open the question page and go down for answers, on the answer need to delete click on the `More Actions` menu on right and choose `Delete` | Answer delete confirmation form loads    | Works as expected |
| Click on `Confirm` button                                                                                                                  | Question page reloads and answer deleted | Works as expected |

<details>
<summary>Screenshots</summary>

__Question__
![question](docs/Screenshots/question-details.PNG)

__Answer__
![answer](docs/Screenshots/answer-desktop.PNG)

__Answer Delete Confirmation Form__
![answer delete form](docs/Screenshots/answer-delete-desktop.PNG)

</details>
<hr>

__16.  I can reply to users' messages so that I provide them with the required feedback and support:__

_The use of an external mail service needed as a feature not fully implemented_ 

| Step                                                                                                       | Expected Result                          | Actual Result     |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------- |
| Click on `Inbox` and click on the message need to reply and copy the `email` to send a message to the user | Message page loads with the user's email | Works as expected |

<details>
  <summary>Screenshots</summary>
  
__Navbar -> Inbox__
    ![navbar inbox](docs/Screenshots/inbox-nav-desktop.PNG)

__Message__
    ![message](docs/Screenshots/message-desktop.PNG)
</details>
<hr>

__17.  I want users to be able to open the site on their mobile phone or tablet so that they'll have the same experience as on a desktop:__

| Step                                                   | Expected Result                                               | Actual Result     |
| ------------------------------------------------------ | ------------------------------------------------------------- | ----------------- |
| Open https://owline.herokuapp.com/ on mobile or tablet | Navbar and other elements fully responsive on smaller screens | Works as expected |
| Navigate to question page                              | Vote control will move to left-down the question              | Works as expected |

<details>
  <summary>Screenshots</summary>

__Site on Mobile Screen__

  ![inbox mobile](docs/Screenshots/inbox-mobile.PNG)
  ![answer mobile](docs/Screenshots/answer-mobile.PNG)  
  ![question mobile](docs/Screenshots/question-mobile.PNG)
  ![message mobile](docs/Screenshots/message-mobile.PNG)
  ![navbar mobile](docs/Screenshots/nav-mobile.PNG)
  </details>
<hr>

__18.  I want users to be able to open any page wherever they are so that navigating through the site will be easy:__

| Step                               | Expected Result                     | Actual Result     |
| ---------------------------------- | ----------------------------------- | ----------------- |
| From Navbar click on  `Home`       | Home page loads with questions list | Works as expected |
| From Footer click on home icon     | Home page loads with questions list | Works as expected |
| From Navbar click on  `Contact Us` | Message create form loads           | Works as expected |
| From Footer click on envelope icon | Message create form loads           | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Navbar__
  ![navbar](docs/Screenshots/contactus-navbar.PNG)

__Footer__
  ![footer](docs/Screenshots/footer-desktop.PNG)
</details>
<hr>

__19.  I want users to be able to get feedback on their actions so that they'll know if their action was completed or failed:__

| Step                                        | Expected Result   | Actual Result     |
| ------------------------------------------- | ----------------- | ----------------- |
| `Upvote` or `Downvote` a question or answer | Feedback provided | Works as expected |
| Try to `Accept` an answer                   | Feedback provided | Works as expected |

<details>
<summary>Screenshots</summary>

__Upvote__
![upvote](docs/Screenshots/upvote-answer-desktop.PNG)

__Downvote__
![downvote](docs/Screenshots/downvote-answer-desktop.PNG)

__Vote Success__
![vote success](docs/Screenshots/notification-success-desktop.PNG)

__Vote Failed__
![vote failed](docs/Screenshots/notification-failed-desktop.PNG)

__Answer Accept Success Mobile__

![accept success](docs/Screenshots/notification-success-mobile.PNG)

</details>
<hr>

__20.   I want users to see the site's text fonts and colours clearly so that they can focus on the content without distraction:__

| Step                                          | Expected Result                                                                                                                              | Actual Result     |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Open `Home` and click on one of the questions | Home and question pages load with clear font of `Lato` and comfortable `black` colour font and `dark blue` vote buttons on a `white` surface | Works as expected |

<details>
<summary>Screenshots</summary>
  
__Questions List__
  ![questions list](docs/Screenshots/question-list-desktop.PNG)

__Question__
  ![question](docs/Screenshots/question-details.PNG)
</details>
<hr>


## Automated Testing

- All unit tests written for this site have been passed successfully.
  <details>
  <summary>How to Run Automated Testing </summary>

  - the testing command:

    `python3 manage.py test [app_name]`

  - Or generate test coverage reports using the coverage command:

    `coverage run --source=[app_name] --omit='*/migrations/*.py' manage.py test`

  - To get the coverage report results:

    `coverage html`
    `python3 -m http.server`

  - Open the browser and click on `htmlcov/` to see the report.
  </details>

  <details>
  <summary>Unit Test Result</summary>

  ![unit test result](docs/Validators/unit-test-result.PNG)
  </details>

  <details>
  <summary>Forum App Coverage Report</summary>

  ![forum coverage report](docs/Validators/forum-test-coverage.PNG)
  </details>

  <details>
  <summary>Contact Us App Coverage Report</summary>

  ![contact us coverage report](docs/Validators/contactus-test-coverage.PNG)
  </details>

  <details>
  <summary>Home App Coverage Report</summary>

  ![home coverage report](docs/Validators/home-test-coverage.PNG)
  </details>

  <details>
  <summary>Overall Coverage Report</summary>

  ![overall coverage report](docs/Validators/overall-test-coverage.png)
  </details>

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Configurations

## Login Credentials

| Username |  Password  | Admin? |
| :------- | :--------: | -----: |
| admin    | @dminPa$46 |      ✓ |
| ahmed    |  @hmed$90  |      X |

## Fork This Repository

<details>
<summary>How to fork this repository</summary>

1. On the top right of this page, click on the `Fork` button.
2. On `Create a new fork` update the repository's `name` and `description` if needed.
3. Then click on `Create fork`.

</details>

## Make Local Clone

<summary>How to make a local clone from this repository</summary>

1. On top of this page, click on the `<> Code` button.
2. Select "HTTPS" from the drop-down menu.
3. Click on the `clipboard` icon to copy the URL.
4. On your computer, open the terminal where you want to clone the repository.
5. Enter the command: `git clone [copied URL]` and press `Enter`.

</details>

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Credits

## Media

- Question not found: image is an <a href="https://www.freepik.com/free-vector/mistery-box-concept-illustration_24487830.htm#query=question%20not%20found&position=11&from_view=search&track=ais">image by storyset</a> on Freepik
- Error page 400: image is an <a href="https://www.freepik.com/free-vector/400-error-bad-request-concept-illustration_8030432.htm#query=400&position=1&from_view=search&track=sph">image by storyset</a> on Freepik
- Error page 403: image is an <a href="https://www.freepik.com/free-vector/403-error-forbidden-with-police-concept-illustration_8030434.htm#query=403&position=1&from_view=search&track=sph">image by storyset</a> on Freepik
- Error page 404: image is an <a href="https://www.freepik.com/free-vector/oops-404-error-with-broken-robot-concept-illustration_8030430.htm#query=404&position=2&from_view=search&track=sph">image by storyset</a> on Freepik
- Error page 500: image is an <a href="https://www.freepik.com/free-vector/500-internal-server-error-concept-illustration_8030427.htm#query=500&position=14&from_view=search&track=sph">image by storyset</a> on Freepik

## Documentations

- [Organizing models in a package](https://docs.djangoproject.com/en/1.11/topics/db/models/#organizing-models-in-a-package).
- [Bootstrap navbars](https://getbootstrap.com/docs/5.0/components/navbar/).
- [Built-in filter (safe)](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#safe)
- [Built-in filter (truncatewords)](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#truncatewords).
- [Django auto slug library](https://pypi.org/project/django-autoslug/).
- [Django testing overview](https://docs.djangoproject.com/en/4.1/topics/testing/overview/).
- [Django testing example](https://docs.djangoproject.com/en/1.11/topics/testing/tools/#overview-and-a-quick-example).
- [Pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/).
  
## Code

- Extending built-in user model is taken from [Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy).
- Some of the index HTML page and pagination code in the base file are taken from [Code Institute's blog starter](https://github.com/Code-Institute-Solutions/django-blog-starter-files/blob/master/templates/index.html).
- Generic views were developed based on [GeeksforGeeks](https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/) and [onespacemedia.com](https://www.onespacemedia.com/news/getting-started-generic-class-based-views-django/) posts.
- Getting to know about Django filters after [David](https://stackoverflow.com/questions/20095936/add-rich-text-format-functionality-to-django-textfield) and [heckj](https://stackoverflow.com/questions/3484149/limit-number-of-characters-with-django-template-filter) answers.
- Specifying login required for function-based views is from this [Stackoverflow thread](https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django).
- Adding value to many to many fields is an idea of [Daniel Roseman](https://stackoverflow.com/questions/1182380/how-to-add-data-into-manytomany-field).
- Code of getting the list of `ids` from many to many fields is taken from [Luan Fonseca](https://stackoverflow.com/questions/17388254/django-retrieving-ids-of-manytomany-fields-quickly).
- Counting the number of answers in a question is based on the [poke](https://stackoverflow.com/questions/65524039/django-template-exceptions-templatesyntaxerror-could-not-parse-some-characters) answer.
- style of the question and answer cards is taken from [CSSCodeLab](https://www.csscodelab.com/html-css-chat-bubble-design-example/).
- a user record in testing is taken from [Sam Dolan](https://stackoverflow.com/questions/3495114/how-to-create-admin-user-in-django-tests-py) answer.
- Testing the generic update view is based on [Kurt Peek answer](https://stackoverflow.com/questions/48814830/how-to-test-djangos-updateview)
- Dealing with the HTTP response context is based on [daveoncode answer](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages).
- Checking whether query sets are equal or not is done with the help of [Alasdair](https://stackoverflow.com/questions/45217691/django-check-if-querysets-are-equals
).
- The code of the filtering question in the search function is taken from [Bryce Siedschlaw](https://stackoverflow.com/questions/5956391/django-objects-filter-with-list).
- Ignoring letter cases when filtering is an idea from [Ron](https://stackoverflow.com/questions/11743207/how-to-query-case-insensitive-data-in-django-orm).
- Overriding the delete generic view function is inspired by [Django forum post](https://forum.djangoproject.com/t/overriding-delete-method-in-generic-delete-view-not-working-and-getting-warning/12089) and [Stackoverflow answer](https://stackoverflow.com/questions/57661025/how-to-prevent-deletion-of-django-model-from-django-admin-unless-part-of-a-casc).
- Using object database `id` to give a unique HTML `id` is based on [Aman Garg answer](https://stackoverflow.com/questions/64906475/how-to-set-the-id-of-an-html-element-with-django-variable).
- Error page messages taken from [Canva](https://www.canva.com/templates/EAFM6KBWneA-light-pink-light-blue-pastel-green-gradients-error-page-website-error-page/), [UXDesign](https://uxdesign.cc/designing-error-pages-that-actually-work-a8724f51a141), and [GeeksforGeeks](https://www.geeksforgeeks.org/http-status-codes-client-error-responses/?ref=rp).
- Media query code taken from [W3Schools](https://www.w3schools.com/css/css_rwd_mediaqueries.asp).
- Ignoring migrations' files on the coverage test command is taken from [Torsten Engelbrecht](https://stackoverflow.com/questions/4500785/how-can-i-exclude-south-migrations-from-coverage-reports-using-coverage-py).

## Errors Solving

- The template does not exist issue for delete views was resolved with the help of [Alasdair's answer](https://stackoverflow.com/questions/47894779/django-templatedoesnotexist-auth-user-confirm-delete-html).
- Fixing the error of `Error: Got an error creating the test database: permission denied to create database` while testing was done with the help of [kawadhiya21 answer](https://stackoverflow.com/questions/47466185/got-an-error-creating-the-test-database-django-unittest).
- Fixing word breaks in posts is taken from [Gready](https://stackoverflow.com/questions/29650189/how-to-disable-word-breaking-in-css) and [Peyman Mohamadpour](https://stackoverflow.com/questions/1165497/how-to-prevent-text-from-overflowing-in-css).
- Solving the `too long string` issue is done with the help of [FogleBird](https://stackoverflow.com/questions/8577027/how-to-declare-a-long-string-in-python).
- Fixing Heroku `pull rejected` crash because of static files was done with the help of [Aokiji answer](https://stackoverflow.com/questions/49266021/django-app-only-works-on-debug-true-heroku).
- Solving the `Heroku refused to connect` in WAVE tool and Am I Responsive Sites issue is done by installing the `Ignore X-Frame headers` Google Chrome extension, which is recommended by [Techsini post](https://techsini.com/unable-to-generate-mockup-of-your-website-here-is-the-quick-fix/)


[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)