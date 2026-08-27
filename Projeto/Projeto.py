from datetime import datetime

class Projeto:
  id = 1

  def __init__(self, nome, descricao, idUsuario):
    self.id = Projeto.id

    self.nome = nome
    
    self.descricao = descricao
    
    self.dataCriacao = datetime.now()

    self.idUsuario = idUsuario
    
    Projeto.id +=1
