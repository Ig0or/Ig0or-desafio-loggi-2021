# Restrição 1
def tipoValido(pacote):
    tipo = int(pacote[12:15])
    if tipo != 000 and tipo != 111 and tipo != 333 and tipo != 555 and tipo != 888:
        return False
    else:
        return True


# Restrição 2
def origemJoia(pacote):
    tipo = int(pacote[12:15])
    origem = int(pacote[0:3])
    if tipo == 000 and origem == 111:
        return False
    else:
        return True


# Restrição 3
def cnpjInativo(pacote):
    vendedor = int(pacote[9:12])
    if vendedor == 584:
        return False
    else:
        return True


# Verifica se o tamanho do código de barras está correto
def tamanhoCodigo(codigo):
    if len(codigo) != 15:
        return False
    else:
        return True
