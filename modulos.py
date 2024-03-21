from re import match
from os import system, name

def limpar_console():
    system('cls' if name == 'nt' else 'clear')

def pause():
  pause = input("\nPressione qualquer tecla pra continuar...")
  limpar_console()
  return

def adicionar_mascara_telefone(telefone):
  telefone = ''.join(filter(str.isdigit, telefone))
  if len(telefone) == 10:
      return '({}) {}-{}'.format(telefone[:2], telefone[2:6], telefone[6:])
  elif len(telefone) == 11:
      return '({}) {}-{}'.format(telefone[:2], telefone[2:7], telefone[7:])
  else:
      return 'Número de telefone inválido'

def valida_telefone(telefone):
  padrao_regex = '^\d{10,11}$'
  if match(padrao_regex, telefone):
      return True
  else:
      print(f"\nO Telefone {telefone} informado está fora do padrão. Padrão: DDD + Numero (somente numeros)")
      return False
  
def validar_email(email):
    padrao_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if match(padrao_regex, email):
        return True
    else:
        print(f"\nO Email {email} informado está fora do padrão.")
        return False

def adicionar_contado(contatos, nome, telefone, email):

  if valida_telefone(telefone) == False:
    return
  
  if validar_email(email) == False:  
    return
  
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"O contato {nome} foi adiocionado a sua lista.")
  return

def visualizar_contatos(contatos):
  print("\nLista de Contatos")
  if len(contatos) <= 0:
    print("\nSua lista de contatos está vazia.")
    return

  for indice, contato in enumerate(contatos, start=1):
    nome = contato["nome"]
    telefone_mascarado = adicionar_mascara_telefone(contato["telefone"])
    email = contato["email"]
    favorito = "S" if contato["favorito"] else "N"
    print(f"{indice}. [{favorito}] [{nome}] [{telefone_mascarado}] [{email}]")
  return

def identificar_indice_contato(contatos):
  visualizar_contatos(contatos)
  indice = input("Digite o numero do contato: ")
  try:
    return int(indice) - 1
  except Exception as e:
    return -2

def editar_contato(contatos, indice, tipo_edicao, nome, telefone, email):
  if indice < 0 or indice >= len(contatos):
    print(f"\nNumero do contato inválido.")
    return
  
  if tipo_edicao == "todos":
    if valida_telefone(telefone) == False:
      return
    if validar_email(email) == False:
      return
    
    contatos[indice]["nome"] = nome
    contatos[indice]["telefone"] = telefone
    contatos[indice]["email"] = email

  elif tipo_edicao == "nome":
     contatos[indice]["nome"] = nome

  elif tipo_edicao == "telefone":
     if valida_telefone(telefone) == False:
      return
     contatos[indice]["telefone"] = telefone

  elif tipo_edicao == "email":
     if validar_email(email) == False:
      return
     contatos[indice]["email"] = email
  
  print(f"\nContato {indice + 1} atualizado.")
  return

def favoritar_contato(contatos, indice, tornar_favorito):
  if indice < 0 or indice >= len(contatos):
    print(f"\nNumero do contato inválido.")
    return
  contatos[indice]["favorito"] = tornar_favorito
  favorito_ou_desfavorito = "marcado" if tornar_favorito else "desmarcado"
  print(f"\nO Contato {indice + 1} foi {favorito_ou_desfavorito} como favorito")
  return

def visualizar_contatos_favoritos(contatos):
  print("\nLista de Contatos Favoritos")
  if len(contatos) <= 0:
    print("\nSua lista de contatos está vazia.")
    return

  existe_favorito = 0
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      nome = contato["nome"]
      telefone_mascarado = adicionar_mascara_telefone(contato["telefone"])
      email = contato["email"]
      favorito = "S" if contato["favorito"] else "N"
      print(f"{indice}. [{favorito}] [{nome}] [{telefone_mascarado}] [{email}]")
      existe_favorito += 1
  
  if existe_favorito == 0:
    print("\nSua lista de contatos favoritos está vazia.")
  
  return

def apagar_contato(contatos, indice):
  if indice < 0 or indice >= len(contatos):
    print(f"\nNumero do contato inválido.")
    return
  nome = contatos[indice]["nome"]
  del contatos[indice]
  print(f"\nO contato {nome} foi apagado da lista.")
  return
