# Special Relativity Website

## Design 

### Design Philosophy

### Front-end
The space-theme asthetic is handled using CSS, inside the style.css file. CSS handles all the futuristic page transitions and the layout of the page. While HTML pages contain information about what should be displayed. The *home*, *learn*, *stats*, *login*, *tests* and *sign-up* pages are linked HTML sheets while inside *stats* pagination is used. Javascript functions are used to validate forms instead of the server, as well as to handle the animations and navigation bar. All Javascript functions are placed inside the script.js file.  
### Back-end
The website is run using a flask server. Flask is a micro framework for the backend of the website. Jinja is used inside the HTML so the display can adapt to server data as well as for running loops. Users are saved inside a SQLite database. The username, password, and scores of the user are saved so progress can be encouraged.


## Intent 
The intent of the LSR website is to teach the public what the special theory of relativity is. People are often confused about what relativity is and use the words 'special relativity' without knowing there scientific meaning. Special relativity is sometimes counterintuitive but with real world examples it is easy to understand. People often find physics boring and hard to comprehend. To address this our website uses visuals, examples and quizzes to make learning engaging and memorable.

## Development 
Make a virtual environment:
In unix and mac:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
And make sure all packages are up to date:
```
$ pip3 install -r requirements.txt
```
The HTML pages are inside Website/app/templates and the CSS/Javascript are in  Website/app/static. Both can be altered to change the function and look of the website.
The main.py and config.py will not need to be changed as they are simply running the flask and SQLite. 
To change backend database management edit Wesbite/app/models.py.

## Deployment

```
$ pip3 install -r requirements.txt
$ python main.py
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
Move this chromedriver.exe to the *Website* folder.
```
$ pip3 install -r requirements.txt
$ python main.py
```
Then in a separate terminal:
```
$ python systemtest.py
```

## Authors
* Jordan Hartley
* Jasper Paterson
* Maxwell Dix-Matthews



## References
Albert Einstein photo ref: https://www.theguardian.com/books/2015/jun/12/five-reasons-we-should-celebrate-albert-einstein
