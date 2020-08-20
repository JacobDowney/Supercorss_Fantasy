import requests
from bs4 import BeautifulSoup
import json

import consts

class Rider:
    def __init__(self, name, number, position, laps, gap, diff, last, best, in_, active):
        self.name = name
        self.number = number
        self.position = position
        self.laps = laps
        self.gap = gap
        self.diff = diff
        self.last = last
        self.best = best
        self.in_ = in_
        self.active = active

class RaceData:
    def __init__(self, title, event, session):
        self.title = title
        self.event = event
        self.session = session

    def __init__(self, race_data_info):
        self.title = race_data_info['t']
        self.event = race_data_info['e']
        self.session = race_data_info['s']


def GetStatus():
    url = consts.race_data_url
    race_data_json = json.loads(requests.get(url).content)
    status = race_data_json['B']
    if status == "Session Complete":
        return consts.status_complete
    return consts.status_unknown

def GetRaceData():
    url = consts.xml_url
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    race_data_info = soup.find_all("a")[0]
    return RaceData(race_data_info)

def GetStandings():
    url = consts.xml_url
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    rider_infos = soup.find_all("b")
    riders = []
    for rider_info in rider_infos:
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
        rider = Rider(name, number, position, laps, gap, diff, last, best, in_, active)
        riders.append(rider)
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
