class PrisionersGame:
    """docstring for PrisionersGame"""
    def __init__(self, num_drawers):
        assert num_drawers % 2 == 0
        self.num_drawers = num_drawers
        self.max_attempts = int(self.num_drawers / 2)
        self.drawer_ids = list(range(1, num_drawers + 1))
        shuffled = self.drawer_ids[:]
        random.shuffle(shuffled)
        self.drawers = dict(zip(self.drawer_ids, shuffled))

# by 광영
#
def play_naive(self, player_number):
        """ Randomly open drawers """
        for attempt in range(self.max_attempts):
            if self.drawers[random.choice(self.drawer_ids)] == player_number:
                return True

    return False
