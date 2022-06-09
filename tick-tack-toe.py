import csv
import pandas as pd
import numpy as np
import random
import sys

def computerBlock(grid):
    if grid[1] == 'X' and grid[2] == 'X' and grid[3] == 3:
        return 3
    elif grid[1] == 'X' and grid[2] == 2 and grid[3] == 'X':
        return 2
    elif grid[1] == 1 and grid[2] == 'X' and grid[3] == 'X':
        return 1
    elif grid[1] == 'X' and grid[4] == 'X' and grid[7] == 7:
        return 7
    elif grid[1] == 'X' and grid[4] == 4 and grid[7] == 'X':
        return 4
    elif grid[1] == 1 and grid[4] == 'X' and grid[7] == 'X':
        return 1
    elif grid[2] == 'X' and grid[5] == 'X' and grid[8] == 8:
        return 8
    elif grid[2] == 'X' and grid[5] == 5 and grid[8] == 'X':
        return 5
    elif grid[2] == 2 and grid[5] == 'X' and grid[8] == 'X':
        return 2
    elif grid[3] == 'X' and grid[6] == 'X' and grid[9] == 9:
        return 9
    elif grid[3] == 'X' and grid[6] == 6 and grid[9] == 'X':
        return 6
    elif grid[3] == 3 and grid[6] == 'X' and grid[9] == 'X':
        return 3
    elif grid[4] == 'X' and grid[5] == 'X' and grid[6] == 6:
        return 6
    elif grid[4] == 'X' and grid[5] == 5 and grid[6] == 'X':
        return 5
    elif grid[4] == 4 and grid[5] == 'X' and grid[6] == 'X':
        return 4
    elif grid[7] == 'X' and grid[8] == 'X' and grid[9] == 9:
        return 9
    elif grid[7] == 'X' and grid[8] == 8 and grid[9] == 'X':
        return 8
    elif grid[7] == 7 and grid[8] == 'X' and grid[9] == 'X':
        return 7
    elif grid[1] == 'X' and grid[5] == 'X' and grid[9] == 9:
         return 9
    elif grid[1] == 'X' and grid[5] == 5 and grid[9] == 'X':
        return 5
    elif grid[1] == 1 and grid[5] == 'X' and grid[9] == 'X':
        return 1
    elif grid[3] == 'X' and grid[5] == 'X' and grid[7] == 7:
        return 7
    elif grid[3] == 'X' and grid[5] == 5 and grid[7] == 'X':
        return 5
    elif grid[3] == 3 and grid[5] == 'X' and grid[7] == 'X':
        return 3
    else:
        return False

def testAIVictory(grid):
    if grid[1] == 'O' and grid[2] == 'O' and grid[3] == 3:
        return 3
    elif grid[1] == 'O' and grid[2] == 2 and grid[3] == 'O':
        return 2
    elif grid[1] == 1 and grid[2] == 'O' and grid[3] == 'O':
        return 1
    elif grid[1] == 'O' and grid[4] == 'O' and grid[7] == 7:
        return 7
    elif grid[1] == 'O' and grid[4] == 4 and grid[7] == 'O':
        return 4
    elif grid[1] == 1 and grid[4] == 'O' and grid[7] == 'O':
        return 1
    elif grid[2] == 'O' and grid[5] == 'O' and grid[8] == 8:
        return 8
    elif grid[2] == 'O' and grid[5] == 5 and grid[8] == 'O':
        return 5
    elif grid[2] == 2 and grid[5] == 'O' and grid[8] == 'O':
        return 2
    elif grid[3] == 'O' and grid[6] == 'O' and grid[9] == 9:
        return 9
    elif grid[3] == 'O' and grid[6] == 6 and grid[9] == 'O':
        return 6
    elif grid[3] == 3 and grid[6] == 'O' and grid[9] == 'O':
        return 3
    elif grid[4] == 'O' and grid[5] == 'O' and grid[6] == 6:
        return 6
    elif grid[4] == 'O' and grid[5] == 5 and grid[6] == 'O':
        return 5
    elif grid[4] == 4 and grid[5] == 'O' and grid[6] == 'O':
        return 4
    elif grid[7] == 'O' and grid[8] == 'O' and grid[9] == 9:
        return 9
    elif grid[7] == 'O' and grid[8] == 8 and grid[9] == 'O':
        return 8
    elif grid[7] == 7 and grid[8] == 'O' and grid[9] == 'O':
        return 7
    elif grid[1] == 'O' and grid[5] == 'O' and grid[9] == 9:
         return 9
    elif grid[1] == 'O' and grid[5] == 5 and grid[9] == 'O':
        return 5
    elif grid[1] == 1 and grid[5] == 'O' and grid[9] == 'O':
        return 1
    elif grid[3] == 'O' and grid[5] == 'O' and grid[7] == 7:
        return 7
    elif grid[3] == 'O' and grid[5] == 5 and grid[7] == 'O':
        return 5
    elif grid[3] == 3 and grid[5] == 'O' and grid[7] == 'O':
        return 3
    else:
        return False
cr = 0
r = 0
class Game():
    def __init__(self):
        pass
    '''Creates game grid.'''
    grid = ['0',1,2,3,4,5,6,7,8,9]
    x = len(grid)
    
    def gameGrid(grid):
        print(grid[1],'|',grid[2],'|',grid[3])
        print('-','-','-','-','-')
        print(grid[4],'|',grid[5],'|',grid[6])
        print('-','-','-','-','-')
        print(grid[7],'|',grid[8],'|',grid[9])

    def playerTurn(grid,x,data):
        try:
            '''Player selects where he wants to place "X".'''
            test2 = False
            buz = 0
            global cr
            global playerMove
            while test2 == False:
                select = int(input('Select slot: '))
                test3 = isinstance(select,int)
                if select != 0 and test3 == True and select < 10:
                    test2 = isinstance(grid[select],int)
                    if test2 == True:
                        playerMove = grid[select]
                        data.append(str(grid[select]))
                        grid[select] = 'X'
                        cr+=1
                        return True
                    elif test2 == False:
                        print('Cant select that slot.')
                        for i in range(x):
                            cantPlace = isinstance(grid[i], int)
                            if cantPlace == False:
                                buz += 1
                                if buz == 10:
                                    return False
                                else:
                                    pass
                elif select == 0:
                    print('Choose between 1-9.')
                elif select > 9:
                    print('Choose between 1-9.')
                elif test3 == False:
                    print('Tha\'\s not a number.')
                else:
                    pass

        except ValueError:
            '''Feature to skip your turn.'''
            print('Your turn was skipped.')
        except KeyboardInterrupt:
            if input('Press \'y\' to exit the Game: ') in ('y', 'Y'):
                sys.exit()
            else:
                pass
            
    '''Checks if player has won at the end of every round.'''
    def victory(grid):
        def reset(grid):
            grid [1] = 1
            grid [2] = 2
            grid [3] = 3
            grid [4] = 4
            grid [5] = 5
            grid [6] = 6
            grid [7] = 7
            grid [8] = 8
            grid [9] = 9
                    
        if grid[1] == 'X' and grid[2] == 'X' and grid[3] == 'X':
            reset(grid)
        elif grid[1] == 'X' and grid[4] == 'X' and grid[7] == 'X':
            reset(grid)
        elif grid[2] == 'X' and grid[5] == 'X' and grid[8] == 'X':
            reset(grid)
        elif grid[3] == 'X' and grid[6] == 'X' and grid[9] == 'X':
            reset(grid)
        elif grid[4] == 'X' and grid[5] == 'X' and grid[6] == 'X':
            reset(grid)
        elif grid[7] == 'X' and grid[8] == 'X' and grid[9] == 'X':
            reset(grid)
        elif grid[1] == 'X' and grid[5] == 'X' and grid[9] == 'X':
            reset(grid)
        elif grid[3] == 'X' and grid[5] == 'X' and grid[7] == 'X':
            reset(grid)
        else:
            return False
        return True


    def computerTurn(grid,x,data,testAIVictory):
        '''Computer selects where it places "O".'''
        test = False
        fuz = 0
        global cr
        global r
        winMoves = []
        block = computerBlock(grid)
        aiVictory = testAIVictory(grid)
        moves = pd.read_csv("TTT_data.csv", index_col=False)
        moveList = [moves.X0,moves.O0,moves.X1,moves.O1,moves.X2,moves.O2,moves.X3,moves.O3,moves.X4]

        movesLen = len(moveList[r])
        pComputerMoves = []
        cleanedMoves = []

        winPercent = []
        victoryCalc = []
        allMovesList = ['X0','O0','X1','O1','X2','O2','X3','O3','X4']

        for i in range(movesLen):
            if moves.iat[i,r] == playerMove and moves.iat[i,9] == 1.0 or moves.iat[i,r] == playerMove and moves.iat[i,9] == 0.5:
                winMoves.append(i)
        
        winMovesLen = len(winMoves)

        """ get computer moves from player move rows """
        for i in range(winMovesLen):
            pComputerMoves.append(moves.iat[winMoves[i],cr])

        for i in pComputerMoves:
            if i not in cleanedMoves:
                cleanedMoves.append(i)
        cleanedMovesLen = len(cleanedMoves)

        for i in range(cleanedMovesLen):
            values = moves[moves[allMovesList[cr]] == cleanedMoves[i]]
            meanOfData = values['Victory'].mean()
            
            winPercent.append([cleanedMoves[i], meanOfData])
        
        if aiVictory != False:
            if aiVictory not in winPercent:
                winPercent.append([aiVictory,1.0])
            else:
                winPercent[aiVictory][1] += 1.0

        if block != False:
            if block not in winPercent:
                winPercent.append([block,0.5])
            else:
                winPercent[block][1] += 0.5
        
        winPercentLen = len(winPercent)
        for i in range(winPercentLen):
            victoryCalc.append(winPercent[i][1])

        victoryCalc = sorted(victoryCalc, reverse=True)

        for j in range(winPercentLen):
            for i in range(winPercentLen):
                if winPercent[i][1] == victoryCalc[j]:
                    winprecentChoice = winPercent[i][0]
                    winprecentChoice = int(winprecentChoice)
                    test = isinstance(grid[int(winPercent[i][0])],int)
                    if test == True and winPercent[i] != 0:
                        data.append(str(winPercent[i][0]))
                        grid[winPercent[i][0]] = 'O'
                        r+=1
                        return True
                    
        while test == False:
            computerSelect = random.choice(grid)
            if aiVictory != False:
                computerSelect = aiVictory
                data.append(str(grid[computerSelect]))
                grid[computerSelect] = 'O'
                return True

            if block != False:
                computerSelect = block
                data.append(str(grid[computerSelect]))
                grid[computerSelect] = 'O'
                return True
            
            test = isinstance(computerSelect,int)
            if test == True and computerSelect != 0:
                data.append(str(grid[computerSelect]))
                grid[computerSelect] = 'O'
                return True
            else:
                for fuz in range(x):
                    cantPlace = isinstance(grid[fuz], int)
                    if cantPlace == False:
                        fuz += 1
                        if fuz == 10:
                            return False
                    else:
                        data.append(str(grid[fuz]))
                        grid[fuz] = 'O'
                        return True

            
    '''Checks if computer has won at the end of every round.'''
    def computerVictory(grid):
        def reset(grid):
            grid [1] = 1
            grid [2] = 2
            grid [3] = 3
            grid [4] = 4
            grid [5] = 5
            grid [6] = 6
            grid [7] = 7
            grid [8] = 8
            grid [9] = 9
                    
        if grid[1] == 'O' and grid[2] == 'O' and grid[3] == 'O':
            reset(grid)
        elif grid[1] == 'O' and grid[4] == 'O' and grid[7] == 'O':
            reset(grid)
        elif grid[2] == 'O' and grid[5] == 'O' and grid[8] == 'O':
            reset(grid)
        elif grid[3] == 'O' and grid[6] == 'O' and grid[9] == 'O':
            reset(grid)
        elif grid[4] == 'O' and grid[5] == 'O' and grid[6] == 'O':
            reset(grid)
        elif grid[7] == 'O' and grid[8] == 'O' and grid[9] == 'O':
            reset(grid)
        elif grid[1] == 'O' and grid[5] == 'O' and grid[9] == 'O':
            reset(grid)
        elif grid[3] == 'O' and grid[5] == 'O' and grid[7] == 'O':
            reset(grid)
        else:
            return False
        return True
        
    print('Welcome to play Tic-Tac-Toe. You are playing as "X" and you can choose a slot where you want to place with numbers 1-9 as shown in grid.')
    print('You can exit the game by pressing ctrl + C.')
    print('Players score is presented in left ->0-0 and computers in right 0-0<-.')
    print('Have Fun!!!')
    print('\r')
    plaPoints = 0
    coPoints = 0
    data = []
    
    while True:
        try:
            '''Set the ammount of points it is needed to win.'''
            viPoints = 1
            start = isinstance(viPoints,int)
            if start == True:
                break
            else:
                pass
        except ValueError:
            print('You have to select a number 1,2,3...')
            print('\r')
            pass
        except KeyboardInterrupt:
            if input('Press \'y\' to exit the Game: ') in ('y', 'Y'):
                sys.exit()
            else:
                pass

    while True:
        gameGrid(grid)
        if playerTurn(grid,x,data) == False:
            '''adjust data victory'''
            data.append(0.5)
            
            print('Tie.')
            grid [1] = 1
            grid [2] = 2
            grid [3] = 3
            grid [4] = 4
            grid [5] = 5
            grid [6] = 6
            grid [7] = 7
            grid [8] = 8
            grid [9] = 9
            print('Current score: '+ str(plaPoints) +'-'+ str(coPoints))
            print('player tie')
            break

        else:
            pass
        if victory(grid) == True:
            plaPoints+=1
            print('Current score: '+ str(plaPoints) +'-'+ str(coPoints))

            if plaPoints == viPoints:
                '''adjust data victory'''
                len_data = len(data)
                if len_data != 9:
                    for x in range(len_data, 9):
                        data.append(0)
                data.append('0')
                
                print('You Won!')
                break
            else:
                pass
        else:
            pass
        if computerTurn(grid,x,data,testAIVictory) == False:
            '''adjust data victory'''
            data.append(0.5)
                
            print('Tie.')
            grid [1] = 1
            grid [2] = 2
            grid [3] = 3
            grid [4] = 4
            grid [5] = 5
            grid [6] = 6
            grid [7] = 7
            grid [8] = 8
            grid [9] = 9
            print('Current score: '+ str(plaPoints) +'-'+ str(coPoints))
            print('computer tie')
            break
            
        else:
            pass
        if computerVictory(grid) == True:
            coPoints+=1
            print('Current score: '+ str(plaPoints) +'-'+ str(coPoints))

            if coPoints == viPoints:
                '''adjust data victory'''
                len_data = len(data)
                if len_data != 9:
                    for x in range(len_data, 9):
                        data.append('')
                data.append('1')
                
                print('You Lost.')
                break
            else:
                pass
        else:
            pass

    ''' write data to datasheet '''
    with open('TTT_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    print('Game Over')
