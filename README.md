# Tick Tack Toe AI
Tic Tac Toe game made with pyhton where simple AI playes against you.

Note:
  Game has still few bugs and is not quite finished.
  Main idea here was to test making very simple AI which learns from previous rounds and thus becomes better.
  AI is not using any machine learning models.

How the AI works:
  After every round, the game writes data from the game (where each player placed the X and O and what was the outcome of the game).
  When it's the AIs turn, the AI decides it's move by seeing what is the best current move to win based on the data.
  If AI doesn't have any data yet, it makes a random move.
  More data AI collects, more precises it's moves will become.
