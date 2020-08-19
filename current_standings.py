import requests
from bs4 import BeautifulSoup

import rider

def GetCurrentStandings():
    url = "http://www.americanmotocrosslive.com/xml/mx/RaceResultsWeb.xml"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    rider_infos = soup.find_all("b")
    riders = []
    for i in range(0, len(rider_infos)):
        rider_info = rider_infos[i]
        name = rider_info['f']
        number = int(rider_info['n'])
        position = int(rider_info['a'])
        laps = int(rider_info['l'])
        gap = format_time(rider_info['g'])
        diff = format_time(rider_info['d'])
        last = format_time(rider_info['ll'])
        best = format_time(rider_info['bl'])
        in_ = int(rider_info['in'])
        active = rider_info['s'] == "Active"
        newRider = rider.Rider(name, number, position, laps, gap, diff, last, best, in_, active)
        riders.append(newRider)
    return riders

def format_time(time):
    if time == "--.---":
        return float("0.0")
    if "lap" in time:
        return round(float(time.split()[0]) * -1, 3)
    if not ":" in time:
        return round(float(time), 3)
    split = time.split(":")
    return round((60.0 * float(split[0])) + float(split[1]), 3)
