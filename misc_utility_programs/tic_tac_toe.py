#### function to show the board #####

import random
def show_bord(bord):
    for i in bord:
        for j in i:
            print(j,end=" ")
        print()

#### Start of function to find winner #####
def find_winner(bord,player):
    ##if rows are winner
    for i in range(0,len(bord)):
        count=0
        for j in range(0,len(bord)):
            if bord[i][j]==player:
                win=True
                count+=1
            else:
                win=False
        # print(win, count) #debug line
        if win==True and count==3: return True
            
##if cols are winner
    for i in range(0,len(bord)):
        count=0
        for j in range(0,len(bord)):
            if bord[j][i]==player:
                win=True
                count+=1
            else:
                win=False
        if win==True and count==3: return True

##if 1st daigonal are winner
    count=0
    for i in range(0,len(bord)):
        for j in range(0,len(bord)):
            if i==j:
                if bord[i][j]==player:
                    win=True
                    count+=1
                else:
                    win=False
        if win==True and count==3: return True
    
    #print("inside winnner fun")        
##if 2nd daigonal is winner
    count,i,j=0, 0, 2
    while i <3 and j <3:
        if bord[i][j]==player:
            win=True
            count+=1
        i +=1
        j -=1
    if win==True and count==3: return True 

#### end of function winner #####



##### main section of the program #####    

board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]

board_pos = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

player_human = 'x'
player_computer = 'o'
total_hand=0

player_x_track=[]
winner_x=False

player_o_track=[]
winner_o=False
print("Human(x) is starting the game")
while True:
    row_indx, col_indx = input("Enter row & column index: ").split()
    
    row_indx=int(row_indx)
    col_indx=int(col_indx)

    if board[row_indx][col_indx] == '-':
        board[row_indx][col_indx]='x'
        total_hand +=1
        player_x_track.append([row_indx,col_indx])
        board_pos.remove([row_indx,col_indx])
        show_bord(board)

    if total_hand>=5:
        winner_x=find_winner(board,'x')

    if winner_x==True:
        print("Human is winner")
        break

    possible_move=random.choice(board_pos) ## function to get the computer hand row & column index
    new_row=possible_move[0]
    new_col=possible_move[1]
    print("Machines next move ",new_row," ",new_col)

    if board[new_row][new_col] == '-':
        board[new_row][new_col]='0'
        total_hand +=1
        show_bord(board)
        player_o_track.append([new_row,new_col])
        board_pos.remove([new_row,new_col])

    #print("total hand",total_hand)
    
    if total_hand>=5:
        winner_o=find_winner(board,'0')

    if winner_o==True:
        print("Machine is winner")
        break

    if total_hand==9:
        print("No winner")
        break
