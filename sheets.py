import gspread
from oauth2client.service_account import ServiceAccountCredentials

import consts

class PlayerPick:
    def __init__(self, name, points, picks, pick_lcq, pick_250):
        self.name = name
        self.points = points
        self.picks = picks
        self.pick_lcq = pick_lcq
        self.pick_250 = pick_250

class Update:
    def __init__(self, row, col, info):
        self.row = row
        self.col = col
        self.info = info


def GetPlayerPicks():
    sheet = get_sheet(consts.sheet_picks)
    row1 = sheet.row_values(1)
    player_picks = []
    for i in range(2, len(row1)+1):
        name = sheet.cell(1, i).value
        points = sheet.cell(2, i).value
        picks = []
        for j in range(3, 7):
            picks.append(sheet.cell(j, i).value)
        pick_lcq = sheet.cell(7, i).value
        pick_250 = sheet.cell(8, i).value
        player_pick = PlayerPick(name, points, picks, pick_lcq, pick_250)
        player_picks.append(player_pick)
    return player_picks

def SetPlayerPicks(player_picks):
    sheet = get_sheet(consts.sheet_results)
    for i in range(2, len(player_picks)+2):
        player_pick = player_picks[i-2]
        sheet.update_cell(1, i, player_pick.name)
        sheet.update_cell(2, i, player_pick.pick_lcq)
        sheet.update_cell(3, i, 0)
        sheet.update_cell(4, i, player_pick.pick_250)
        sheet.update_cell(5, i, 0)
        # Nothing for sheet cell 6
        sheet.update_cell(7, i, player_pick.picks[0])
        sheet.update_cell(8, i, 0)
        sheet.update_cell(9, i, player_pick.picks[1])
        sheet.update_cell(10, i, 0)
        sheet.update_cell(11, i, player_pick.picks[2])
        sheet.update_cell(12, i, 0)
        sheet.update_cell(13, i, player_pick.picks[3])
        sheet.update_cell(14, i, 0)
        sheet.update_cell(18, i, player_pick.points)
    sheet.update_cell(1, len(player_picks)+3, consts.leaderboard)
    sheet.update_cell(1, len(player_picks)+4, consts.timing_names)
    sheet.update_cell(1, len(player_picks)+5, consts.timing_times)

def SetInfoBoards():
    sheet = get_sheet(consts.sheet_results)
    num_players = len(sheet.row_values(1)) - 1


def CompleteUpdates(updates):
    sheet = get_sheet(consts.sheet_results)
    for update in updates:
        sheet.update_cell(update.row, update.col, update.info)


def get_sheet(sheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    return client.open(consts.sheet_name).worksheet(sheet_name)

SetInfoBoards()
