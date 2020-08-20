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

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_poition(self):
        return self.position

    def get_laps(self):
        return self.laps

    def get_gap(self):
        return self.gap

    def get_diff(self):
        return self.diff

    def get_last(self):
        return self.last

    def get_best(self):
        return self.best

    def get_in(self):
        return self.in_

    def get_active(self):
        return self.active


class Player:
    def __init__(self, name, points, picks, pick_lcq, pick_250):
        self.name = name
        self.points = points
        self.picks = picks
        self.pick_lcq = pick_lcq
        self.pick_250 = pick_250

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def get_picks(self):
        return self.picks

    def get_pick_lcq(self):
        return self.pick_lcq

    def get_pick_250(self):
        return self.pick_250


class RaceData:
    def __init__(self, title, event, session):
        self.title = title
        self.event = event
        self.session = session

    def get_title(self):
        return self.title

    def get_event(self):
        return self.event

    def get_session(self):
        return self.session
