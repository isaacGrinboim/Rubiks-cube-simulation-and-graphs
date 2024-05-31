import copy
WHITE_SIDE = 0
YELLOW_SIDE = 1
RED_SIDE = 2
ORANGE_SIDE = 3
BLUE_SIDE = 4
GREEN_SIDE = 5

colors = {0:"white",1: "yellow",2: "red", 3: "orange", 4:"blue",5: "green"}

class Cube:
    MAX_LEN = 5

    def __init__(self) -> None:

        self.UD_indexes = [GREEN_SIDE,ORANGE_SIDE,BLUE_SIDE,RED_SIDE]
        self.RL_indexes = [GREEN_SIDE,WHITE_SIDE,BLUE_SIDE,YELLOW_SIDE]
        self.FB_indexes = [ORANGE_SIDE, YELLOW_SIDE,RED_SIDE,WHITE_SIDE]
        self.make_move = {"R":self.R_rotate, "R'":self.R_prime_rotate, "L":self.L_rotate, "L'":self.L_prime_rotate, "U":self.U_rotate,"U'":self.U_prime_rotate,"D":self.D_rotate,"D'":self.D_prime_rotate,"F":self.F_rotate,"F'":self.F_prime_rotate,"B":self.B_rotate,"B'":self.B_prime_rotate}
        self.sides = [ # assuming holding down and green front
        
            [['white', 'white', 'white'],
             ['white', 'white', 'white'],
             ['white', 'white', 'white']],

            [['yellow', 'yellow', 'yellow'],
             ['yellow', 'yellow', 'yellow'],
             ['yellow', 'yellow', 'yellow']],

            [['red', 'red', 'red'],
             ['red', 'red', 'red'],
             ['red', 'red', 'red']],

            [['orange', 'orange', 'orange'],
             ['orange', 'orange', 'orange'],
             ['orange', 'orange', 'orange']],

            [['blue', 'blue', 'blue'],
             ['blue', 'blue', 'blue'],
             ['blue', 'blue', 'blue']],

            [['green', 'green', 'green'],
             ['green', 'green', 'green'],
             ['green', 'green', 'green']]
        ]

    def print_side(self, side):
        for row in self.sides[side]:
            print(row)       
#side rotation:
    def self_rotate(self, side, clockwise=True):
        temp_matrix = [row[:] for row in self.sides[side]]
        if clockwise:
            for i in range(3):
                for j in range(3):
                    self.sides[side][j][2 - i] = temp_matrix[i][j]
        else:
            for i in range(3):
                for j in range(3):
                    self.sides[side][2 - j][i] = temp_matrix[i][j]
    
    def UD_rotate(self, row, clockwise): 
        temp = self.sides[self.UD_indexes[0]][row]
        self.sides[self.UD_indexes[0]][row] = self.sides[self.UD_indexes[(1 + 2*(1- clockwise)) % 4]][row]
        self.sides[self.UD_indexes[(1 + 2*(1- clockwise)) % 4]][row] = self.sides[self.UD_indexes[2]][row]
        self.sides[self.UD_indexes[2]][row] = self.sides[self.UD_indexes[(3 + 2*(1- clockwise)) % 4]][row]
        self.sides[self.UD_indexes[(3 + 2*(1- clockwise)) % 4]][row] = temp
    def U_rotate(self):
        self.UD_rotate(0,1)
        self.self_rotate(YELLOW_SIDE, True)
    def U_prime_rotate(self):
        self.UD_rotate(0,0)
        self.self_rotate(YELLOW_SIDE, False)
    def D_rotate(self):
        self.UD_rotate(2,0)
        self.self_rotate(WHITE_SIDE, True)
    def D_prime_rotate(self):
        self.UD_rotate(2,1)
        self.self_rotate(WHITE_SIDE, False)

    def RL_rotate(self, col, clockwise):
        temp = self.sides[self.RL_indexes[0]][0][col] , self.sides[self.RL_indexes[0]][1][col] , self.sides[self.RL_indexes[0]][2][col]
        self.sides[self.RL_indexes[0]][0][col] , self.sides[self.RL_indexes[0]][1][col] , self.sides[self.RL_indexes[0]][2][col] = self.sides[self.RL_indexes[(1+2*clockwise)%4]][0][col] , self.sides[self.RL_indexes[(1+2*clockwise)%4]][1][col] , self.sides[self.RL_indexes[(1+2*clockwise)%4]][2][col]
        self.sides[self.RL_indexes[(1+2*clockwise)%4]][0][col] , self.sides[self.RL_indexes[(1+2*clockwise)%4]][1][col] , self.sides[self.RL_indexes[(1+2*clockwise)%4]][2][col] = self.sides[self.RL_indexes[2]][2-0][2-col] , self.sides[self.RL_indexes[2]][2-1][2-col] , self.sides[self.RL_indexes[2]][2-2][2-col]
        self.sides[self.RL_indexes[2]][2-0][2-col] , self.sides[self.RL_indexes[2]][2-1][2-col] , self.sides[self.RL_indexes[2]][2-2][2-col] = self.sides[self.RL_indexes[(3+2*clockwise)%4]][0][col] , self.sides[self.RL_indexes[(3+2*clockwise)%4]][1][col] , self.sides[self.RL_indexes[(3+2*clockwise)%4]][2][col]  
        self.sides[self.RL_indexes[(3+2*clockwise)%4]][0][col] , self.sides[self.RL_indexes[(3+2*clockwise)%4]][1][col] , self.sides[self.RL_indexes[(3+2*clockwise)%4]][2][col] = temp
    def R_rotate(self):
        self.RL_rotate(2,False)
        self.self_rotate(ORANGE_SIDE, True)
    def R_prime_rotate(self):
        self.RL_rotate(2,True)
        self.self_rotate(ORANGE_SIDE, False)
    def L_rotate(self):
        self.RL_rotate(0,True)
        self.self_rotate(RED_SIDE, True)
    def L_prime_rotate(self):
        self.RL_rotate(0,False)
        self.self_rotate(RED_SIDE, False)

    def FB_rotate_clockwise(self, col):
                temp = self.sides[self.FB_indexes[0]][0][col] , self.sides[self.FB_indexes[0]][1][col] , self.sides[self.FB_indexes[0]][2][col]
                self.sides[self.FB_indexes[0]][0][col] , self.sides[self.FB_indexes[0]][1][col] , self.sides[self.FB_indexes[0]][2][col] = self.sides[self.FB_indexes[1]][2-col][0] , self.sides[self.FB_indexes[1]][2-col][1] , self.sides[self.FB_indexes[1]][2-col][2]
                self.sides[self.FB_indexes[1]][2-col][0] , self.sides[self.FB_indexes[1]][2-col][1] , self.sides[self.FB_indexes[1]][2-col][2] = self.sides[self.FB_indexes[2]][2][2-col] , self.sides[self.FB_indexes[2]][1][2-col] , self.sides[self.FB_indexes[2]][0][2-col]
                self.sides[self.FB_indexes[2]][2][2-col] , self.sides[self.FB_indexes[2]][1][2-col] , self.sides[self.FB_indexes[2]][0][2-col] = self.sides[self.FB_indexes[3]][col][2] , self.sides[self.FB_indexes[3]][col][1] , self.sides[self.FB_indexes[3]][col][0]
                self.sides[self.FB_indexes[3]][col][2] , self.sides[self.FB_indexes[3]][col][1] , self.sides[self.FB_indexes[3]][col][0] = temp     
    def F_rotate(self):
        self.FB_rotate_clockwise(0)
        self.self_rotate(GREEN_SIDE,True)
    def B_prime_rotate(self):
        self.FB_rotate_clockwise(2)
        self.self_rotate(BLUE_SIDE,False)
    def FB_rotate_counter_clockwise(self, col):
        temp = self.sides[self.FB_indexes[0]][0][col] , self.sides[self.FB_indexes[0]][1][col] , self.sides[self.FB_indexes[0]][2][col]
        self.sides[self.FB_indexes[0]][0][col] , self.sides[self.FB_indexes[0]][1][col] , self.sides[self.FB_indexes[0]][2][col] = self.sides[self.FB_indexes[3]][col][2] , self.sides[self.FB_indexes[3]][col][1] , self.sides[self.FB_indexes[3]][col][0]
        self.sides[self.FB_indexes[3]][col][2] , self.sides[self.FB_indexes[3]][col][1] , self.sides[self.FB_indexes[3]][col][0] = self.sides[self.FB_indexes[2]][2][2-col] , self.sides[self.FB_indexes[2]][1][2-col] , self.sides[self.FB_indexes[2]][0][2-col] 
        self.sides[self.FB_indexes[2]][2][2-col] , self.sides[self.FB_indexes[2]][1][2-col] , self.sides[self.FB_indexes[2]][0][2-col] = self.sides[self.FB_indexes[1]][2-col][0] , self.sides[self.FB_indexes[1]][2-col][1] , self.sides[self.FB_indexes[1]][2-col][2]
        self.sides[self.FB_indexes[1]][2-col][0] , self.sides[self.FB_indexes[1]][2-col][1] , self.sides[self.FB_indexes[1]][2-col][2] = temp        
    def B_rotate(self):
        self.FB_rotate_counter_clockwise(2)
        self.self_rotate(BLUE_SIDE, True)
    def F_prime_rotate(self):
        self.FB_rotate_counter_clockwise(0)
        self.self_rotate(GREEN_SIDE, False)

    def clone(self) -> 'Cube' :
        return copy.deepcopy(self)        
    def get_legal_moves(self)->list:
        return ["R","R'","L","L'","U","U'","D","D'","F","F'","B","B'"]
    
    def set_cube_sides(self, sides): #totally assumes that scramble is legal
        self.sides = copy.deepcopy(sides) 

    def scrumble(self, moves: list):
        for move in moves:
            self.make_move[move]()
                        
    def not_in_place(self) -> int:
        not_in_place = 0
        for i, side in enumerate(self.sides):
            for row in side:
                for color in row:
                    not_in_place += (color != colors[i])
        return not_in_place
                        
    def solved(self) -> bool:
        return self.not_in_place() == 0

    def h_val(self) -> float:
        return self.not_in_place()/(6*9)












# cube = Cube()
# for i in range(1):
#     cube.R_rotate()
#     cube.U_rotate()
#     cube.L_rotate()
#     cube.D_rotate()

# cube.F_rotate()
# cube.R_prime_rotate()
# cube.R_prime_rotate()
# cube.B_prime_rotate()
# cube.R_prime_rotate()
# cube.R_prime_rotate()
# cube.F_prime_rotate()
# moves = ["R","U","L","D"]
# cube.scrumble(moves)


# cube.print_side(GREEN_SIDE)
# print(cube.solved())
