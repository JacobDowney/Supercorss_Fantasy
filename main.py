import threading, time
from operator import attrgetter

import consts
import sheets
import moto_scraper


def main():
    player_picks = sheets.GetPlayerPicks()
    sheets.SetPlayerPicks(player_picks)
    leaderboard_col = len(player_picks) + 3
    timing_names_col = len(player_picks) + 4
    timing_times_col = len(player_picks) + 5

    riders = {}
    leaderboard_riders = [""] * consts.num_riders
    timed_riders = [["", -1.0]] * consts.num_riders

    ticker = threading.Event()
    count = 0
    while not ticker.wait(consts.update_interval_seconds):
        updated_riders = moto_scraper.GetRiders()
        updates = []
        # Updating the player picks section with new points
        for i in range(0, len(player_picks)):
            picks = player_picks[i].picks
            for j in range(0, len(picks)):
                updated_rider = updated_riders.get(picks[j], None)
                if updated_rider == None: # This rider is not in the main
                    continue
                rider = riders.get(picks[j], None)
                if rider == None or rider.position != updated_rider.position:
                    update = sheets.Update((j*2)+8, i+2, consts.points[updated_rider.position])
                    updates.append(update)
        riders = updated_riders

        # Updating the leaderboard with new changes
        # updated_leaderboard_riders = updated_riders[consts.sorted_riders]
        # for i in range(0, consts.num_riders):
        #     updated_rider_name = updated_leaderboard_riders[i].name
        #     if leaderboard_riders[i] != updated_rider_name:
        #         update = sheets.Update(i+2, leaderboard_col, updated_rider_name)
        #         updates.append(update)
        # leaderboard_riders = updated_leaderboard_riders
        # # Updating the timing board with new changes
        # updated_timed_riders = sorted(updated_leaderboard_riders, key=attrgetter("last"))
        # for i in range(0, consts.num_riders):
        #     updated_timed_rider = updated_timed_riders[i]
        #     if timed_riders[i][1] == -1.0 or timed_riders[i][0] != updated_timed_rider.name:
        #         update_name = sheets.Update(i+2, timing_names_col, updated_timed_rider.name)
        #         update_time = sheets.Update(i+2, timing_times_col, updated_timed_rider.last)
        #         updates.extend([update_name, update_time])
        #         timed_riders[i] = [updated_timed_rider.name, updated_timed_rider.last]

        sheets.CompleteUpdates(updates)



if __name__ == "__main__":
    main()
else:
    print("Incorrect usage")
