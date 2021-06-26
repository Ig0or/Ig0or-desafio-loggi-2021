from restricoes import tipoValido, origemJoia, cnpjInativo, tamanhoCodigo


class Pacote:
    def __init__(self, pacotes):
        self.listaPacotes = pacotes

    # A) Identifica o destino de cada pacote
    def verificarDestino(self):
        numeroPacote = 1
        for pacote in self.listaPacotes:
            self.destino = int(pacote[3:6])
            if self.destino == 111:
                print(f"A região de destino do Pacote {numeroPacote} é: Centro-Oeste.")
            elif self.destino == 333:
                print(f"A região de destino do Pacote {numeroPacote} é: Nordeste.")
            elif self.destino == 555:
                print(f"A região de destino do Pacote {numeroPacote} é: Norte.")
            elif self.destino == 888:
                print(f"A região de destino do Pacote {numeroPacote} é: Sudeste.")
            elif self.destino == 000:
                print(f"A região de destino do Pacote {numeroPacote} é: Sul.")
            else:
                print(f"A região de destino do Pacote {numeroPacote} é inválida.")
            numeroPacote += 1
        print("-" * 30)

    # B) Verifica se o pacote tem código de barras válido
    def codigoValido(self):
        numeroPacote = 1
        self.pacotesValido = []
        for pacote in self.listaPacotes:
            if (
                tamanhoCodigo(pacote)
                and tipoValido(pacote)
                and origemJoia(pacote)
                and cnpjInativo(pacote)
            ):
                print(f"O Pacote {numeroPacote} está com código de barras válido.")
                self.pacotesValido.append(pacote)
            else:
                print(f"O Pacote {numeroPacote} está com código de barras inválido.")
            numeroPacote += 1
        print("-" * 30)

    # C) Identifica se o pacote tem como origem a região sul e tipo de produto brinquedos
    def brinquedosSul(self):
        numeroPacote = 1
        qtd = 0
        for pacote in self.listaPacotes:
            self.origem = int(pacote[0:3])
            self.tipo = int(pacote[12:15])
            if self.origem == 000 and self.tipo == 888:
                qtd += 1
                print(
                    f"Pacote {numeroPacote} que tem como origem a região Sul possui brinquedos em seu conteúdo."
                )
            numeroPacote += 1
        if qtd >= 1:
            print("-" * 30)

    # D) lista os pacotes agrupados por região de destino (pacotes válidos)
    def regiaoAgrupados(self):
        self.centroOeste = []
        self.nordeste = []
        self.norte = []
        self.sudeste = []
        self.sul = []
        for pacote in self.pacotesValido:
            self.destino = int(pacote[3:6])
            if self.destino == 111:
                self.centroOeste.append(pacote)
            elif self.destino == 333:
                self.nordeste.append(pacote)
            elif self.destino == 555:
                self.norte.append(pacote)
            elif self.destino == 888:
                self.sudeste.append(pacote)
            elif self.destino == 000:
                self.sul.append(pacote)
        print(f"Pacotes com região de destino Centro-Oeste:")
        for pacote in self.centroOeste:
            print(pacote)
        print(f"Pacotes com região de destino Nordeste:")
        for pacote in self.nordeste:
            print(pacote)
        print(f"Pacotes com região de destino Norte:")
        for pacote in self.norte:
            print(pacote)
        print(f"Pacotes com região de destino Sudeste:")
        for pacote in self.sudeste:
            print(pacote)
        print(f"Pacotes com região de destino Sul:")
        for pacote in self.sul:
            print(pacote)
        print("-" * 30)

    # E) Lista o número de pacotes enviados por cada vendedor (pacotes válidos)
    def enviadosVendedor(self):
        vendedores = []
        for pacote in self.pacotesValido:
            self.vendedor = int(pacote[9:12])
            vendedores.append(self.vendedor)

        listaVendedores = []
        contagem = []
        for vendedor in vendedores:
            if listaVendedores.count(vendedor) == 0:
                listaVendedores.append(vendedor)
                contagem.append(vendedores.count(vendedor))

        index = 0
        for vendedor in listaVendedores:
            print(f"O vendedor {vendedor} enviou {contagem[index]} pacotes.")
            index += 1
        print("-" * 30)

    # F) Relatório de pacotes por destino e por tipo (pacotes válidos)
    def pacotesDestinoTipo(self):
        for pacote in self.centroOeste:
            joias = []
            livros = []
            eletronicos = []
            bebidas = []
            brinquedos = []
            self.tipo = int(pacote[12:15])
            if self.tipo == 000:
                joias.append(pacote)
            elif self.tipo == 111:
                livros.append(pacote)
            elif self.tipo == 333:
                eletronicos.append(pacote)
            elif self.tipo == 555:
                bebidas.append(pacote)
            elif self.tipo == 888:
                brinquedos.append(pacote)
        if joias:
            print(f"Pacotes contendo jóias com região de destino Centro-Oeste:")
            for pacote in joias:
                print(pacote)
        if livros:
            print(f"Pacotes contendo livros com região de destino Centro-Oeste:")
            for pacote in livros:
                print(pacote)
        if eletronicos:
            print(f"Pacotes contendo eletrônicos com região de destino Centro-Oeste:")
            for pacote in eletronicos:
                print(pacote)
        if bebidas:
            print(f"Pacotes contendo bebidas com região de destino Centro-Oeste:")
            for pacote in bebidas:
                print(pacote)
        if brinquedos:
            print(f"Pacotes contendo brinquedos com região de destino Centro-Oeste:")
            for pacote in brinquedos:
                print(pacote)

        for pacote in self.nordeste:
            joias = []
            livros = []
            eletronicos = []
            bebidas = []
            brinquedos = []
            self.tipo = int(pacote[12:15])
            if self.tipo == 000:
                joias.append(pacote)
            elif self.tipo == 111:
                livros.append(pacote)
            elif self.tipo == 333:
                eletronicos.append(pacote)
            elif self.tipo == 555:
                bebidas.append(pacote)
            elif self.tipo == 888:
                brinquedos.append(pacote)
        if joias:
            print(f"Pacotes contendo jóias com região de destino Nordeste:")
            for pacote in joias:
                print(pacote)
        if livros:
            print(f"Pacotes contendo livros com região de destino Nordeste:")
            for pacote in livros:
                print(pacote)
        if eletronicos:
            print(f"Pacotes contendo eletrônicos com região de destino Nordeste:")
            for pacote in eletronicos:
                print(pacote)
        if bebidas:
            print(f"Pacotes contendo bebidas com região de destino Nordeste:")
            for pacote in bebidas:
                print(pacote)
        if brinquedos:
            print(f"Pacotes contendo brinquedos com região de destino Nordeste:")
            for pacote in brinquedos:
                print(pacote)

        for pacote in self.norte:
            joias = []
            livros = []
            eletronicos = []
            bebidas = []
            brinquedos = []
            self.tipo = int(pacote[12:15])
            if self.tipo == 000:
                joias.append(pacote)
            elif self.tipo == 111:
                livros.append(pacote)
            elif self.tipo == 333:
                eletronicos.append(pacote)
            elif self.tipo == 555:
                bebidas.append(pacote)
            elif self.tipo == 888:
                brinquedos.append(pacote)
        if joias:
            print(f"Pacotes contendo jóias com região de destino Norte:")
            for pacote in joias:
                print(pacote)
        if livros:
            print(f"Pacotes contendo livros com região de destino Norte:")
            for pacote in livros:
                print(pacote)
        if eletronicos:
            print(f"Pacotes contendo eletrônicos com região de destino Norte:")
            for pacote in eletronicos:
                print(pacote)
        if bebidas:
            print(f"Pacotes contendo bebidas com região de destino Norte:")
            for pacote in bebidas:
                print(pacote)
        if brinquedos:
            print(f"Pacotes contendo brinquedos com região de destino Norte:")
            for pacote in brinquedos:
                print(pacote)

        for pacote in self.sudeste:
            joias = []
            livros = []
            eletronicos = []
            bebidas = []
            brinquedos = []
            self.tipo = int(pacote[12:15])
            if self.tipo == 000:
                joias.append(pacote)
            elif self.tipo == 111:
                livros.append(pacote)
            elif self.tipo == 333:
                eletronicos.append(pacote)
            elif self.tipo == 555:
                bebidas.append(pacote)
            elif self.tipo == 888:
                brinquedos.append(pacote)
        if joias:
            print(f"Pacotes contendo jóias com região de destino Sudeste:")
            for pacote in joias:
                print(pacote)
        if livros:
            print(f"Pacotes contendo livros com região de destino Sudeste:")
            for pacote in livros:
                print(pacote)
        if eletronicos:
            print(f"Pacotes contendo eletrônicos com região de destino Sudeste:")
            for pacote in eletronicos:
                print(pacote)
        if bebidas:
            print(f"Pacotes contendo bebidas com região de destino Sudeste:")
            for pacote in bebidas:
                print(pacote)
        if brinquedos:
            print(f"Pacotes contendo brinquedos com região de destino Sudeste:")
            for pacote in brinquedos:
                print(pacote)

        for pacote in self.sul:
            joias = []
            livros = []
            eletronicos = []
            bebidas = []
            brinquedos = []
            self.tipo = int(pacote[12:15])
            if self.tipo == 000:
                joias.append(pacote)
            elif self.tipo == 111:
                livros.append(pacote)
            elif self.tipo == 333:
                eletronicos.append(pacote)
            elif self.tipo == 555:
                bebidas.append(pacote)
            elif self.tipo == 888:
                brinquedos.append(pacote)
        if joias:
            print(f"Pacotes contendo jóias com região de destino Sul:")
            for pacote in joias:
                print(pacote)
        if livros:
            print(f"Pacotes contendo livros com região de destino Sul:")
            for pacote in livros:
                print(pacote)
        if eletronicos:
            print(f"Pacotes contendo eletrônicos com região de destino Sul:")
            for pacote in eletronicos:
                print(pacote)
        if bebidas:
            print(f"Pacotes contendo bebidas com região de destino Sul:")
            for pacote in bebidas:
                print(pacote)
        if brinquedos:
            print(f"Pacotes contendo brinquedos com região de destino Sul:")
            for pacote in brinquedos:
                print(pacote)
        print("-" * 30)

    def iniciar(self):
        self.verificarDestino()
        self.codigoValido()
        self.brinquedosSul()
        self.regiaoAgrupados()
        self.enviadosVendedor()
        self.pacotesDestinoTipo()
