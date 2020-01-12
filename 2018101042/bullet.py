'''
Bullet is an obstacle with the ability to move only foreward (why would anyone shoot backward, duh)
Attributes: Nothing? since it is inherited
Functions: Move front, check if it collides with anything and destroy what it collides with and destroy self too
'''
import global_stuff
from obstacle import obstacle 
class bullet(obstacle):
    def __init__(self):
        super().__init__(0, 0, 1, 2, [['≡','>']], 'Bullet')
        self.exist=0
        self.deployable=0
    
    def move_right(self,board):
        if(self.exist==1):
            try:
                board.board[self.x][self.y][0]= ' '
                board.board[self.x][self.y][1]='Normal'
                board.board[self.x][self.y+1][0]= ' '
                board.board[self.x][self.y+1][1]='Normal'
                board.board[self.x][self.y-1][0]= ' '
                board.board[self.x][self.y-1][1]='Normal'
                self.y+=2
                if(self.y+1>=board.columns):
                    self.exist=0
                else:
                    board.board[self.x][self.y][0]= '≡'
                    board.board[self.x][self.y][1]='Bullet'
                    board.board[self.x][self.y+1][0]= '>'
                    board.board[self.x][self.y+1][1]='Bullet'
                    print("BULL",self.x,self.y)
            except:
                self.exist=0
                self.deployable=0
    
    def deploy(self,hero):
        if(self.deployable==0):
            return 0
        elif(self.deployable==1):
            try:
                self.x=hero.x
                self.y=hero.y+4
                self.exist=1
                self.deployable=0
                global_stuff.bullets_left-=1 
                return 1
            except:
                return 0
    
    def display(self,board):
        if(self.exist==1):
            self.write_self_on_board(board)
    