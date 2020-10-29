class Client:
    def __init__(self, name, id, credit, address):
        self.name = name
        self.id = id
        self.credit = credit
        self.address = address

def run():
    cliente = Client("Grecia Corona", "00510", "543534598", "Av. San Jerónimo 2242, Col. Pueblo Nuevo Alto")
    print(f"Name: {cliente.name}")
    print(f"ID: {cliente.id}")
    print(f"Credit: {cliente.credit}")
    print(f"Address: {cliente.address}")
    
if __name__ == "__main__":
    run()