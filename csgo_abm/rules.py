class Player:
    def __init__(self):
        self.money = 800


class Team:
    def __init__(self):
        self.players = []


class Game:
    def __init__(self):
        self.round = 1
        self.rounds = []
        self.teams = []
        self.t_side = []
        self.ct_side = []

    def award_winning_team(self):
        pass

    def award_kill_reward(self, player):
        player.money += 300

    def end_round(self, winner, reason):
        if winner == "t":
            if reason in ["elimination", "time"]:
                for p in self.t_side:
                    p.money += 3250

                for p in self.ct_side:
                    p.money += 2000
        elif winner == "ct":
            if reason in "elimination":
                for p in self.ct_side:
                    p.money += 3250
                for p in self.t_side:
                    p.money += 2000
            elif reason == "defuse":
                for p in self.ct_side:
                    p.money += 3600
                for p in self.t_side:
                    p.money += 2000
            elif reason == "time":
                for p in self.ct_side:
                    p.money += 3250
                for p in self.t_side:
                    p.money += 2000
