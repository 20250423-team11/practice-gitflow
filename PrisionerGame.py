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


        # 웅비님(수종본)
    def play_optimum(self, player_number):
        """ Open the drawer that matches the player number and then open the drawer
        with the revealed number.
        """
        prev_attempt = player_number
        for attempt in range(self.max_attempts):
            if self.drawers[prev_attempt] == player_number:
                return True
            else:
                prev_attempt = self.drawers[prev_attempt]

        return False
    
    @classmethod
    def victory(csl, results):
        """Defines a victory of a game: all players won"""
        return all(results)

    def play(self, approach):
        """Plays this game and returns a list of booleans with
        True if a player one, False otherwise"""
        return [approach(self, player) for player in self.drawer_ids]
