class Usuario:
  id = 1

  def __init__(self, nome, email, senha):
    self.id = Usuario.id

    self.nome = nome
    
    self.email = email
    
    self.senha = senha
    
    Usuario.id +=1
