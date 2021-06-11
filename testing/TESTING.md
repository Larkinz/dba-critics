# Testing

View live version of the website [here](http://dba-critics.herokuapp.com/).

Milestone Project 3: Python and Data Centric Development – [Code Institute](https://codeinstitute.net/)

In this document you will find information about the testing procedures that I have used to make sure the website displays and functions correctly on most browsers and devices.

---

## Contents

- [**Browser compatibility**](#browser-compatibility)

  - Tested browsers and devices
  - What I tested
  - Browser compatibility testing results

- [**Mobile responsiveness**](#mobile-responsiveness)

- [**Lighthouse**](#lighthouse)

- [**Code validators**](#code-validators)

  - W3C - Markup Validation Service
  - W3C - CSS Validation Service
  - JSHint - JavaScript code quality checker
  - Python checker - Python code syntax checker
  - PEP8 online - Python code style checker

- [**Test cases**](#test-cases)

- [**Testing user stories**](#testing-user-stories)

- [**Bugs**](#bugs)

  - Solved bugs
  - Known bugs

---

## Browser compatibility

### Tested browsers and devices

I tested these browser versions on these devices:

**Desktop PC (64-bit, Windows 10):**

- Google Chrome Version 91.0.4472.77 (Official Build) (64-bit)
- Firefox Version 89.0 (64-bit)
- Microsoft Edge Version 91.0.864.41 (Official build) (64-bit)
- iOS (via https://www.browserstack.com/)

**Dell E7240 laptop (64-bit, Windows 10):**

- Opera Version 77.0.4054.60 (64-bit)

**Samsung Galaxy S7 (Android Version 8.0.0):**

- Samsung internet Version 13.2.2.4
- Brave Browser Version 1.23.76

### What I tested

List of things that I tested:

- If elements display correctly in size and order
- If images display correctly
- If all the (internal) links work
- If hover effects work
- If the JavaScript functionality works
- If the Python functionality works
- In general I tested the entire website, to see if it displayed and worked as intended.

### Browser compatibility testing results

**Google Chrome Version 91.0.4472.77 (Official Build) (64-bit):**

Everything is working and displaying as intended. [(screenshot)](testing-img/chrome.png)

**Firefox Version 89.0 (64-bit):**

Everything is working and displaying as intended. [(screenshot)](testing-img/firefox.png)

**Microsoft Edge Version 91.0.864.41 (Official build) (64-bit):**

Everything is working and displaying as intended. [(screenshot)](testing-img/edge.png)

**iOS:**

I've tested a couple of iOS 12 and 13 devices on [Browserstack](https://www.browserstack.com/). When I wasn't logged in there weren't any issues as you can see using this [iPhone 11 Pro](testing-img/iphone11pro.png) with iOS 13, the entire website displayed correctly. When I logged in there was a small display issue on the albums page, as you can see on this [iPad Air 2019](testing-img/ipadair2019.png) with iOS 13. The submit button was only half visible, but it was still clickable and functioning. The same issue occured when I tested an iPhone 8 with iOS 12, but the rest of the website had no issues, things like [the mobile navigation menu](testing-img/iphone8.png) all displayed correctly. Unfortunately I wasn't allowed to test any iOS 14 devices this time, but from previous experience it's likely that iOS 14 devices are performing equal if not better than older iOS devices, so I expect no major issues there.

**Opera Version 77.0.4054.60 (64-bit):**

Smooth scroll didn't work at first, but it turned out to be a browser setting similar to Google Chrome. So everything is working and displaying as intended. [(screenshot)](testing-img/opera.png)

**Samsung internet Version 13.2.2.4:**

Everything is working and displaying as intended. [(screenshot)](testing-img/samsung.jpg)

**Brave Browser Version 1.23.76:**

Everything is working and displaying as intended. [(screenshot)](testing-img/brave.jpg)

**_[Back to top](#contents)_**

---

## Mobile responsiveness

I've applied completely custom media queries throughout the website to achieve mobile responsiveness. To test the website for mobile responsiveness I've been using the Google Chrome devtools throughout the coding of the media queries. I manually used the sliders to adjust for different screen sizes, and I've also used all of the [pre-configured screen sizes](testing-img/devtools-phones.png) in the devtools to test if things looked okay, both in vertical and horizontal directions. Since the early stages of development I've also tested parts of the website on my Galaxy S7, this was possible because I deployed the website to Heroku at the beginning of the development process. Another thing I did was use [responsive design checker](https://responsivedesignchecker.com/) and [ami responsive design](http://ami.responsivedesign.is/) for some additional mobile responsiveness testing throughout the building of the website, since the Google Chrome devtools can behave a bit strange at times it's good to test responsiveness with more than a single tool.

**_[Back to top](#contents)_**

---

## Lighthouse

In the Google Chrome devtools I have used the Lighthouse feature to check: performance, accessibility, best practices and SEO indicators for my website. I recorded before and after scores of the desktop and mobile tests of both the homepage and albums page. Some test scores deviated between 1 and 6 points without making changes to the website, so take that into consideration. The images below this paragraph show the scores before making changes to my website, and the best scores that I've managed to achieve after making some recommended changes. I improved the performance score by: compressing and/or optimizing videos and images, adding SEO tags and a website description, and by adding aria labels and alt tags. During testing with Lighthouse is became obvious to me that using the Materialize framework and Flask with its Jinja templating caused a lot of errors or warnings resulting in lower scores, especially in accessibility.

![Desktop results lighthouse](testing-img/lh-desktop.png)

![Mobile results lighthouse](testing-img/lh-mobile.png)

**_[Back to top](#contents)_**

---

## Code validators

### W3C - Markup Validation Service

I've put the HTML code through the [W3C markup validator](https://validator.w3.org/), and I only got Flask/Jinja related errors that should be ignored.

### W3C - CSS Validation Service

I've put my style.css file through the [W3C CSS validator](https://jigsaw.w3.org/css-validator/) and it [passed without errors](testing-img/css-validation.png) on the second try, after removing some unnecessary background styling.

### JSHint - JavaScript code quality checker

I've put my script.js file through the [JSHint validator](https://jshint.com/) and it gave some warnings about missing a few semicolons. After adding those, I only got 1 ignorable warning about use strict, and 5 ignorable warnings related to some Materialize code.

![JavaScript validator warnings](testing-img/js-validation.png)

### Python checker - Python code syntax checker

I've checked my Python code syntax on the [extendsclass website](https://extendsclass.com/python-tester.html), and after removing the f-strings that gave errors (because I couldn't select my Python version and this checker is apparently not up to date with Python 3.6 or 3.9) I got no errors at all.

![Python syntax checker](testing-img/python-validation1.png)

### PEP8 online - Python code style checker

I've checked my Python code style to fit the PEP8 guidelines on the [PEP8online website](http://pep8online.com/), and after pushing down some lines of code that were too long I was only left with ignorable warnings for using multiple hashtags in a comment. I chose to do this to make my credits stand out against regular comments.

![Python PEP8 guidelines checker](testing-img/python-validation2.png)

**_[Back to top](#contents)_**

---

## Test cases

### Welcome page

1. Showcase:

   1.1 A full screen video clip should be playing in the background with no audio.

   1.2 Near the bottom half of the screen is a container containing 4 elements underneath each other: a title, a subtitle, a button to enter the website and a logo.

---

### General features

2. Top bar:

   2.1 The top bar will be visible at the top of the page.

   2.2 The top bar should be sticky.

   2.3 On big screen sizes the top bar should have a logo on the left and navigation links on the right.

   2.4 On mobile screen sizes the top bar should have a logo in the center and a hamburger menu icon on the right that triggers the mobile sidenav.

---

3. Mobile sidenav:

   3.1 The mobile sidenav has a logo in the top.

   3.2 Under the logo are the navigation links all underneath each other.

---

4. Footer:

   4.1 The footer has one piece of text in the middle saying "Dead by April".

   4.2 Underneath this text are 4 icons next to each other linking to social media channels.

---

5. Flash messages:

   5.1 On the login, register and albums pages flash messages can be displayed underneath the Top nav bar.

   5.2 The flash message is a piece of text displayed horizontally, alerting the user of an action.

---

### Homepage

6. Home section:

   6.1 Under the top bar the home section will be displayed.

   6.2 There is a header on the top left of the section saying "HOME'.

   6.3 Under the header are 2 subtitles and 2 corresponding paragraphs.

   6.4 The first subtitle says "Welcome!".

   6.5 The second subtitle says "Dead by April".

---

7. First parallax:

   7.1 Under the home section is a parallax image containing the cover art of Dead by April's single called Memory.

---

8. Band section:

   8.1 Under the first parallax the band section will be displayed.

   8.2 There is a header on the top left of the section saying "BAND".

   8.3 Under the header are 4 containers, each having a slider picture that changes every 8 seconds and some information of the corresponding band member next to it.

   8.4 On mobile screen sizes the slider pictures are displayed vertically with the information of the corresponding band member underneath.

---

9. Second parallax:

   9.1 Under the band section is a parallax image containing a picture of the band members and the cover art of Dead by April's single called Heartbeat.

---

10. Blog section:

    10.1 Under the second parallax the blog section will be displayed.

    10.2 There is a header on the top left of the section saying "BLOG".

    10.3 Under the header are 4 containers displayed 2 by 2, each contains: the blog title, date, text, and a read more button in it.

    10.4 Clicking on a read more button will activate an external link to the official Dead by April blog.

---

18. Third parallax:

    18.1 Under the blog section is a parallax image containing some Dead by April logo artwork.

---

11. Tour section:

    11.1 Under the third parallax the tour section will be displayed.

    11.2 There is a header on the top left of the section saying "TOUR".

    11.3 Under the header are 3 containers displayed underneath each other, each horizontally containing: the concert date, venue, location, RSVP button and a tickets button.

    11.4 Clicking on the RSVP or tickets button will activate an external link to an event ticket seller.

    11.5 On mobile screen sizes the information in the containers will be displayed vertically.

---

### Albums page

12. Album container:

    12.1 There are 4 album containers displayed underneath each other on the albums page, one for each Dead by April studio album.

    12.2 Each container has 3 collapsible headers containing: the album name, tracklist, and comments.

    12.3 At the bottom of each album container is a ratings container.

    12.4 The body of the album name collapsible header contains: the cover art of the album, and the album release year displayed underneath each other.

    12.5 The body of the tracklist collapsible header contains: the complete tracklist of the album, including bonus songs displayed underneath each other.

    12.6 The body of the comments collapsible header contains: a comment section exclusively for that album.

    12.7 When not logged in, the comment container has text on top saying "Log in to write a comment!", with an internal link to the login page. Comments are displayed underneath this text.

    12.8 When logged in, the comment container has a textarea on top, with a submit button underneath. Comments are displayed underneath this textarea.

    12.9 Each comment displays the username and the comment itself underneath each other.

    12.10 When logged in, edit and delete buttons will be displayed underneath a comment that is made by the corresponding user.

    12.11 Clicking the edit button will open a modal containing a textarea with the comment, the user can change the contents of the comment in here. Underneath is a submit button, and on the bottom right is a close button that closes the modal when clicked.

    12.12 Clicking the delete button will open a modal asking the user to confirm if he or she is sure about deleting the comment, this choice can be made by clicking either the yes or the no button which are displayed horizontally next to each other.

    12.13 In the ratings container the rating for each album is displayed, next to it between parentheses the total number of votes on the album are displayed.

    12.14 Underneath the rating a range input slider is displayed, ranging from 1 to 100.

    12.15 When not logged in, a text saying "log in to vote" is displayed under the range input slider.

    12.16 When logged in, if a user has voted on an album, their rating will be displayed under the range input slider. Also, a submit button is displayed under the user rating. This submit button can only be clicked after moving the slider.

---

### Log in page

13. Log in container:

    13.1 The log in container displayed in the center of the page contains 4 elements: a title, username input field, password input field, and a login button.

    13.2 The title says "Log in".

    13.3 The username input field has a label saying "Username" and placeholder text saying "USERNAME", and a user icon to the left.

    13.4 The password input field has a label saying "Password" and placeholder text saying "PASSWORD", and a password icon to the left.

    13.5 The login button says "LOG IN", and has an arrow icon to the right.

    13.6 Under the log in container is a text that says "New visitor? Register here.", with an internal link to the register page.

---

### Register page

14. Register container:

    14.1 The register container displayed in the center of the page contains 4 elements: a title, username input field, password input field, and a register button.

    14.2 The title says "Register".

    14.3 The username input field has a label saying "Username (a-z, 0-9)" and placeholder text saying "USERNAME", and an add user icon to the left.

    14.4 The password input field has a label saying "Password (Length: 8-24)" and placeholder text saying "PASSWORD", and a password icon to the left.

    14.5 The register button says "REGISTER", and has an arrow icon to the right.

    14.6 Under the register container is a text that says "Already registered? Log in here.", with an internal link to the log in page.

---

### 404 Error page

15. 404 Error container:

    15.1 The 404 error container displayed in the center of the page contains 2 elements: a title and a single line of text.

    15.2 The title says "Error 404: page not found".

    15.3 The text says "Take me back to the homepage.", with an internal link to the homepage.

---

### 405 Error page

16. 405 Error container:

    16.1 The 405 error container displayed in the center of the page contains 2 elements: a title and a single line of text.

    16.2 The title says "Error 405: page not found".

    16.3 The text says "Take me back to the homepage.", with an internal link to the homepage.

---

### 500 Error page

17. 500 Error container:

    17.1 The 500 error container displayed in the center of the page contains 2 elements: a title and a single line of text.

    17.2 The title says "Error 500: page not found".

    17.3 The text says "Take me back to the homepage.", with an internal link to the homepage.

**_[Back to top](#contents)_**

---

## Testing user stories

- As a visitor, I would like to see an overview of the upcoming tour, so that I know where and when the next concerts take place.

Large screen sizes:

1. After entering the website from the welcome page the visitor [will see a navigation link to the tour section](testing-img/tour-001.png) in the navigation bar.
2. After clicking this link the [tour section](testing-img/tour-002.png) will be visible, where the dates, venues, locations, and external links to ticket sellers will be displayed.

Smaller screen sizes:

1. After entering the website from the welcome page the visitor [will see a hamburger menu icon](testing-img/tour-003.png) on the right side of the top bar.
2. After clicking on this icon the mobile sidenav will be displayed, where [a navigation link to the tour section](testing-img/tour-004.png) is visible.
3. After clicking this link the [tour section](testing-img/tour-005.png) will be visible, where the dates, venues, locations, and external links to ticket sellers will be displayed.

---

- As a visitor, I would like to rate albums, so that I can compare the ratings with other fans.

All screen sizes:

1. After [logging in](testing-img/ratings-001.png) the visitor will be redirected to the albums page.
2. On the albums page, at the bottom of each album a [ratings container](testing-img/ratings-002.png) is displayed. The visitor can see: the average rating, the total number of votes, and their own rating (if any). Rating an album or updating your rating can be done by moving the slider (1 to 100) and pressing the submit button.

---

- As a visitor, I would like to discuss albums, so that I can share my thoughts with other fans.

All screen sizes:

1. After [logging in](testing-img/ratings-001.png) the visitor will be redirected to the albums page.
2. On the albums page, each album container has a [comments header](testing-img/comments-001.png).
3. After clicking on the comments header the [comments section](testing-img/comments-002.png) will be displayed. The visitor can communicate with other fans here by logging in and placing comments under each album.

---

- As a site owner, I would like our website to have an intuitive navigation system, so that visitors can easily find what they are looking for.

Large screen sizes:

1. On the welcome page an ["Enter site" button](testing-img/nav-001.png) is visible which links to the homepage.
2. On all the other pages on the right side of the top bar there are [navigation links](testing-img/nav-002.png) visible that are relevant to the current page that the visitor is on.

Smaller screen sizes:

1. On the welcome page an ["Enter site" button](testing-img/nav-001.png) is visible which links to the homepage.
2. On all the other pages the visitor [will see a hamburger menu icon](testing-img/tour-003.png) on the right side of the top bar.
3. After clicking on this icon the [mobile sidenav](testing-img/nav-003.png) will be displayed, where navigation links are visible that are relevant to the current page that the visitor is on.

---

- As a site owner, I would like to prevent unique visitors from voting twice, so that album ratings can't easily be cheated.

1. Each unique user account can only vote once on each album, voting twice will just [update their rating](testing-img/unique-vote-001.png) instead of adding another one.
2. Visitors can still create multiple accounts, however. Ideally a vote limit is set based on IP address, I've looked into this, but it was a bit too advanced to implement right now. This would also bring up other issues such as multiple people in one household being limited to a single vote, and people can cheat using a VPN.

**_[Back to top](#contents)_**

---

## Bugs

### Solved bugs

- There was a bug where comments without spaces would overflow the comment container, this was fixed by adding `overflow-wrap: break-word;` to the comment paragraph element.

- There was a bug that made scrollspy/smooth scroll not work because of the Flask Jinja href anchor tag syntax `{{ url_for('.homepage', _anchor='blog') }}` , this was fixed by making [different list elements](testing-img/bugfix-001.png) be displayed when on the homepage.

- There was an issue that made the anchor scroll not stop at the correct height because it didn't consider the top navbar height, this was fixed by adding `scroll-margin-top: 56px;` to each section element that had an anchor tag.

- There was a bug where the welcome page content would be outside the video background, this was fixed by giving both the welcome page html and body elements a unique ID, and then setting their height to 100% and overflow to hidden. Also, the `.landing-page-content` class needed top percentage styling media queries to not move into the hidden overflow.

- There was an [error logged in the console](testing-img/js-bug-001.png) related to [this JavaScript code](testing-img/js-bug-002.png), this was fixed by putting [all these functions](testing-img/js-bug-003.png) into a `window.onload` function, and adding an if statement checking for `null`.

### Known bugs

- On both the register and log in pages the [footer is not displayed at the bottom of the screen](testing-img/footer-bug-001.png), I encountered the same issue in a previous project and fixed it. This time however, I couldn't get it to work because of Flask/Jinja extending the base.html that contains the footer and body elements.

- On iOS versions 12 and 13 on the albums page the [rating submit button is only half visible](testing-img/just-another-one-of-those-apple-ios-bugs.png), but the functionality still works.

**_[Back to top](#contents)_**

---
