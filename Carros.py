import requests

class FipeIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = []
        self.index = 0
        
        self._carregar_modelos()

    def _carregar_modelos(self):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            self.modelos = data['modelos']
        else:
            raise Exception('Falha ao carregar os modelos da marca')

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.modelos):
            modelo = self.modelos[self.index]
            self.index += 1
            return modelo
        else:
            raise StopIteration

marca_id = 3
iterator = FipeIterator(marca_id)

for modelo in iterator:
    nome = modelo['nome']
    id = modelo['codigo']
    print(f'Codigo: {id}, Nome: {nome}')