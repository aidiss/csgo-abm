from rules import Game, Player, Team


def test_kill_reward():
    # Kill reward. In all modes, killing an enemy player rewards $300 to the killer.
    player = Player()
    game = Game()
    player.money = 800
    game.award_kill_reward(player)
    assert player.money == 1100


def test_t_wins_by_elimination():
    # Winning team receives $3250 if they won by eliminating the enemy team.
    game = Game()
    game.t_side = [Player() for _ in range(5)]
    game.ct_side = [Player() for _ in range(5)]
    game.end_round(winner='t', reason='elimination')
    t_money = sum([p.money for p in game.t_side])
    assert t_money == 20250


def test_ct_wins_by_time():
    # All Counter-Terrorists receive $3250 if they won running down the time.
    game = Game()
    game.t_side = [Player() for _ in range(5)]
    game.ct_side = [Player() for _ in range(5)]
    game.end_round(winner='ct', reason='time')
    t_money = sum([p.money for p in game.ct_side])
    assert t_money == 20250


def test_ct_wins_by_defusal():
    # In Bomb Defusal, all Counter-Terrorists receive $3600 if they won by defusing the bomb.
    game = Game()
    game.t_side = [Player() for _ in range(5)]
    game.ct_side = [Player() for _ in range(5)]
    game.end_round(winner='ct', reason='defusal')
    t_money = sum([p.money for p in game.ct_side])
    assert t_money == 4000


def test_t_wins_by_detonation():
    # In Bomb Defusal, all Terrorists receive $3500 if they won by detonating the bomb.
    game = Game()
    game.t_side = [Player() for _ in range(5)]
    game.ct_side = [Player() for _ in range(5)]
    game.end_round(winner='t', reason='detonation')
    t_money = sum([p.money for p in game.t_side])
    assert t_money == 4000


def test_award_losing_team():
    game = Game()
    game.round = 2
    game.rounds = 't'
    game.end_round(winner='t', reason='elimination')

    # $1400 after losing the first round
    # $1900 after losing 2 rounds in a row
    # $2400 after losing 3 rounds in a row
    # $2900 after losing 4 rounds in a row
    # $3400 after losing 5 or more rounds in a row
