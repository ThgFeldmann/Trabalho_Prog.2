from datetime import datetime

#* Classe para Livros
class Livro:
    def __init__(self, titulo, codigo, editora, categoria, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
    
    def Info(self): # Método para informar *todos* os livros

        self.valor = float(self.valor)
        self.estoque = int(self.estoque)

        # Calculo para o valor total em estoque
        valor_estoque = self.valor * self.estoque

        print(f"\n>>>>>>Cod#{self.codigo}")
        print(f"Titulo/Editora: {self.titulo}/{self.editora}")
        print(f"Categoria: {self.categoria}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor}")
        print(f"Estoque: {self.estoque:.2f} unidade(s)")
        print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
    
    def Info_Diferencas(self, lista_diferencas):
        valor_estoque = 0
        
        for diferenca in lista_diferencas:
            valor = diferenca[0]
            estoque = diferenca [2]
            
            valor_estoque += valor * estoque
        
        print(f"\n>>>>>>Cod#{self.codigo}")
        print(f"Titulo/Editora: {self.titulo}/{self.editora}")
        print(f"Categoria: {self.categoria}")
        print(f"Ano: {self.ano}")
        
        for diferenca in lista_diferencas:
            print(f"Valor: R$ {diferenca[0]:.2f} >>> Filial {diferenca[1]}: estoque: {diferenca[2]} unidades")

        print(f"Valor total em estoque: R$ {valor_estoque:.2f}")

#* Classe para Filiais
class Filial(Livro):
    def __init__(self, codigo, nome, endereco, telefone):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.livros = []
        
    def Info(self):
        print(f"\n{self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Quantidade de Livros: {len(self.livros)}")
    
    def Info_Livros(self):
        print(f"\nLivros na Filial: {self.codigo}")
        for livro in self.livros:
            livro.Info()
    
    def Retornar_Livro_por_Codigo(self, codigo_inserido):
        for livro in self.livros:
            if livro.codigo == codigo_inserido:
                return livro
    
    def Info_Livro_por_Nome(self, titulo_inserido):
        for livro in self.livros:
            if livro.titulo.upper() == titulo_inserido:
                livro.Info()
    
    def Info_Livro_por_Categoria(self, categoria_inserido):
        for livro in self.livros:
            if livro.categoria.upper() == categoria_inserido:
                livro.Info()
    
    def Info_Livro_por_Valor(self, valor_inserido):
        for livro in self.livros:
            if livro.valor == valor_inserido:
                livro.Info()
    
    def Info_Livro_por_Estoque(self, estoque_inserido):
        for livro in self.livros:
            if livro.estoque == estoque_inserido:
                livro.Info()
    
    def Adicionar_Livro(self, livro):
        self.livros.append(livro)
    
    def Listar_Livros_Da_Filial(self):
        for livro in self.livros:
            livro.Info()
    
    def Calcular_Valor_Total_de_Livros(self):
        valor_total = 0
        
        for livro in self.livros:
            valor_total += livro.valor * livro.estoque
        
        print(f"\nValor total no estoque da Filial: R$ {valor_total:.2f}")
    
    def Retornar_Valor_Total_de_Livros(self):
        valor_total = 0
        
        for livro in self.livros:
            valor_total += livro.valor * livro.estoque
        
        return valor_total

#* Funções

# Função para verificar se a Filial existe no arquivo de estoque
def Verificar_Filial(codigo_filial_inserido):
    codigo_foi_aceito = False
    
    # Abrindo o arquivo para a leitura
    with open("estoque_filiais.txt", "r", encoding="utf-8") as arquivo:
        
        # Leitura do arquivo linha-por-linha
        for linha in arquivo:
            
            # Caso a linha atual seja uma Filial
            if linha[0] == "#":
                # Normalize a linha
                filial = linha.strip().replace("\n", "").split(",")
                # Separe o código da Filial
                codigo_filial = filial[0].replace("#FL", "")
                
                # Verifique se o código inserido pelo usuário, está presente no arquivo
                if codigo_filial == codigo_filial_inserido:
                    codigo_foi_aceito = True
                    return codigo_foi_aceito
    
    if codigo_foi_aceito == False:
        return codigo_foi_aceito

def Entrada_do_Codigo_Filial():
    recebendo_valores = True

    # Normalizando o código da Filial
    while recebendo_valores: # Código da Filial
        print("\nDigite o código da Filial")
        print("Digite apenas o número do código")
        
        try:
            codigo_inserido = input(": ")
            
            if codigo_inserido != "":
                # Verificando se a Filial existe no arquivo
                codigo_validado = Verificar_Filial(codigo_inserido)
                
                if codigo_validado:
                    codigo_atual = codigo_inserido
                    
                    try:
                        codigo_inserido = str(int(codigo_inserido))
                        codigo_inserido = "0" + str(codigo_inserido)
                        
                        if codigo_atual[0] == "0" and codigo_inserido[0] != "0":
                            codigo_inserido = "0" + str(codigo_inserido)

                        codigo_inserido = "#FL" + codigo_inserido
                        recebendo_valores = False
                        
                        #* Retornando o código da Filial, validado e normalizado
                        return codigo_inserido
                    
                    except ValueError:
                        print("\nCódigo inválido. Digite apenas números inteiros.")
                        Continuar()
                        continue
                    except Exception as error:
                        print("\nOcorreu um erro inesperado, tente novamente.")
                        print(f"Erro: {error}")
                        Continuar()
                        continue
                else:
                    print("\nNão foi encontrado nenhuma Filial com este código.")
                    Continuar()
                    continue
            else:
                raise ValueError
        except ValueError:
            print("\nCódigo inválido. Insira algum valor e tente novamente")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            Continuar()
            continue

# Função para a escolha do cadastro
def Escolher_Cadastro(lista_filiais):
    running = True

    while running:
        print("O que deseja cadastrar:\n")
        print("1 - Livro")
        print("2 - Filial")
        print("0 - Sair")

        try:
            escolha = int(input(": "))
        except ValueError:
            print("-"*30)
            print("Entrada inválida. Utilize números inteiros.")
            Continuar()
            continue
        except Exception as error: #* Em caso de erros inesperados
            print("-"*30)
            print("Ocorreu um erro inesperado, certifique-se de usar números inteiros e tente novamente")
            Continuar()
            continue
        
        if (escolha == 0):
            print("\nVoltando para o menu...")
            running = False
            Continuar()
        elif (escolha == 1):
            print("-"*30)
            running = False
            Cadastro_De_Livros(lista_filiais)
        elif (escolha == 2):
            print("-"*30)
            running = False
            Cadastro_De_Filiais(lista_filiais)

# Função para a escolha da busca
def Escolher_Busca(lista_filiais):
    running = True

    while running:
        print("Como deseja procurar o livro?\n")
        print("1 - Buscar livros por código")
        print("2 - Buscar livros por nome")
        print("3 - Buscar livros por categoria")
        print("4 - Buscar livros por preço")
        print("5 - Busca por quantidade em estoque")
        print("0 - Sair")

        try:
            escolha = int(input(": "))
        except ValueError:
            print("-"*30)
            print("Entrada inválida. Utilize números inteiros.")
            Continuar()
            continue
        except Exception as error: #* Em caso de erros inesperados
            print("-"*30)
            print("Ocorreu um erro inesperado, certifique-se de usar números inteiros e tente novamente")
            Continuar()
            continue
        
        if (escolha == 0):
            print("\nVoltando para o menu...")
            running = False
            Continuar()
        elif (escolha == 1):
            print("-"*30)
            running = False
            Info_Por_Codigo(lista_filiais)
        elif (escolha == 2):
            print("-"*30)
            running = False
            Info_Por_Nome(lista_filiais)
        elif (escolha == 3):
            print("-"*30)
            running = False
            Info_Por_Categoria(lista_filiais)
        elif (escolha == 4):
            print("-"*30)
            running = False
            Info_Por_Valor(lista_filiais)
        elif (escolha == 5):
            print("-"*30)
            running = False
            Info_Por_Estoque(lista_filiais)

# Função para enviar o Livro para o estoque e adiciona-lo na Filial correta
def Enviar_Livro_Para_a_Filial_No_Estoque(codigo_filial_inserido, livro):
    
    # 'Salvando' o texto atual do arquivo em uma variável
    with open("estoque_filiais.txt", "r", encoding="utf-8") as arquivo_atual:
        texto_arquivo_atual = arquivo_atual.readlines()
    
    # Abrindo o arquivo para escrita
    with open("estoque_filiais.txt", "w", encoding="utf-8") as arquivo_novo:
        # 'Lendo' o texto do arquivo atual, pela variável já salva
        for linha in texto_arquivo_atual:
            
            if linha != "":
                # Verificando se a linha representa uma Filial
                if linha[0] == "#":
                    # Extraindo o código da Filial
                    filial = linha.strip().replace("\n", "").split(",")
                    codigo_filial_para_verificar = filial[0].replace("#FL", "")
                    
                    # Verificando se o código é o mesmo que o inserido pelo usuário
                    if (codigo_filial_para_verificar == codigo_filial_inserido):
                        linha = linha + f"{livro.codigo},{livro.titulo},{livro.ano},{livro.categoria},{livro.editora},R${livro.valor},{livro.estoque}\n"
                    
                arquivo_novo.write(linha)

# Função de cadastro de livros
def Cadastro_De_Livros(lista_filiais):
    recebendo_valores = True

    print("Cadastro de Livros\n")
    
    while recebendo_valores: # Código
        try:
            print("Digite o código de um Filial.")
            print("O livro será cadastrado na Filial correspondente.")
            codigo_filial = input(": ")
            
            if codigo_filial:
                codigo_existe = Verificar_Filial(codigo_filial)
                
                if codigo_existe:
                    codigo_filial = "#FL" + codigo_filial
                    recebendo_valores = False
                else: # Caso o código não exista no sistema
                    print("\nCódigo inválido. Este código não foi encontrado no sistema.")
                    Continuar()
                    continue
            else:
                raise ValueError

        except ValueError:
            print("\nCódigo inválido, digite apenas os números inteiros do código.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

    # 'Reiniciando' para o próximo loop
    recebendo_valores = True

    while recebendo_valores: # Código
        try:
            codigo_livro = int(input("Digite o código do livro: "))
            
            if codigo_livro:
                recebendo_valores = False
            else:
                raise ValueError

        except ValueError:
            print("\nCódigo inválido, utilize apenas números inteiros.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

    # 'Reiniciando' para o próximo loop
    recebendo_valores = True
    
    while recebendo_valores: # Título
        try:
            titulo = input("Digite o titulo do livro: ")
            
            if (len(titulo) > 0):
                recebendo_valores = False
            else:
                raise ValueError

        except ValueError:
            print("\nTítulo inválido, utilize caracteres alfabéticos, números ou símbolos.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue
    
    # 'Reiniciando' para o próximo loop
    recebendo_valores = True
    
    while recebendo_valores: # Editora
        try:
            editora = input("Digite a editora do livro: ")
            
            if (len(editora) > 0):
                recebendo_valores = False
            else:
                raise ValueError

        except ValueError:
            print("\nEditora inválida, utilize caracteres alfabéticos, números ou símbolos.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue
    
    # 'Reiniciando' para o próximo loop
    recebendo_valores = True
    
    while recebendo_valores: # Categoria
        try:
            categoria = input("Digite a categoria do livro: ")
            
            if (len(categoria) > 0):
                recebendo_valores = False
            else:
                raise ValueError

        except ValueError:
            print("\nCategoria inválida, utilize caracteres alfabéticos, números ou símbolos.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue
    
    # 'Reiniciando' para o próximo loop
    recebendo_valores = True
    
    while recebendo_valores: # Ano
        try:
            # Coletando o input como string
            ano = input("Digite o ano de publicação do livro: ")
            
            if (len(ano) <= 0):
                raise ValueError

            elif (len(ano) <= 4):
                try:
                    # Convertendo ano para int
                    ano = int(ano)

                    ano_atual = datetime.now().year

                    if ano <= 0:
                        print("\nNão será aceito números menores que zero.")
                        raise ValueError

                    elif ano > ano_atual:
                        print("\nAno inexistente")
                        raise ValueError
                    
                    recebendo_valores = False
                except ValueError:
                    print("\nEntrada inválida, insira um ano válido.")
                    Continuar()
                    continue
            else:
                print("\nEntrada inválida, insira um ano válido.")
                Continuar()
                continue
            
        except ValueError:
            print("\nEntrada inválida, insira um ano válido.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue
    
    # 'Reiniciando' para o próximo loop
    recebendo_valores = True
    
    while recebendo_valores: # Valor
        try:
            valor = input("Digite o valor da unidade deste livro: ")
            
            if (len(valor) > 0):
                valor = float(valor)
                
                recebendo_valores = False
            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido, utilize números inteiros ou flutuantes.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue
    
    # 'Reiniciando' para o próximo loop
    recebendo_valores = True
    
    while recebendo_valores: # Estoque
        try:
            estoque = input("Digite a quantidade em estoque: ")
            
            if (len(estoque) > 0):
                estoque = int(estoque)
                
                recebendo_valores = False
            else:
                raise ValueError

        except ValueError:
            print("\nQuantidade inválida, utilize apenas números inteiros.")
            Continuar()
            continue
        except Exception as error:
            print("\nOcorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

    # Calculo para o valor total em estoque
    valor_estoque = valor * estoque
    
    livro = Livro(codigo_livro, titulo, editora, categoria, ano, valor, estoque)
    
    # Etapa de confirmação de dados, para o cadastro do livro
    Confirmação_De_Cadastro_Do_Livro(livro, codigo_filial, lista_filiais)

# Função para o usuário confirmar o cadastro do livro
def Confirmação_De_Cadastro_Do_Livro(livro, codigo_filial, lista_filiais):
    running = True
    
    while running:
        print("-"*30)
        print("Confirmando os dados...\n")
        
        valor_estoque = livro.valor * livro.estoque
        
        print(f"Filial: #FL{codigo_filial}")
        print(f"\n>>>>>>Cod#{livro.codigo}")
        print(f"Titulo/Editora: {livro.titulo}/{livro.editora}")
        print(f"Categoria: {livro.categoria}")
        print(f"Ano: {livro.ano}")
        print(f"Valor: R$ {livro.valor}")
        print(f"Estoque: {livro.estoque:.2f} unidade(s)")
        print(f"Valor total em estoque: R$ {valor_estoque:.2f}\n")
        
        print("-"*30)
        
        print("Cadastrar?\n")
        print("S - Confirmar")
        print("N - Cancelar\n")
        
        try:
            confirmação = input("Escolha: ").upper()
        except ValueError:
            print("\nOcorreu um erro na entrada. Utilize uma das opções válidas e tente novamente.")
            Continuar()
            continue
        except Exception as error:
            print("Ocorreu um erro inesperado, tente novamente.")
            print(f"Mensagem do erro: {error}")
            Continuar()
            continue
        
        if confirmação == "S":
            print("-"*30)
            print("\nCadastrando o livro...")
            print(".")
            print(".")
            print(".")

            try:
                #Adicionando o Livro na Filial correta
                for filial in lista_filiais:
                    if filial.codigo == codigo_filial:
                        filial.Adicionar_Livro(livro)
                
                print("Livro cadastrado com sucesso.")
                
                #* Condição para o término da repetição
                running = False
                Continuar()
            except Exception as error:
                print("Ocorreu um erro no cadastro, tente novamente.")
                print("Erro: ", error)
                Continuar()
                continue

        elif confirmação == "N":
            print("-"*30)
            print("Cancelando o cadastro...")
            print(".")
            print(".")
            print(".")
            print("Cadastro cancelado.")
            #* Condição para o término da repetição
            running = False
            Continuar()
        
        else:
            print("-"*30)
            print("Opção inválida, tente novamente.")
            Continuar()
            continue

# Função de cadastro de Filiais
# A Filial é cadastrada sem Livros
def Cadastro_De_Filiais(lista_filiais):
    running = True

    while running:
        print("Cadastro de Filiais\n")
        
        codigo = Entrada_do_Codigo_Filial()

        # Flag para repetição de inputs individuais
        recebendo_valores = True

        while recebendo_valores: # Nome
            try:
                nome = input("Digite o nome da filial: ")
                
                if nome != "":
                    recebendo_valores = False
                else:
                    print("\nInsira algum valor válido no campo.")
                    Continuar()
                    continue
                
            except ValueError:
                print("\nNome inválido, digite apenas caracteres alfabéticos.")
                Continuar()
                continue
            except Exception as error:
                print("\nOcorreu um erro inesperado, tente novamente.")
                Continuar()
                continue

        recebendo_valores = True

        while recebendo_valores: # Endereço
            try:
                endereco = input("Digite o endereço da filial: ")
                
                if endereco != "":
                    recebendo_valores = False
                else:
                    print("\nInsira algum valor válido no campo.")
                    Continuar()
                    continue
                
            except ValueError:
                print("\nEndereço inválido, digite apenas caracteres alfabéticos.")
                Continuar()
                continue
            except Exception as error:
                print("\nOcorreu um erro inesperado, tente novamente.")
                Continuar()
                continue
        
        recebendo_valores = True

        while recebendo_valores: # Telefone
            try:
                telefone = input("Digite o telefone da filial: ")
                
                if telefone != "":
                    recebendo_valores = False
                else:
                    print("\nInsira algum valor válido no campo.")
                    Continuar()
                    continue

            except ValueError:
                print("\nTelefone inválido, digite no formato: xxxx-xxxx.")
                Continuar()
                continue
            except Exception as error:
                print("\nOcorreu um erro inesperado, tente novamente.")
                Continuar()
                continue
        
        try:
            lista_filiais.append(Filial(
                codigo,
                nome,
                endereco,
                telefone
            ))

            running = False
        except Exception as error:
            print("\nOcorreu um erro inesperado ao realizar o cadastro. Tente novamente.")
            Continuar()

#Função de busca de Livros por código, mostrando valores diferentes entre as Filiais
def Info_Por_Codigo(lista_filiais):
    if len(lista_filiais) > 0:
        recebendo_valores = True
        encontrados = 0

        while recebendo_valores:
            print("\nBusca pelo código do livro\n")
            
            try:
                codigo_inserido = input("Digite o código do livro desejado: ").upper()
                
                if (len(codigo_inserido) <= 0):
                    raise ValueError
            
            except ValueError:
                print("\nOcorreu um erro na entrada, utilize apenas números inteiros e tente novamente.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem de erro: {error}")
                Continuar()
                continue
            
            print("Buscando livros...")
            
            try:
                # Lista de Livros repetidos, com alguns valores diferentes
                lista_livros = []
                
                lista_enderecos_filiais = []

                # diferenca = [valor, endereço_filial, estoque]
                lista_diferencas = []

                for filial in lista_filiais:
                    lista_enderecos_filiais.append(filial.endereco)
                    
                    # Adicionando todos os livros que possuem o 'codigo_inserido' na lista de Livros
                    lista_livros.append(filial.Retornar_Livro_por_Codigo(codigo_inserido))
                    
                    encontrados += 1

                # Contador para selecionar o endereço correto na lista
                contador_enderecos = 0

                # Procurando as diferenças entre as Filiais e os endereços
                for livro in lista_livros:
                    endereco_filial = lista_enderecos_filiais[contador_enderecos]
                    lista_diferencas.append([livro.valor, endereco_filial, livro.estoque])
                    contador_enderecos += 1

                try:
                    livro.Info_Diferencas(lista_diferencas)
                except Exception as error:
                    print("\nOcorreu um erro inesperado durante a busca. Tente novamente mais tarde.")
                    Continuar()
                    continue
                
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro com este titulo foi encontrado.")
                
                recebendo_valores = False
                Continuar()

            except Exception as error:
                print("Ocorreu um erro inesperado durante a busca. Tente novamente mais tarde.")
                Continuar()
                continue

    else:
        print("\nNão existe nenhuma Filial na lista local")
        Continuar()

# Função de busca de livros pelo titulo
def Info_Por_Nome(lista_filiais):
    if len(lista_filiais) > 0:

        codigo_inserido = Entrada_do_Codigo_Filial()

        recebendo_valores = True
        encontrados = 0

        while recebendo_valores:
            print("\nBusca pelo nome do livro\n")
            
            try:
                titulo_inserido = input("Digite o titulo do livro desejado: ").upper()
                
                if (len(titulo_inserido) <= 0):
                    raise ValueError
            
            except ValueError:
                print("\nOcorreu um erro na entrada, utilize apenas caracteres alfabéticos e tente novamente.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem de erro: {error}")
                Continuar()
                continue
            
            print("Buscando livros...")
            
            try:
                for filial in lista_filiais:
                    if filial.codigo == codigo_inserido:
                        encontrados += 1
                        filial.Info_Livro_por_Nome(titulo_inserido)
                
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro com este titulo foi encontrado.")
                
                recebendo_valores = False
                Continuar()

            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue

    else:
        print("\nNão existe nenhuma Filial na lista local")
        Continuar()

# Função de busca de livros por categoria
def Info_Por_Categoria(lista_filiais):
    if len(lista_filiais) > 0:

        codigo_inserido = Entrada_do_Codigo_Filial()

        recebendo_valores = True
        encontrados = 0

        while recebendo_valores:
            print("\nBusca pela categoria do livro\n")
            
            try:
                categoria_inserida = input("Digite a categoria do livro desejado: ").upper()
                
                if (len(categoria_inserida) <= 0):
                    raise ValueError
            
            except ValueError:
                print("\nOcorreu um erro na entrada, utilize apenas caracteres alfabéticos e tente novamente.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem de erro: {error}")
                Continuar()
                continue
            
            print(f"Buscando livros com a categoria: {categoria_inserida}...")
            
            try:
                for filial in lista_filiais:
                    if filial.codigo == codigo_inserido:
                        encontrados += 1
                        filial.Info_Livro_por_Categoria(categoria_inserida)
                
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro com esta categoria foi encontrado.")
                
                recebendo_valores = False
                Continuar()

            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue

    else:
        print("\nNão existe nenhuma Filial na lista local")
        Continuar()

# Função de busca de livros pelo valor
def Info_Por_Valor(lista_filiais):
    if len(lista_filiais) > 0:

        codigo_inserido = Entrada_do_Codigo_Filial()

        recebendo_valores = True
        encontrados = 0

        while recebendo_valores:
            print("\nBusca pelo valor máximo do livro\n")
            
            try:
                valor_inserido = float(input("Digite o valor máximo desejado para a busca: "))
                
                if (len(valor_inserido) <= 0):
                    raise ValueError
            
            except ValueError:
                print("\nOcorreu um erro na entrada, utilize apenas caracteres alfabéticos e tente novamente.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem de erro: {error}")
                Continuar()
                continue
            
            print(f"Buscando livros até o valor de R$ {valor_inserido:.2f}...")
            
            try:
                for filial in lista_filiais:
                    if filial.codigo == codigo_inserido:
                        encontrados += 1
                        filial.Info_Livro_por_Valor(valor_inserido)
                
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro até este valor foi encontrado.")
                
                recebendo_valores = False
                Continuar()

            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue

    else:
        print("\nNão existe nenhuma Filial na lista local")
        Continuar()

# Função de busca de livros pelo estoque
def Info_Por_Estoque(lista_filiais):
    if len(lista_filiais) > 0:

        codigo_inserido = Entrada_do_Codigo_Filial()

        recebendo_valores = True
        encontrados = 0

        while recebendo_valores:
            print("\nBusca pela quantidade mínima do livro\n")
            
            try:
                estoque_inserido = float(input("Digite a quantidade mínima desejada para a busca: "))
                
                if (len(estoque_inserido) <= 0):
                    raise ValueError
            
            except ValueError:
                print("\nOcorreu um erro na entrada, utilize apenas caracteres alfabéticos e tente novamente.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem de erro: {error}")
                Continuar()
                continue
            
            print(f"Buscando livros com quantidade maior que: {estoque_alvo}...")
            
            try:
                for filial in lista_filiais:
                    if filial.codigo == codigo_inserido:
                        encontrados += 1
                        filial.Info_Livro_por_Estoque(estoque_inserido)
                
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro com quantidade maior que esta foi encontrado.")
                
                recebendo_valores = False
                Continuar()

            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue

    else:
        print("\nNão existe nenhuma Filial na lista local")
        Continuar()

# Função de calculo para o valor total em estoque (entre todos as Filiais)
def Valor_Total_Estoque(lista_filiais):
    if len(lista_filiais) > 0:
        valor_total = 0
        
        print("Calculando o valor total em estoque...\n")
        
        try:
            for filial in lista_filiais:
                valor_total += filial.Retornar_Valor_Total_de_Livros()
            
            print(f"\nO valor total do estoque, entre todas as Filiais, é de: R$ {valor_total:.2f}")
        except Exception as error:
            print("\nNão foi possível realizar o calculo. Erro inesperado.")
            print(f"Mensagem de erro: {error}")

    else:
        print("\nNão existe nenhuma Filial na lista local")
    
    Continuar()

# Função para coletar os dados no arquivo de estoque
def Carregar_Estoque():
    contador_linhas = 0

    print("Carregando dados do arquivo de estoque...\n")

    try:
        # Abrindo o arquivo
        arquivo = open("estoque_filiais.txt", "r", encoding="utf-8")

        # carregando todas as linhas do arquivo
        for linha in arquivo:
            if linha[0] == "#": # A linha representa uma Filial
                # Separe a linha em uma lista
                filial = linha.strip().replace("\n", "").split(",")
                filial = Filial(
                        codigo=filial[0],
                        nome=filial[2],
                        endereco=filial[1],
                        telefone=filial[3]
                    )
            
            else: # A linha representa um Livro
                contador_linhas += 1
                linha = linha.replace("\n", "").replace("R$", "").split(",")
            
                try:
                    novo_valor = float(linha[-2])
                except ValueError:
                    print(
                        f"\nOcorreu um erro ao carregar o valor presente na linha: {contador_linhas}"
                    )
                    print("\nCancelando a função....")
                    print("\nVerifique o dado e tente novamente.")
                    Continuar()
                    break
                except Exception as error:
                    print("\nOcorreu um erro inesperado com o valor, verifique o arquivo e tente novamente")
                    Continuar()
                    break

                try:
                    novo_estoque = int(linha[-1])
                except ValueError:
                    print(
                        f"\nOcorreu um erro ao carregar a quantidade presente na linha: {contador_linhas}"
                    )
                    print("\nCancelando a função....")
                    print("\nVerifique o dado e tente novamente.")
                    Continuar()
                    break
                except Exception as error:
                    print("\nOcorreu um erro inesperado com a quantidade, verifique o arquivo e tente novamente")
                    Continuar()
                    break

            try:
                if linha[0] == "#": # Se for uma Filial, adicione na lista de Filiais
                    lista_filiais.append(filial)
                else:
                    livro = Livro(
                        codigo=linha[0],
                        titulo=linha[1],
                        editora=linha[4],
                        categoria=linha[3],
                        ano=linha[2],
                        valor=novo_valor,
                        estoque=novo_estoque
                    )
                    filial.Adicionar_Livro(livro)
            except Exception as error:
                print("\nOcorreu um erro inesperado ao carregar, verifique o arquivo e tente novamente")
                Continuar()
                break
        
        # fechando o arquivo no final da função
        arquivo.close()
        
        Continuar()
    except FileNotFoundError:
        print("O arquivo de estoque não foi encontrado, certifique-se de que ele exista e está localizado junto com o programa.")
        Continuar()
    except IOError:
        print("O arquivo apresentou algum erro que impediu a leitura.")
        Continuar()
    except Exception as error:
        print("Ocorreu um erro inesperado, tente novamente.")
        Continuar()

# Função de atualizaro arquivo de estoque
def Atualizar_Estoque(lista_filiais):
    if (len(lista_filiais) > 0):
        running = True

        while running:
            try:
                print("Atualizando o arquivo de estoque...")
            
                # Abrindo o arquivo para adicionar as Filiais
                with open("estoque_filiais.txt", "w", encoding="utf-8") as arquivo:
                    try:
                        for filial in lista_filiais:
                            # escrevendo as Filiais no arquivo
                            arquivo.write(f"{filial.codigo},{filial.endereco},{filial.nome},{filial.telefone}\n")
                            
                            # Adicionando os Livros logo abaixo da Filial
                            for livro in filial.livros:
                                arquivo.write(f"{livro.codigo},{livro.titulo},{livro.ano},{livro.categoria},{livro.editora},{livro.valor},{livro.estoque}\n")

                        running = False
                    except Exception as error:
                        print("\nOcorreu um erro na hora de atualizar o arquivo de estoque.")
                        print(f"Mensagen de erro: {error}\n")
                        
                        # Perguntando se o usuário quer repetir a função anterior
                        repeticao = True
                        
                        while repeticao:
                            print("\nDeseja executar a função novamente? S/N")
                            try:
                                escolha = input(": ")

                                if (escolha.upper() == "N"):
                                    print("Cancelando a execução da funcionalidade...")
                                    Continuar()
                                    repeticao = False
                                    running = False

                                elif (escolha.upper() == "S"):
                                    print("Executando novamente...")
                                    Continuar()
                                    repeticao = False

                                else:
                                    print("Opção inválida, tente novamente...")

                            except ValueError:
                                print("\nOcorreu um erro com o valor inserido, selecione uma opção válida.")
                                Continuar()
                                continue
                            except Exception as error:
                                print("Ocorreu um erro inesperado, tente novamente.")
                                Continuar()
                                continue

            except FileNotFoundError:
                print("O arquivo de estoque não foi encontrado, certifique-se de que ele exista e está localizado junto com o programa.")
                Continuar()
                continue
            except IOError:
                print("O arquivo apresentou algum erro que impediu a leitura.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue

    else:
        print("Não foi possível atualizar o arquivo.")
        print("Não há nenhuma Filial na lista local.")
        Continuar()

# Função para listar os Livros que estão cadastrados em uma Filial específica
# Retorna Também o valor total em estoque
def Listar_Estoque_da_Filial(lista_filiais):
    running = True
    
    while running:
        if len(lista_filiais) > 0:
            codigo_inserido = Entrada_do_Codigo_Filial()

            if codigo_inserido != "":
                try:
                    for filial in lista_filiais:
                        if filial.codigo == codigo_inserido:
                            filial.Info_Livros()
                            break
                    
                    filial.Calcular_Valor_Total_de_Livros()
                    
                    running = False
                except Exception as error:
                    print("\nOcorreu ao listar os livros da Filial. Tente novamente.")
                    print(f"Mensagem do erro: {error}")
                    Continuar()
                    continue
            else:
                print("\nDigite um código para a busca.")
                Continuar()
                continue

        else:
            print("\nNão existe nenhuma Filial na lista local")

    Continuar()

# Função que será executada antes de encerrar o sistema
def Finalizar_Sessão(lista_filiais):
    running = True
    
    while running:
        print("Antes de sair...")
        print("Deseja Atualizar o arquivo de estoque? S/N")
        
        try:
            escolha = input(": ").upper()
            
            if(escolha != "S" and escolha != "N"):
                raise ValueError
            elif (escolha == "S"):
                Atualizar_Estoque(lista_filiais)
                Continuar()
                running = False
                print("Encerrando atividades...")
            elif (escolha == "N"):
                print("\nO arquivo não será salvo\n")
                Continuar()
                running = False
                print("\nEncerrando atividades...")

        except ValueError:
            print("\nEntrada inválida, selecione uma opção válida e tente novamente.")
            Continuar()
            continue
        except Exception as error:
            print("Ocorreu um error inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

# Função para evitar o excesso de informações à vista do usuário,
# requerindo um input qualquer para continuar
def Continuar():
    print("-"*30)
    input("Continuar...")

#* Função Principal
if __name__ == "__main__":
    # lista de filiais
    lista_filiais = []

    # escolha inserida pelo usuário, 
    # número inicial é irrelevante, serve apenas para o começo do loop.
    escolha = 1

    print("-"*30)
    print("\tSistema Livraria")
    
    # Condição para executar o sistema
    while escolha != 0:
        
        # Menu
        print("-"*30)
        print("Funcionalidades Disponíveis: \n")
        print("1 - Cadastrar Livro ou Filial")
        print("2 - Listar livros")
        print("3 - Buscar Livros")
        print("4 - Valor total no estoque")
        print("5 - Carregar estoque")
        print("6 - Atualizar arquivo no estoque")
        print("7 - Listagem de estoque")
        print("0 - Encerrar atividades\n")
        
        # Entrada da escolha do usuário
        try:
            escolha = int(input(
                "Digite o número da funcionalidade desejada: "))
        except ValueError: #* Caso a conversão não seja possível
            print("-"*30)
            print("Entrada inválida. Utilize números inteiros.")
            Continuar()
            continue
        except Exception as error: #* Em caso de erros inesperados
            print("-"*30)
            print("Ocorreu um erro inesperado, certifique-se de usar números inteiros e tente novamente")
            Continuar()
            continue

        if escolha == 0: # Encerrar o sistema
            print("-"*30)
            Finalizar_Sessão(lista_filiais)

        elif escolha == 1: # Cadastro de livros
            print("-"*30)
            Escolher_Cadastro(lista_filiais)

        elif escolha == 2: # Listagem geral dos livros, em todas as Filiais
            print("-"*30)
            
            if (len(lista_filiais) > 0):
                print("Lista dos livros cadastrados: ")
                for filial in lista_filiais:
                    filial.Info_Livros()
                    print("-"*20)
                
            else:
                print("Nenhuma Filial salva na lista local.")

            Continuar()

        elif escolha == 3: # Buscar livros
            print("-"*30)
            Escolher_Busca(lista_filiais)

        elif escolha == 4: # Valor total no estoque
            print("-"*30)
            Valor_Total_Estoque(lista_filiais)

        elif escolha == 5: # Carregar arquivo de livros
            print("-"*30)
            
            # Apagando os valores das listas locais
            lista_filiais = []

            Carregar_Estoque()
        
        elif escolha == 6: # Atualizar o arquivo de estoque
            print("-"*30)
            Atualizar_Estoque(lista_filiais)

        elif escolha == 7: # Listagem do estoque de uma Filial específica
            print("-"*30)
            Listar_Estoque_da_Filial(lista_filiais)

        else: # Opção inválida
            print("-"*30)
            print("Opção não encontrada")