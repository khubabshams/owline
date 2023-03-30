<kbd>[<img src="docs/owline-logo.png" alt="Owline logo" title="Owline Live Site" width="200"/>](https://owline.herokuapp.com)</kbd>

[Owline Live Site](https://owline.herokuapp.com)


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
  - [Bugs](#bugs)
- [Login Credentials](#login-credentials)
- [Configurations](#configurations)
  - [Fork This Repository](#fork-this-repository)
  - [Make Local Clone](#make-local-clone)
  - [Deployment](#deployment)
- [Credits](#credits)
  - [Media](#media)
  - [Docs](#docs)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)


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
4. I can be logged in so that I can ask or answer questions. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
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

1. I can view and filter the listed questions so that I will be able to read them:


    | Step                                                                 | Expected Result                                                                                                                | Actual Result     |
    | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
    | Open https://owline.herokuapp.com/                                   | Home page loads with questions list                                                                                            | Works as expected |
    | Enter keywords in the search input to filter questions and hit enter | URL will change to https://owline.herokuapp.com/forum/search/ and only questions with at least one keyword will be on the list | Works as expected |
    | When a keyword is not found in all questions                         | URL will change to https://owline.herokuapp.com/forum/search/ and a message of "Sorry, There's no question found!" shows       | Works as expected |

    <details>
      <summary>Screenshots</summary>
      
    __Navbar -> Home__
      ![navbar home](docs/Screenshots/nav-desktop.PNG)

    __Question List__
      ![question list](docs/Screenshots/question-list-desktop.PNG)

    __Search__
      ![search](docs/Screenshots/search-desktop.PNG)

    __Search Succeeded__
      ![search success](docs/Screenshots/search-success.PNG)

    __Question Not Found__
      ![search not found](docs/Screenshots/search-not-found.PNG)
    </details>
<hr>

2. I can be able to open a question's details so that I can read the answers:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

3. I can sign up so that I can access more of the site's features:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

4. I can be logged in so that I can ask or answer questions:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

5. I can search for specific questions so that I will avoid question duplication:
 
    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

6. I can ask a question so that I can get an answer:
 
    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

7. I can edit a question so that it is more clearly answered:
  
    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

8. I can answer a question so that my answer could help someone:
  
    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

9.  I can edit an answer so that they are more clarified and updated:
  
    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

10. I can accept one of my questions' answers so that other users know it helped me:
  
    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

11. I can upvote or downvote a question or answer to show how much this question or answer is helpful:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

12.  I can see the vote score of my questions and answers on my profile, so I'll be encouraged to create more helpful questions and answers:
 
    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

13. I can contact the site's admin so that I can report an issue with the website or its content:
    
| Step                               | Expected Result                     | Actual Result     |
| ---------------------------------- | ----------------------------------- | ----------------- |
| Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

  <details>
    <summary>Screenshots</summary>
    
    __Navber -> Home__
    ![navbar home](docs/Screenshots/nav-desktop.PNG)
  </details>

14. I can delete duplicated or irrelevant questions so that users focus on answering valuable ones:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

15. I can delete the irrelevant answers so that they won't distract users:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

16. I can reply to users' messages so that I provide them with the required feedback and support:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

17. I want users to be able to open the site on their mobile phone or tablet so that they'll have the same experience as on a desktop:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

18. I want users to be able to open any page wherever they are so that navigating through the site will be easy:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

19. I want users to be able to get feedback on their actions so that they'll know if their action was successfully completed or failed:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
      </details>
<hr>

20. I want users to see the site's text fonts and colours clearly so that they can focus on the content without distraction:

    | Step                               | Expected Result                     | Actual Result     |
    | ---------------------------------- | ----------------------------------- | ----------------- |
    | Open https://owline.herokuapp.com/ | Home page loads with questions list | Works as expected |

      <details>
        <summary>Screenshots</summary>
        
        __Navbar -> Home__
        ![navbar home](docs/Screenshots/nav-desktop.PNG)
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

## Bugs

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Login Credentials

| Username |  Password  | Admin? |
| :------- | :--------: | -----: |
| admin    | @dminPa$46 |      ✓ |
| ahmed    |  @hmed$90  |      X |

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Configurations

## Fork This Repository

## Make Local Clone

## Deployment

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)
<hr>

# Credits

## Media

## Docs

## Code

## Acknowledgements

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)