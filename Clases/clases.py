class Car():
    """Modelo de Carro"""
    def __init__(self,marca,modelo,año):
        """Inicializando Attributos"""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        """Capacidad y nivel de combustible en Galones"""
        self.capacidad = 15
        self.nivel = 0

        def llenar_tanque():
            """LLnear el tanke de gas a su capacidad"""
            self.nivel = self.capacidad
            print('El tanque esta lleno')