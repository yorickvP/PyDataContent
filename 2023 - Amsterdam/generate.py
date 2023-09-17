from pathlib import Path
import requests
# load https://amsterdam2023.pydata.org/cfp/schedule/export/schedule.json from pretalx as json
schedule = requests.get('https://amsterdam2023.pydata.org/cfp/schedule/export/schedule.json').json()

# for each talk, generate a markdown file
# format: "Day N/room number - room name/start time - title/README.md"
for i, day in enumerate(schedule['schedule']['conference']['days']):
    day_path = Path(f"Day {i+1}")
    day_path.mkdir(exist_ok=True)
    for roomN, talks in enumerate(day['rooms'].values()):
        for talk in talks:
            # forward slash not allowed, replace with unicode forward slash
            talk_title = talk['title'].replace('/', '∕')
            talk_path = day_path / f"{roomN + 1} - {talk['room']}" / f"{talk['start']} - {talk_title}"
            talk_path.mkdir(exist_ok=True, parents=True)
            all_speakers = ", ".join([p['public_name'] for p in talk['persons']])
            with open(talk_path / 'README.md', 'w') as f:
                f.write(f"""# {talk['title']}
by {all_speakers}
* [Talk info]({talk['url']})
## Abstract
{talk['abstract']}
""")
