# Shop Score Page

This [site](http://80.211.16.55) shows max wait time in online store. Site refreshes every 10 seconds.
Layout of this site is sutable for all type of screens (laptops, smartphones etc).

# Deploy on localhost

Linux:
```bash
$ export FLASK_APP=server.py
$ export SECRET_KEY='your secret key'
```
For debug mode use variable FLASK_DEBUG=1
```
$ export FLASK_DEBUG=1
$ flask run
```

Then open the page [localhost:5000](http://localhost:5000) in browser.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
