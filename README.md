# UVM CS1210 Final Project 
`Dylan Pizura and Sylvan Franklin`

#### Dependencies
- python standard library: `random`, `typing`, `enum`

#### Run instructions
The game will prompt you on whether you want to play against another player or play against a random AI. It will then ask you to make a move on a grid via a coordinate (1-9), numbered right to left. If you are unfamiliar with the rules of ultimate tic tac toe I recommend watching a short youtube video [here](https://www.youtube.com/shorts/_Na3a1ZrX7c). But the basic rules are as follows:

1. Player one makes a move on one of nine smaller boards.
2. Player two makes a move on the corresponding big board.
3. Repeat steps **1** and **2** until a board is won.
4. When three boards in a row are won, the game is over. 

In the event that a board is full you may choose to move anywhere. 

#### Testing
We tested both the computer and two player functions through rigorous testing. We tested proper and improper input values, and made sure that every potential situation was covered by the programs internal logic. 

#### Work Distribution

We each had a couple of designated tasks, but did most of the work together in person. 

**Sylvan**: 
- board printing and colors
- final win logic
- this markdown file

**Dylan**: 
- game initialization 
- computer player functionality
- input validation

**Together**:
- movement logic 
- win check functionality
- turn logic

#### Citations

I borrowed the ANSI color class `fg` from [this](https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803) this replit article. 
     

