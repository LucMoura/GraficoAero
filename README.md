# Simulador de Arrasto Aerodinâmico

Este projeto simula a força de arrasto aerodinâmico em função da velocidade de um veículo. Ele utiliza a equação do arrasto para calcular a força resistiva do ar e exibe os resultados em um gráfico.

## 📌 Funcionalidades

- Cálculo da força de arrasto aerodinâmico com base no coeficiente de arrasto, área frontal e densidade do ar.
- Geração de gráficos que mostram a variação da força de arrasto em função da velocidade do veículo.

## 🛠️ Tecnologias Utilizadas

- Python
- NumPy
- Matplotlib

## 📥 Instalação

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install numpy matplotlib
   ```

## 🚀 Como Usar

1. Execute o script principal:
   ```bash
   python main.py
   ```
2. O programa irá calcular a força de arrasto e exibir um gráfico.

## 📜 Código

### Exemplo de Uso

```python
from formula_arrasto import FormulaArrasto
from gerar_grafico import GerarGrafico

carro = FormulaArrasto(CoefArrasto=0.3, AreaFront=2.2, DensidadeAr=1.225)

grafico = GerarGrafico(carro)
grafico.gera_graf()
```

### Implementação

#### `formula_arrasto.py`

```python
class FormulaArrasto:
    def __init__(self, CoefArrasto, AreaFront, DensidadeAr):
        self.CoefArrasto = CoefArrasto
        self.AreaFront = AreaFront
        self.DensidadeAr = DensidadeAr
        self.Fd = 0
    
    def CalFormula(self, VelCarro):
        self.Fd = (0.5 * self.CoefArrasto * self.AreaFront * self.DensidadeAr * (VelCarro ** 2))
        return self.Fd
```

#### `gerar_grafico.py`

```python
import numpy as np
import matplotlib.pyplot as plt
from formula_arrasto import FormulaArrasto

class GerarGrafico:
    def __init__(self, formula_arrasto):
        self.formula_arrasto = formula_arrasto
    
    def gera_graf(self):
        velocidades = np.linspace(0, 100, 50)
        forcas_arrasto = [self.formula_arrasto.CalFormula(v) for v in velocidades]
        
        plt.figure(figsize=(8,5))
        plt.plot(velocidades, forcas_arrasto, label="Força de Arrasto", color="red")
        plt.xlabel("Velocidade (m/s)")
        plt.ylabel("Força de Arrasto (N)")
        plt.title("Força de Arrasto em Função da Velocidade")
        plt.legend()
        plt.grid()
        plt.show()
```

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar conforme necessário.

---


