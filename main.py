import requests
from requests import get
import sqlite3
import atoma

# Init connection to sqllite3 local database to persist records using cursor
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

url = "https://status.astronomer.io/history.atom"
xml = get(url)
response = requests.get(url)
feed = atoma.parse_atom_bytes(response.content)
cursor.execute("CREATE TABLE if not exists  serviceoutages(service, incident type UNIQUE, title, reporttime)")

#Iterate over all entries in the feed to fetch the incident details, avoid duplicates using replace into clause
for item in feed.entries:
    incident = item.id_.split(":")[-1]
    print(incident, item.title.value, item.published)
    sql = "INSERT OR REPLACE INTO serviceoutages (service, incident, title, reporttime ) VALUES (?, ?, ?, ?)"
    cursor.execute(sql, ("astro", incident, item.title.value, item.published))
    conn.commit()
