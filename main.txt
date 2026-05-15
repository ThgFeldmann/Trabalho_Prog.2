#* Classe para Livros
class Livro:
    def __init__(
                self, 
                titulo = "Lorem Ipsum", 
                codigo = "0123", 
                editora = "Lorem Ipsum", 
                categoria = "Lorem Ipsum",
                ano = "2000", 
                valor = 10.00, 
                estoque = 0
            ):

        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
    
    def Info(self): # Método para informar *todos* os livros

        # Calculo para o valor total em estoque
        valor_estoque = self.valor * self.estoque

        print(f"\n>>>>>>Cod#{self.codigo}")
        print(f"Titulo/Editora: {self.titulo}/{self.editora}")
        print(f"Categoria: {self.categoria}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor}")
        print(f"Estoque: {self.estoque:.2f} unidade(s)")
        print(f"Valor total em estoque: R$ {valor_estoque:.2f}")

#* Funções

# Função de cadastro de livros
def Cadastro(lista_livros):
    recebendo_valores = True

    print("Cadastro de Livros\n")

    while recebendo_valores: # Código
        try:
            codigo = input("Digite o código do livro: ")
            
            if (len(codigo) > 0):
                recebendo_valores = False
            else:
                raise ValueError

        except ValueError:
            print("\nCódigo inválido, utilize caracteres alfabéticos ou números.")
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
            ano = input("Digite o ano de publicação do livro: ")
            
            if (len(ano) <= 0):
                raise ValueError

            elif (len(ano) <= 4):
                try:
                    ano = int(ano)
                    
                    recebendo_valores = False
                except ValueError:
                    print("\nEntrada inválida, insira no máximo quatro(4) números inteiros.")
                    Continuar()
                    continue
            else:
                print("\nEntrada inválida, insira no máximo quatro(4) números inteiros.")
                Continuar()
                continue
            
        except ValueError:
            print("\nEntrada inválida, insira no máximo quatro(4) números inteiros.")
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
    
    # Etapa de confirmação de dados, para o cadastro do livro
    Confirmação_De_Cadastro(codigo, titulo, editora, categoria, ano, valor, estoque, valor_estoque)

# Função para o usuário confirmar o cadastro do livro
def Confirmação_De_Cadastro(codigo, titulo, 
                            editora, categoria, ano, 
                            valor, estoque, valor_estoque):
    running = True
    
    while running:
        print("-"*30)
        print("Confirmando os dados...")
        print(f"\n>>>>>>Cod#{codigo}")
        print(f"Titulo/Editora: {titulo}/{editora}")
        print(f"Categoria: {categoria}")
        print(f"Ano: {ano}")
        print(f"Valor: R$ {valor}")
        print(f"Estoque: {estoque:.2f} unidade(s)")
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
                lista_livros.append(Livro(
                    codigo=codigo,
                    titulo=titulo,
                    editora=editora,
                    categoria=categoria,
                    ano=ano,
                    valor=valor,
                    estoque=estoque
                ))
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

# Função de busca de livros pelo titulo
def Info_Por_Nome(lista_livros):
    
    if (len(lista_livros) > 0):
        running = True
        nome_alvo = ""
        encontrados = 0
        
        while running:
            print("Busca pelo nome do livro\n")
            
            try:
                nome_alvo = input("Digite o titulo do livro desejado: ").upper()
                
                if (len(nome_alvo) <= 0):
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
                for livro in lista_livros:
                    if (livro.titulo.upper() == nome_alvo):
                        encontrados += 1
                        livro.Info()
                        print("")
                        
                    print("-"*30)
                
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro com este titulo foi encontrado.")
                
                running = False
                Continuar()

            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue
        
    else:
        print("Não será possível buscar livros.")
        print("Não há nenhum livro salvo na lista local.")
        Continuar()

# Função de busca de livros por categoria
def Info_Por_Categoria(lista_livros):
    
    if (len(lista_livros) > 0):
        running = True

        categoria_alvo = ""
        encontrados = 0
        
        while running:
            print("Busca pela categoria do livro\n")
        
            try:
                categoria_alvo = input("Digite a categoria desejada: ").upper()
                
                if (len(categoria_alvo) <= 0):
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
                # filtragem livro por livro
                for livro in lista_livros:
                    if (livro.categoria.upper() == categoria_alvo):
                        encontrados += 1
                        livro.Info()
                        print("")
                
                print("-"*30)
                
                # verificação para caso livros foram encontrados, ou não
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro com esta categoria foi encontrado.")
                
                running = False
                Continuar()

            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem do erro: {error}")
                Continuar()
                continue
        
    else:
        print("Não será possível buscar livros.")
        print("Não há nenhum livro salvo na lista local.")
        Continuar()

# Função de busca de livros pelo valor
def Info_Por_Valor(lista_livros):
    
    if (len(lista_livros) > 0):
        running = True
        
        valor_alvo = 0.00
        encontrados = 0
        
        while running:
        
            print("Busca pelo preco do livro\n")
            
            try:
                valor_alvo = float(input("Digite o valor máximo desejado para a busca: "))
                
                print(f"Buscando livros até o valor de R$ {valor_alvo:.2f}...")
                
                # filtragem livro por livro
                for livro in lista_livros:
                    if (livro.valor <= valor_alvo):
                        encontrados += 1
                        livro.Info()
                        print("")
                
                print("-"*30)
                
                # verificação para caso livros foram encontrados, ou não
                if encontrados > 0:
                    print(f"\n{encontrados} livro(s) foram encontrados.")
                else:
                    print("\nNenhum livro até este valor foi encontrado.")
                
                running = False
                Continuar()
            except ValueError:
                print("\nOcorreu um erro, tente novamente utilizando números inteiros ou flutuantes.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem do erro: {error}")
                Continuar()
                continue
    else:
        print("Não será possível buscar livros.")
        print("Não há nenhum livro salvo na lista local.")
        Continuar()

# Função de busca de livros pelo estoque
def Info_Por_Estoque(lista_livros):
    
    if (len(lista_livros) > 0):
        running = True
        
        estoque_alvo = 0
        encontrados = 0
        
        while running:
            print("Busca de livros pela quantidade em estoque\n")
            
            try:
                estoque_alvo = int(input("Digite a quantidade mínima desejada para a busca: "))
                
                print(f"Buscando livros com quantidade maior que: {estoque_alvo}...")
                
                # filtragem livro por livro
                for livro in lista_livros:
                    if (livro.estoque >= estoque_alvo):
                        encontrados += 1
                        livro.Info()
                        print("")
                
                print("-"*30)
                
                # verificação para caso livros foram encontrados, ou não
                if encontrados == 1:
                    print(f"\n{encontrados} livro foi encontrado.")
                
                elif encontrados > 1:
                    print(f"\n{encontrados} livros foram encontrados.")
                else:
                    print("\nNenhum livro com quantidade maior que esta foi encontrado.")
                
                running = False
                Continuar()
                
            except ValueError:
                print("\nOcorreu um erro, tente novamente usando números inteiros.")
                Continuar()
                continue
            except Exception as error:
                print("Ocorreu um erro inesperado, tente novamente.")
                print(f"Mensagem do erro: {error}")
                Continuar()
                continue
    else:
        print("Não será possível buscar livros.")
        print("Não há nenhum livro salvo na lista local.")
        Continuar()

# Função de calculo para o valor total em estoque (entre todos os livros)
def Valor_Total_Estoque(lista_livros):
    
    if (len(lista_livros) > 0):
        valores_totais_livros = 0.0
        estoque_total = 0
        valor_total_estoque = 0.0

        print("Calculando o valor total em estoque...\n")
        
        for livro in lista_livros:
            valores_totais_livros += livro.valor
            estoque_total += livro.estoque
        
        valor_total_estoque = valores_totais_livros * estoque_total
        
        if (valor_total_estoque > 0):
            print("Valor total em estoque: ")
            print(f"R$ {valor_total_estoque:.2f}")
        else: 
            print("Não foi possível calcular o valor total do estoque.")
        
        Continuar()
    else:
        print("Não será possível calcular o valor total do estoque.")
        print("Não há nenhum livro salvo na lista local.")
        Continuar()

# Função de busca no arquivo de dados
def Carregar_Estoque():
    contador_linhas = 0

    print("Carregando livros do arquivo...\n")

    try:
        # Abrindo o arquivo
        arquivo = open("estoque.txt", "r", encoding="utf-8")

        # carregando todas as linhas do arquivo
        for linha in arquivo:
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
                lista_livros.append(Livro(
                    codigo=linha[0],
                    titulo=linha[1],
                    editora=linha[2],
                    categoria=linha[3],
                    ano=linha[4],
                    valor=novo_valor,
                    estoque=novo_estoque
                ))
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
        print("O arquivo apresentou algum erro, impedindo a leitura.")
        Continuar()
    except Exception as error:
        print("Ocorreu um erro inesperado, tente novamente.")
        Continuar()

# Função de atualizaro arquivo de estoque
def Atualizar_Estoque(lista_livros):
    if (len(lista_livros) > 0):
        running = True

        while running == True:
            print("Atualizando o arquivo de estoque...")
        
            # Abrindo o arquivo para adicionar conteúdo
            arquivo = open("estoque.txt", "w", encoding="utf-8")
            
            try:
                for livro in lista_livros:
                    arquivo.write(f"{livro.codigo},{livro.titulo},{livro.ano},{livro.categoria},{livro.editora},R${livro.valor},{livro.estoque}\n")

                arquivo.close()
                running = False

            except Exception as error:
                print("\nOcorreu um erro na hora de atualizar o arquivo de estoque.")
                print(f"Mensagen de erro: {error}\n")

                #? Daqui para baixo está funcionando à base da gambiarra. *não mexer*.
                flag = Repetir_Função()
                
                if (flag == True): #* Parar a função
                    running = False
                elif (flag == False): #* Repetir a função
                    Continuar()
                    print("-"*30)

    else:
        print("Não foi possível atualizar o arquivo.")
        print("Não há nenhum livro salvo na lista local.")
        Continuar()

# Função para o usuário escolher se deve repetir a função
def Repetir_Função():
    repetir = True

    while repetir:
        print("\nDeseja executar a função novamente? S/N")
        
        try:
            escolha = input(": ")

            if (escolha.upper() == "N"):
                print("Cancelando a execução da funcionalidade...")
                repetir = False
                # retornando o resultado para parar a execução da função
                return True

            elif (escolha.upper() == "S"):
                print("Executando novamente...")
                repetir = False

                # retornando um sinal para *Não* parar a execução da função
                return False

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

# Função que será executada antes de encerrar o sistema
def Finalizar_Sessão(lista_livros):
    running = True
    
    while running:
        print("Antes de sair...")
        print("Deseja Atualizar o arquivo de estoque? S/N")
        
        try:
            escolha = input(": ").upper()
            
            if(escolha != "S" and escolha != "N"):
                raise ValueError
            elif (escolha == "S"):
                Atualizar_Estoque(lista_livros)
                Continuar()
                running = False
                print("Encerrando atividades...")
            elif (escolha == "N"):
                print("\nO arquivo não será salvo\n")
                Continuar()
                running = False
                print("\nEncerrando atividades...")

        except ValueError:
            print("\nEntrada inválida, utilize caracteres válidos e tente novamente.")
            Continuar()
            continue
        except Exception as error:
            print("Ocorreu um error inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

# Função para evitar o excesso de informações à vista do usuário,
# necessitando de um input qualquer para continuar
def Continuar():
    print("-"*30)
    input("Continuar...")

#* Função Principal
if __name__ == "__main__":
    # lista de livros
    lista_livros = []

    # escolha inserida pelo usuário, 
    # número inicial é irrelevante, serve apenas para o começo do loop.
    escolha = 1

    print("-"*30)
    print("\tSistema Livraria")
    
    # Condição para executar o sistema
    while escolha != 0:
        print("-"*30)
        print("Funcionalidades Disponíveis: \n")
        print("1 - Cadastrar novo livro")
        print("2 - Listar livros")
        print("3 - Buscar livros por nome")
        print("4 - Buscar livros por categoria")
        print("5 - Buscar livros por preço")
        print("6 - Busca por quantidade em estoque")
        print("7 - Valor total no estoque")
        print("8 - Carregar estoque")
        print("9 - Atualizar arquivo no estoque")
        print("0 - Encerrar atividades\n")
        
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
            Finalizar_Sessão(lista_livros)

        elif escolha == 1: # Cadastro de livros
            print("-"*30)
            Cadastro(lista_livros)

        elif escolha == 2: # Listagem geral dos livros
            print("-"*30)
            
            if (len(lista_livros) > 0):
                print("Lista dos livros cadastrados: ")
                for livro in lista_livros:
                    livro.Info()
            else:
                print("Nenhum livro salvo na lista local.")

            Continuar()

        elif escolha == 3: # Buscar livro por nome
            print("-"*30)
            Info_Por_Nome(lista_livros)

        elif escolha == 4: # Buscar livro por categoria
            print("-"*30)
            Info_Por_Categoria(lista_livros)

        elif escolha == 5: # Buscar livro por preço
            print("-"*30)
            Info_Por_Valor(lista_livros)

        elif escolha == 6: # Buscar livro por estoque
            print("-"*30)
            Info_Por_Estoque(lista_livros)

        elif escolha == 7: # Valor total no estoque
            print("-"*30)
            Valor_Total_Estoque(lista_livros)

        elif escolha == 8: # Carregar arquivo de livros
            print("-"*30)
            Carregar_Estoque()
        
        elif escolha == 9:
            print("-"*30)
            Atualizar_Estoque(lista_livros)

        else: # Opção inválida
            print("-"*30)
            print("Opção não encontrada")