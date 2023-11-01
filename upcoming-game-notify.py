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

filtered_results = []

for date, team, time, home_or_away in zip(dates, teams, times, home_or_away):
    date_text = date.get_text(strip=True)
    team_text = team.get_text(strip=True)
    time_text = time.get_text(strip=True)
    home_away_text = home_or_away.get_text(strip=True)

    game_date = datetime.strptime(date_text, "%b %d, %Y").date()

    if one_week_ago <= game_date <= one_week_later:
        formatted_result = f"{date_text} | {home_away_text} | {team_text} | {time_text}"
        filtered_results.append((game_date, formatted_result))

filtered_results.sort(key=lambda x: x[0])

for game_date, formatted_result in filtered_results:
    if game_date > current_date:
        next_game = formatted_result
        break

if next_game:
    print("Next game:", next_game)
    next_game_parts = next_game.split("|")
    next_game_date = datetime.strptime(next_game_parts[0].strip(), "%b %d, %Y")
    next_game_time_raw = next_game_parts[3].strip().split()[0]
    next_game_time = datetime.strptime(next_game_time_raw, "%I:%M")
    
    cron_job_time = f"{next_game_time.minute} {next_game_time.hour + 12} {next_game_date.day} {next_game_date.month} *"
    
    # Modify ntfy.mydomain.com/mytopic to whatever you are using for ntfy messages. 
    command = f"/usr/bin/curl -d 'Texans | {next_game}' ntfy.mydomain.com/mytopic"
    subprocess.run(command, shell=True)
else:
    print("No games found within the specified date range.")
