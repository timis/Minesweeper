# Minesweeper

This was mostly aimed at seeing if I could implement a crude version of minesweeper in a limited timeframe. Done in preparation for a Triplebyte interview (as recommended by them)

Invoke using "python3 Minesweeper.py"

It will ask you for the size of the board and the number of bombs. At the moment it will not autoreveal touching 0 tiles, nor will it guarantee you a safe starting click.

Moves should be of the form "C # #" or "F # #" where C will click the tile at (#, #) and F will flag the tile at (#, #). The first number corresponds to the row, the second to the column