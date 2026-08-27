class controleUsuarios:
  def __init__(self):
    self.listaUsuarios = []

  def criarUsuario(self)
    nome = input("Insira o nome de usuário: ")
    
    email = input("Insira o email: ")

    senha = input("Crie sua senha: ")

    usuario = Usuario(nome, email, senha)

    self.listaUsuarios.append(usuario)

  def listarUsuarios(self)
    print("Usuários cadastrados:\n")

    for usuario in self.listaUsuarios
      print("ID: ", usuario.id)
      print("Nome: ", usuario.nome)
      print("E-mail: ", usuario.email)
      print("\n\n")

  def removerUsuario(self):
    id = int(input("Isira o ID do usuário a ser removido: "))

    for usuario in self.listaUsuarios:
      if id == self.usuario.id:
        self.listaUsuarios.remove(usuario)
        print("Usuário removido.")
        return
      
      print("Operação não realizada. Usuário não cadastrado!\n")

  def buscarUsuario(self):
    id = int(input("Isira o ID do usuário: "))

    for usuario in self.listaUsuarios:
      if id == self.usuario.id:
        return usuario

      print("Operação não realizada. Usuário não cadastrado!\n")
