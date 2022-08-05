class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 32
        self.marca = "Samsung"


tv1 = Televisao()
tv1.tamanho = 43
tv1.marca = "LG"
tv2 = Televisao()
tv2.tamanho = 65
tv2.marca = "Sony"

print(f"tv_quarto tamanho={tv1.tamanho} marca={tv1.marca}")
print(f"tv_sala tamanho={tv2.tamanho} marca={tv2.marca}")