def pesquisa_sequencial(lista, item):
  for i, j in enumerate(lista):
    if j == item:
      return i

pesquisa_sequencial([7, 9, 12, 15, 16, 18, 22], 15)
