from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import subprocess

# Update this with the CBS schedule of your team
url = "https://www.cbssports.com/nfl/teams/HOU/houston-texans/schedule/regular/"


current_date = datetime.now().date()

one_week_later = current_date + timedelta(days=7)
one_week_ago = current_date - timedelta(days=7)

response = requests.get(url)
page = BeautifulSoup(response.text, "html.parser")

dates = page.find_all(class_="CellGameDate")
teams = page.find_all(class_="TeamName")
times = page.find_all(class_="CellGame")
home_or_away = page.find_all(class_="CellLogoNameLockup-opposingPrefix")

# Update this url with the team page of your team
url2 = "https://www.cbssports.com/nfl/teams/HOU/houston-texans/"
response2 = requests.get(url2)
page2 = BeautifulSoup(response2.text, "html.parser")
record = page.find(class_="PageTitle-description")
record_clean = record.get_text(strip=True)

filtered_results = []

for date, team, time, home_or_away in zip(dates, teams, times, home_or_away):
    date_text = date.get_text(strip=True)
    team_text = team.get_text(strip=True)
    time_text = time.get_text(strip=True)
    home_away_text = home_or_away.get_text(strip=True)

    game_date = datetime.strptime(date_text, "%b %d, %Y").date()

    if one_week_ago <= game_date <= one_week_later:
        formatted_result = f"Texans | {date_text} | {home_away_text} | {team_text} | {time_text}"
        filtered_results.append(formatted_result)

filtered_results.append(f"\nRecord: {record_clean}")

output = "\n".join(filtered_results)

# Modify ntfy.mydomain.com/mytopic to whatever you are using for ntfy messages.
command = f"/usr/bin/curl -d '{output}' ntfy.mydomain.com/mytopic"
subprocess.run(command, shell=True)
