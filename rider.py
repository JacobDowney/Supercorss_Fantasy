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
