from formula_arrasto import FormulaArrasto
from gerar_grafico import GerarGrafico

carro = FormulaArrasto(CoefArrasto=0.3, AreaFront=2.2, DensidadeAr=1.225)

grafico = GerarGrafico(carro)
grafico.gera_graf()
