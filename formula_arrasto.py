class FormulaArrasto:
    def __init__(self, CoefArrasto, AreaFront,DensidadeAr,):
        self.CoefArrasto = CoefArrasto
        self.AreaFront = AreaFront
        self.DensidadeAr = DensidadeAr
        self.Fd = 0
        
    def CalFormula(self, VelCarro):
        self.Fd = ((0.5*self.CoefArrasto)*self.AreaFront*self.DensidadeAr*(VelCarro**2))
        return self.Fd
        

