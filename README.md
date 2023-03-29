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
    - [Modules and Packages](#modules-and-packages)
  - [Other Software and Tools](#other-software-and-tools)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Navbar](#navbar)
    - [Login](#login)
    - [Signup](#signup)
    - [Ask Questions](#ask-questions)
    - [Answer Questions](#answer-questions)
    - [Imporve Question/ Answer](#imporve-question-answer)
    - [Delete Question/ Answer](#delete-question-answer)
    - [Register Votes](#register-votes)
    - [Accept Answers](#accept-answers)
    - [Search Questions](#search-questions)
    - [User Votes](#user-votes)
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
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
- [Login Credentials](#login-credentials)
  - [Superuser](#superuser)
  - [Regular User](#regular-user)
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
9. I can edit my answers so that they are more clarified and updated. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
10. I can accept one of my questions' answers so that other users know it helped me. ![could have](https://img.shields.io/badge/could%20have-grey?style=flat)
11. I can upvote or downvote a question or answer to show how much this question or answer is helpful. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
12. I can see the vote score of my questions and answers on my profile, so I'll be encouraged to create more helpful questions and answers. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
13. I can contact the site's admin so that I can report an issue with the website or its content. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)

## Admin User

14. I can delete irrelevant questions so that users focus on answering valuable ones. ![could have](https://img.shields.io/badge/could%20have-grey?style=flat)
15. I can delete the irrelevant answers so that they won't distract users. ![could have](https://img.shields.io/badge/could%20have-grey?style=flat)
16. I can reply to users' messages so that I provide them with the required feedback and support. ![won't have](https://img.shields.io/badge/won't%20have-red?style=flat)

## Site Owner

17. I want users to be able to open the site on their mobile phone or tablet so that they'll have the same experience as on a desktop. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
18. I want users to be able to open any page wherever they are so that navigating through the site will be easy. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
19. I want users to be able to get feedback on their actions so that they'll know if their action was successfully completed or failed. ![should have](https://img.shields.io/badge/should%20have-aqua?style=flat)
20. I can see the site's text fonts and colours clearly so that I can focus on the content with no distraction. ![must have](https://img.shields.io/badge/must%20have-green?style=flat)
    
[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)


# Design

## Frontend

### Colours

The colour scheme created for the site is contrasted, which provides better accessibility and helps the user have a comfortable experience.
<details>
  <summary>The Colour Scheme</summary>

![colour scheme](docs/colour-scheme.PNG)
</details>

### Font

The font used in this site is 'Lato', which is a sans-serif, clean font that's commonly used in blogs and writing.
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

Models has been developed following OOP concepts trying to secure better maintenability and reduce redundancy.

<details>
  <summary>Models' Details</summary>
 
  - Classes `BasePost`, `Question` and `Answer` developed in `forum` app, `Message` in `contact_us` and `Profile` in `home` app. 
  - `BasePost` is the parent class of `Answer`  and `Question`, it contains their main attributes.
  - `Profile` is created to extend built-in `User` class features, a `Profile` record is created and linked with `User` each time the later is created.
  - Each model, except `Profile` and `BasePost`, has different type of generic views developed.
  - Unit tests for `forum` app created by inheriting a main test class, which contain test setup and inherits built-in `TestCase`.   
</details>

<details>
  <summary>Class Diagram For Models</summary>

![models' class diagram](docs/class-diagram.PNG)
</details>


[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

# Technologies

## Django Framework

## Python

### Modules and Packages

__Builts-in__ 

__Third Party__

## Other Software and Tools

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

# Features

## Existing Features

### Navbar

### Login

### Signup

### Ask Questions

### Answer Questions

### Imporve Question/ Answer

### Delete Question/ Answer

### Register Votes

### Accept Answers

### Search Questions

### User Votes

### Contact Us

### Inbox

### Footer

## Features Left to Implement

### Tags

### Reply to User Messages

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

# Validations

## Python

## Javascript

## HTML

## CSS

## Accessability

## Lighthouse

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

# Testing

## Manual Testing

## Automated Testing

## Bugs

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

# Login Credentials

## Superuser

## Regular User

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

# Configurations

## Fork This Repository

## Make Local Clone

## Deployment

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

# Credits

## Media

## Docs

## Code

## Acknowledgements

[<img src="docs/top-arrow.png" alt="Top arrow" title="Go Top" width="50"/>](#table-of-contents)

