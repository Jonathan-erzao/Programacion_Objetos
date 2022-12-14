from payment import Payment

class PaymentTransferencia(Payment):
    cuenta: int
    banco : str
    
    def __init__(self, id, valor, fecha, cuenta, banco):
        super().__init__(id, valor, fecha)
        self.cuenta = cuenta
        self.banco = banco 