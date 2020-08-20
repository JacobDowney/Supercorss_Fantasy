import gspread
from oauth2client.service_account import ServiceAccountCredentials

import consts
import types

def GetPlayers():
    sheet = get_sheet()
    row1 = sheet.row_values(1)
    players = []
    for i in range(2, len(row1)+1):
        name = sheet.cell(1, i).value
        points = sheet.cell(2, i).value
        picks = []
        for j in range(3, 7):
            picks.append(sheet.cell(j, i).value)
        pick_lcq = sheet.cell(7, i).value
        pick_250 = sheet.cell(8, i).value
        player = types.Player(name, points, picks, pick_lcq, pick_250)
        players.append(player)
    return players

def get_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    return client.open(consts.sheet_name).sheet1
