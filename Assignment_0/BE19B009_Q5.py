class MMEqaution:
    def __init__(self, V_max, K_m):
        self._V_max = V_max
        self._K_m = K_m

    def get_rection_rate(self, S):
       v = self._V_max*((S)/(self._K_m + S))
       return v

eq = MMEqaution(4, 10)
rate =  eq.get_rection_rate(200)
print("For V_max = {0}, K_m = {1} & [S] = 200 ==> V = {2}".format(eq._V_max, eq._K_m, rate))
