import modulos

contatos = []
modulos.limpar_console()
MENSAGEM_TELEFONE = "Telefone - Padrão: DDD + Numero (somente numeros): "

while True:
  print("\nMenu do Gestor de Contatos")
  print("1. Adicionar Contato")
  print("2. Visualizar Contatos")
  print("3. Editar Contato - Todos os Dados")
  print("4. Editar Contato - Nome")
  print("5. Editar Contato - Telefone")
  print("6. Editar Contato - Email")
  print("7. Favoritar Contato")
  print("8. Desfavoritar Contato")
  print("9. Visualizar Lista de Contatos Favoritos")
  print("10. Apagar Contato")
  print("11. Sair")
  
  opcao = input("\nDigite a opção desejada: ")
  
  try:
    escolha = int(opcao)
  except ValueError as e:
    print("\nValor informado inválido. Informe somente números.")
    escolha = 0
  except Exception as e:
    print("\nErro:", e)
    escolha = 0

  if escolha == 0:
    modulos.pause()
  
  elif escolha == 1:
    print("Informe os dados do contato:")
    nome = input("Nome: ")
    telefone = input(MENSAGEM_TELEFONE)
    email = input("Email: ")
    modulos.adicionar_contado(contatos, nome, telefone, email)
    modulos.pause()

  elif escolha == 2:
    modulos.visualizar_contatos(contatos)
    modulos.pause()

  elif escolha == 3:
    indice = modulos.identificar_indice_contato(contatos)
    print("Informe os novos dados:")
    nome = input("Nome: ")
    telefone = input(MENSAGEM_TELEFONE)
    email = input("Email: ")
    modulos.editar_contato(contatos, indice, "todos", nome, telefone, email)
    modulos.pause()
  
  elif escolha == 4:
    indice = modulos.identificar_indice_contato(contatos)
    nome = input("Informe o novo Nome: ")
    modulos.editar_contato(contatos, indice, "nome", nome, '', '')
    modulos.pause()
  
  elif escolha == 5:
    indice = modulos.identificar_indice_contato(contatos)
    telefone = input(f"Informe o novo {MENSAGEM_TELEFONE}")
    modulos.editar_contato(contatos, indice, "telefone", '', telefone, '')
    modulos.pause()

  elif escolha == 6:
    indice = modulos.identificar_indice_contato(contatos)
    email = input("Informe o novo Email: ")
    modulos.editar_contato(contatos, indice, "email", '', '', email)
    modulos.pause()

  elif escolha == 7:
    indice = modulos.identificar_indice_contato(contatos)
    modulos.favoritar_contato(contatos, indice, True)
    modulos.pause()

  elif escolha == 8:
    indice = modulos.identificar_indice_contato(contatos)
    modulos.favoritar_contato(contatos, indice, False)
    modulos.pause()

  elif escolha == 9:
    modulos.visualizar_contatos_favoritos(contatos)
    modulos.pause()

  elif escolha == 10:
    indice = modulos.identificar_indice_contato(contatos)
    modulos.apagar_contato(contatos, indice)
    modulos.pause()
    
  elif escolha == 11:
    break
  else:
    print("\nOpção informada inálida.")
    modulos.pause()
    

print("\nGestor de Contatos Finalizado")