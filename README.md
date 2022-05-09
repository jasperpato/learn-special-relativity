# Special Relativity Website

## Design

### Design Philosophy

We aimed for our design to be visually engaging within the space aesthetic, including futuristic page transitions, animations and parallax effects when the mouse moves. The website is designed to keep users interested in space and in special relativity.

The website is also designed to be customisable. As a reward for good test scores, a user is given the opportunity to change the theme to four different colours. This makes user feel more connected to the site adds to the beauty.

### Front-end

The space-theme aesthetic is handled using CSS, inside the style.css file. CSS handles all the futuristic page transitions and the layout of the page. While HTML pages contain information about what should be displayed. The _home_, _learn_, _login_, _tests_ and _sign-up_ pages are linked HTML sheets while inside _lessons_ and _stats_ pagination is used. Javascript functions are used to validate forms instead of the server, as well as to handle the animations and navigation bar. All Javascript functions are placed inside the script.js file.

### Back-end

The website is run using a flask server. Flask is a micro framework for the backend of the website. Jinja is used inside the HTML so the display can adapt to server data as well as for running loops. Users and test attempts are saved inside a SQLite database. The username, password, and scores of the user are saved so progress can be encouraged.

## Intent

The intent of the LSR website is to educate about the theory of special relativity. A reasonable, high school level knowledge of maths and physics is assumed so that the lessons can be conveyed properly. Special relativity is sometimes counterintuitive but with real world examples it can be easy to understand. People often find physics boring and hard to comprehend. To address this our website uses visuals, examples and quizzes to make learning engaging and memorable.

## Development

Make a virtual environment:
On Mac:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

And make sure all packages are up to date:

```
(venv) $ pip3 install -r requirements.txt
```

The HTML pages are inside Website/app/templates and the CSS/Javascript are in Website/app/static. Both can be altered to change the function and look of the website.
The main.py and config.py will not need to be changed as they are simply running the flask and SQLite.
To change backend database management edit Wesbite/app/models.py.

## Deployment

```
$ pip3 install -r requirements.txt
$ python3 main.py
```

This will install the needed packages and start the server at http://127.0.0.1:5000/

## Running Tests

### Unit Test

Open the root directory

```
$ pip3 install -r requirements.txt
$ python tests.py
```

### Selenium

Selenium needs a chromedriver to run.
Go to https://sites.google.com/a/chromium.org/chromedriver/downloads and download the chromedriver fitting your current chrome.
Move this chromedriver.exe to the _Website_ folder.

```
$ pip3 install -r requirements.txt
$ python3 main.py
```

Then in a separate terminal:

```
$ python3 systemtest.py
```

## Authors

- Jordan Hartley
- Jasper Paterson
- Maxwell Dix-Matthews

## References

Albert Einstein photo ref: MPI/Getty Images
Diagrams by Jasper Paterson and Simon Dransfield
Background art by Jordan Hartley
