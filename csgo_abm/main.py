from itertools import cycle
from random import choice, random

from mesa import Agent, Model
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation

from csgo_abm.rules import Game


class Player(Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model, team):
        super().__init__(unique_id, model)
        self.money = 800
        self.team = team
        self.hp = 100
        self.primary_weapon = None
        self.secondary_weapon = None
        self.nades = []
        self.defuse_kit = False
        self.kills = 0
        self.deaths = 0

    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)

    def step(self):
        self.buy_awp()
        self.buy_rifle()
        if self.hp <= 0:
            print("dead")
            return

        target = choice(self.model.players)
        if self.primary_weapon == "awp":
            self.kill(target)
            target.die()
            self.money += 300
            self.kills += 1
        elif random() < 0.5:
            self.kill(target)
            target.die()
            self.money += 300
            self.kills += 1

    def kill(self, player):
        player.hp = 0

    def buy_awp(self):
        if not self.primary_weapon and self.money >= 4750:
            self.money -= 4700
            self.primary_weapon = "awp"

    def buy_rifle(self):
        if not self.primary_weapon and self.money >= 3000:
            self.money -= 3000
            self.primary_weapon = "rifle"

    def die(self):
        self.hp = 0
        self.primary_weapon = None
        self.secondary_weapon = None
        self.nades = None
        self.defuse_kit = None
        self.deaths += 1


class CsgoModel(Model):
    """A model with some number of agents."""

    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.players = []
        self.scoreboard = []
        dc = DataCollector(model_reporters=None, agent_reporters={"money": "money"})
        self.datacollector = dc

        # Create agents
        for i, team in zip(range(self.num_agents), cycle(["t", "ct"])):
            player = Player(i, self, team=team)
            self.schedule.add(player)
            self.players.append(player)

    def __repr__(self):
        return "Model"

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.schedule.step()
        winner = choice(["t", "ct"])
        self.scoreboard.append(winner)
        for player in self.players:
            if player.team == winner:
                player.money += 3000
            elif player.team != winner:
                player.money += 2500
            if player.money >= 16000:
                player.money = 16000
        for player in self.players:
            print(player)
        for player in self.players:
            player.hp = 100
