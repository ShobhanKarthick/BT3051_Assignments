from matplotlib.pyplot import matshow, imsave

class Simulate_Conways_Game_of_Life():
    def __init__(self, MyMatrix):
        self.matrix = MyMatrix
        """ Add your code here """
    
    def value(self, i, j, Matrix):
        try:
            return Matrix[i][j]
        except:
            return 0

    def neighboursNum(self, i, j, Matrix):
        neighborCells = ([
            self.value(i-1, j-1, Matrix), 
            self.value(i-1, j  , Matrix), 
            self.value(i-1, j+1, Matrix), 
            self.value(i  , j-1, Matrix), 
            self.value(i  , j+1, Matrix), 
            self.value(i+1, j-1, Matrix), 
            self.value(i+1, j  , Matrix), 
            self.value(i+1, j+1, Matrix) 
            ])
        count = neighborCells.count(1)
        return count
    
    """ Add your functions here """
    def population(self, i, j, matrix):
        numOfNeighbours = self.neighboursNum(i, j, matrix)
        if matrix[i][j] and not (2 <= numOfNeighbours <= 3):
            return 0
        elif numOfNeighbours == 3:
            return 1
        return matrix[i][j]  

    def simulate_one_step(self):
        newMatrix = [[0 for i in range(100)] for j in range(100)]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                newMatrix[i][j] = self.population(i, j, self.matrix)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = newMatrix[i][j]


    def final_output(self):
        """
        Return the output of the 39th step 
        """
        for i in range(39):
            self.simulate_one_step()
        return self.matrix 


Glider = [[0 for i in range(100)] for j in range(100)]
Glider[1][2] = 1
Glider[2][3] = 1
Glider[3][1:4] = [1,1,1]

# 0 - Dead cell, 1 - Live cell
Game1 = Simulate_Conways_Game_of_Life(Glider)
Step_39 = Game1.final_output()

from matplotlib.pyplot import matshow

imsave("im" +".png", Step_39)
matshow(Step_39)
