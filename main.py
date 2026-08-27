from src.Usuario.Usuario import controleUsuarios
from src.Projeto.Projeto import controleProjetos

controleUsuarios = controleUsuarios()
controleProjetos = controleProjetos(controleUsuarios)

print("Menu\n1 - Criar Usuário\n2 - Listar Usuários\n3 - Remover Usuário\n4 - Buscar Usuário\n5 - Criar Projeto\n6 - Listar Projetos\n7 - Remover Projeto\n8 - Buscar Projeto\n9 - Sair")

opMenu = 0

while(opMenu != 9):
  opMenu = int(input("Insira a opção desejada: "))

  match opMenu:
    case 1:
      controleUsuarios.criarUsuario()
    case 2:
      controleUsuarios.listarUsuarios()
    case 3:
      controleUsuarios.removerUsuario()
    case 4:
      controleUsuarios.buscarUsuario()
    case 5:
      controleProjetos.criarProjeto()
    case 6:
      controleProjetos.listarProjetos()
    case 7:
      controleProjetos.removerProjeto()
    case 8:
      controleProjetos.buscarProjeto()
    case 9:
      print("Programa finalizado!")
    case _:
      print("Opção inválida!")
