from csgo_abm.main import Game, CsgoModel

game = Game()
model = CsgoModel(10)
for i in range(15):
    print('Round nr:', i)
    model.step()
agent_vars = model.datacollector.get_agent_vars_dataframe()
agent_vars.unstack().to_csv('reports/agent_vars.csv')
print(model.scoreboard)
