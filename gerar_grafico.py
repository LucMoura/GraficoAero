import numpy as np
import matplotlib.pyplot as plt
from formula_arrasto import FormulaArrasto

class GerarGrafico:
    def __init__(self, formula_arrasto):
        self.formula_arrasto = formula_arrasto
    
    def gera_graf(self):
        velocidades = np.linspace(0,100,50)
        forcas_arrasto = [self.formula_arrasto.CalFormula(v) for v in velocidades]
        
        plt.figure(figsize=(8,5))
        plt.plot(velocidades, forcas_arrasto, label="Força de Arrasto", color = "red")
        plt.xlabel("Velocidade (m/s)")
        plt.ylabel("Força de Arrasto (N)")
        plt.title("Força de Arrasto em Função de Velocidade")
        plt.legend()
        plt.grid()
        plt.show()
        
    