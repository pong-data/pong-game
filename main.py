
import os
import pandas as pd
import pongv5 as game

# run the game
score = game.pong_game()

print(score)

# save input and scores
df_score = pd.DataFrame(data=score, index=[0])

if os.path.exists("output/scores.csv"):
    score_table = pd.read_csv("output/scores.csv")
    score_table = score_table.append(df_score, ignore_index=True)
    score_table.to_csv("output/scores.csv", index=False)
else:
    df_score.to_csv("output/scores.csv", index=False)
