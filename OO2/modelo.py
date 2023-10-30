class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes(self):
        return self._likes
         
    def dar_like(self):
        self._likes +=1  

    @property
    def nome(self):
        return self._nome      
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    def __str__(self):
        return(f'{self._nome} - {self.ano} - {self._likes}')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return(f'{self._nome} - {self.ano} - {self.duracao} - {self._likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return(f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes}')    

class Playlist(list):
    def __init__(self, nome, programas):
        super().__init__(programas)
        self.nome = nome




vingadores = Filme('vingadores1', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)
vingadores.dar_like()
demolidor.dar_like()
demolidor.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)