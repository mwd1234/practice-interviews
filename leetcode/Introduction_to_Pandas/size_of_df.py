# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+
# Write a solution to calculate and display the number of rows and columns of players.

# Return the result as an array:

# [number of rows, number of columns]

# The result format is in the following example.

import pandas as pd

def get_dataframe_size(players: pd.DataFrame) -> list[int]:
    rows, columns = players.shape

    return [rows , columns]

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

print(get_dataframe_size(pd.DataFrame(student_data)))