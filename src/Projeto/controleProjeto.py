from Projeto.Projeto import Projeto

class controleProjetos:
  def __init__(self, controleUsuarios):
    self.listaProjetos = []
    self.controleUsuarios = controleUsuarios

  def criarProjeto(self):
    nome = input()

    descricao = input()

    idUsuario = self.controleUsuarios.buscarUsuario().id

    projeto = Projeto(nome, descricao, idUsuario)

  def listarProjetos(self):
    print("Projetos cadastrados: \n")

    for projeto in self.listaProjetos:
      print("ID do projeto: ", projeto.id)
      print("Nome do projeto: ", projeto.nome)
      print("Descrição do projeto: ", projeto.descricao)
      print("Data de criação do projeto: ", projeto.dataCriacao)
      print("ID do usuário proprietário do projeto: ", projeto.idUsuario)
      print("\n\n")

  def removerProjeto(self):
    id = int(input("Isira o ID do projeto a ser removido: "))

    for projeto in self.listaProjetos:
      if id == projeto.id:
        self.listaProjetos.remove(projeto)
        print("Projeto removido.")
        return
      
      print("Operação não realizada. Projeto não cadastrado!\n")
  
  def buscarProjeto(self):
    id = int(input("Isira o ID do projeto: "))

    for projeto in self.listaProjetos:
      if id == projeto.id:
        return projeto

      print("Operação não realizada. projeto não cadastrado!\n")
