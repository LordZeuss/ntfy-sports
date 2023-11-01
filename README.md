# ntfy-sports
Scrape data on sports teams and send that data to you via ntfy messages.

## General Information:
This repo is a collection of scripts I threw together to scrape data from CBS sports pages in order to grab data and push that data via ntfy. I will eventually modify the scripts to be more plug-n-play, but for now, it's functional. I know the scripts and the code are crude. I got it functional, and that was good enough for me (for the time being lol).

---

## Requirements
* Python
  * BeautifulSoup4
  * Requests
* ntfy topic (and/or your own ntfy instance)

---

## Getting Started:

Clone the repo
```
git clone https://github.com/lordzeuss/ntfy-sports
```

Install Python dependencies
```
pip install -r requirements.txt
```

---

## How do I use it?
Take a look at any of the scripts. You will notice there is a url to the schedule of a particular sports team on CBS's website. Replace that link with the team link you are trying to grab data from.

The scripts are looking for certain elements on the page, so you can only use CBS's site. If you are technical enough, you can change this, or pull more info as needed/wanted.

By default, some info is pulled. Here is an example output message you would receive via ntfy:
```
Texans | Oct 29, 2023 | @ | Carolina | L15-13
Texans | Nov 5, 2023 | vs | Tampa Bay | 1:00 pm

Record: 3-4-0 Overall • 1-1-0 AFC • 2nd South
```
Another example where it is the next upcoming game:
```
Texans | Nov 5, 2023 | vs | Tampa Bay | 1:00 pm
```

---

## What do I need to change to make it work for the team I want?
* Modify the wanted script's `url` value to use the team schedule from CBS sports. Use the default Texans one as an example.
* (OPTIONAL) Modify the date range for how many games you want. Default is 7 days but this can be changed to your desire.
* Depending on the script, you may need to also modify `url2` to be the team page instead of the schedule. Use Texans page as an example.
* Modify the `Texans` text near the end of the script, to the name of the team you are looking for. This is just text that will show in the message, and is hard set here.
* At the end of the script, modify the ntfy server, and topic to whatever you are using. Replace `ntfy.mydomain.com/mytopic` to whatever you will be using.

---

## Automatic Updates
If you want a script to run periodically, use cronjobs to run the script periodically. Here is how I use each script:

* todays-games.py | Check for any games today. Notify if there is.
* schedule-check-notify.py | Check the team's schedule 7 days before & after the current date, and then send a push notification with that data.
* upcoming-game-notify.py | Check the next upcoming game, and send a push notification with that data.














