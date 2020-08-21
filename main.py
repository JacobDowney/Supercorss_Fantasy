import threading, time

import consts
import sheets
import moto_scraper


def main():
    player_picks = sheets.GetPlayerPicks()
    sheets.SetPlayerPicks(player_picks)

    riders = moto_scraper.GetInitialRiders()
    ticker = threading.Event()
    count = 0
    while not ticker.wait(consts.update_interval_seconds):
        updated_riders = moto_scraper.GetRiders()
        updates = []
        for i in range(0, len(player_picks)):
            picks = player_picks[i].picks
            for j in range(0, len(picks)):
                rider = riders.get(picks[j], None)
                updated_rider = updated_riders.get(picks[j], None)
                if rider == None or updated_rider == None:
                    continue
                if rider.position != updated_rider.position:
                    update = sheets.Update((j*2)+8, i+2, consts.points[updated_rider.position])
                    updates.append(update)
        sheets.CompleteUpdates(updates)
        riders = updated_riders
        count += 1
        if count >= 5:
            break



if __name__ == "__main__":
    main()
else:
    print("Incorrect usage")
