import random

###############################################################################
#                   Funções para os  Genes                                    #
###############################################################################

def gene_cb () :
    """Gera um gene válido para o problema das caixas binárias
    
    Return:
        Um valor zero ou um.
    """ 
    lista = [0,1]
    gene = random.choice (lista)
    return gene

# atividade 4
def gene_cnb (valor_max_caixa) :
    """Sortear um número de 0 a 100, gerar um gene válido para o problema das caixas não binárias
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir
    
    Return:
       Um valor de 0 a 'valor_max_caixa' (incluso)
       
    """ 
    
    gene = random.randint (0, valor_max_caixa)
    return gene

# atividade 5

def gene_letra(letras):
    """Sortear uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra



###############################################################################
#                   Funções para os Indivíduos                                #
###############################################################################

def individuo_cb (n):
    """ Gera um indivíduo para o problema das caixas binárias.
    
    Args:
    n: número de genes do indivíduo.
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range (n):
        gene = gene_cb ()
        individuo.append (gene)
    return individuo 

def individuo_cnb (numero_genes, valor_max_caixa):
    """ Gera um indivíduo válido para o nosso o problema das caixas não binárias.
    
    Args:
    numero_genes: numero de genes na lista que representa o indivíduo
    e valor_max-caixa: Valor máximo que a caixa pode assumir
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for _ in range (numero_genes):
        gene = gene_cnb (valor_max_caixa)
        individuo.append (gene)
    return individuo 


# atividade 5 
def individuo_senha(tamanho_da_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_da_senha: inteiro representando o tamanho da senha.
      letras: letras que podem ser sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_da_senha):
        candidato.append(gene_letra(letras))

    return candidato

###############################################################################
#                   Funções para populações                                   #
###############################################################################

def populacao_cb (tamanho, n):
    
    """Cria uma população no problemaq de caixas binárias
    
    Args:
        tamanho: tamanho da população
        n: número de genes do indivíduo
    Returns:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes.
        """
    
    populacao = []
    for _ in range (tamanho):
        populacao.append (individuo_cb (n))
    return populacao

def populacao_cnb (tamanho_populacao,numero_genes, valor_max_caixa):
    
    """Cria uma população no problema de caixas não binárias
    
    Args:
        tamanho_pop: tamanho da individuos da população
        numero_genes: número de genes do indivíduo
        valor_max_caixa: valor maximo que a caixa pode assumir
        
    Returns:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes.
        """
    
    populacao = []
    for _ in range (tamanho_populacao):
        populacao.append (individuo_cnb (numero_genes, valor_max_caixa))
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


###############################################################################
#                                   Seleção                                   #
###############################################################################

def selecao_roleta_max (populacao, fitness):
    """ Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: Apenas funciona para problemas de maximização!!!
    
    Args:
        população: lista com todos os indivíduos da população
        fitness: lista com o valor da funcao objetivo dos individuos da população
    
    Returns: População dos Indivíduos selecionados.
    
    """
    
    populacao_selecionada = random.choices (populacao, weights = fitness, k= len(populacao))
    return populacao_selecionada



# Atividade 5

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness com is valores da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []
    
     # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados
    

###############################################################################
#                  Funções objetivo para indivíduos                           #
###############################################################################

def funcao_objetivo_cb (individuo):
    """ Computa a função objetivo no problema das caixas binárias.
    
    Args:
        n: número de genes dos indivíduo.
    
    Return:
        Um valor representando a soma dos genes do individuo.
    """
    
    return sum (individuo)


def funcao_objetivo_cb (individuo):
    """ Computa a função objetivo no problema das caixas binárias.
    
    Args:
        n:lista contendo os genes das caixas binárias.
    
    Return:
        Um valor representando a soma dos genes do individuo.
    """
    
    return sum(individuo)

def funcao_objetivo_cnb (individuo):
    """ Calcula o fitness do individuo para o problema das caixas não-binárias
    Args:
        individuo: lista que representa um individuo dentro do problrma das CNB
    
    Return:
        Um valor representando o fitness do individuo.
    """
    
    fitness = sum(individuo)
    return fitness

def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca

###############################################################################
#              Funções objetivo para populações                               #
###############################################################################

def funcao_objetivo_pop_cb (populacao):
    """Calcula a funcao objetivo para todos os membros de uma população
    
        Args:
            população: lista com indivíduos selecionados.
        
        Return:
            Lista de valores representando o fitness dos indivíduos
    """
    
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb (individuo)
        fitness.append (fobj)
    return fitness 

def funcao_objetivo_pop_cnb (populacao):
    """Calcula o fitness da população completa
    
        Args:
            população: lista com todos os individuos da população
        
        Return:
            Lista de valores representando o fitness dos indivíduos em ordem
    """
    
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb (individuo)
        fitness_pop.append (fitness_ind)
    return fitness_pop

#atividade 5

def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado





###############################################################################
#                   Cruzamentos                                               #
###############################################################################

def cruzamento_ponto_simples (pai, mae):
    """Operador de cruzamento de ponto simples,
    
    Args:
        pai: uma lista representando um indivíduo
        mãe: uma lista representando um indivíduo
    
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai [ : ponto_de_corte] + mae [ponto_de_corte :]
    filho2 = mae [ : ponto_de_corte] + pai [ponto_de_corte :]
    
    return filho1, filho2

###############################################################################
#                   Funções para mutações                                     #
###############################################################################

def mutacao_cb (individuo):
    """ Realiza a mutação de um gene no problema das caixas binárias
    Args:
        individuo: uma lista representando o problemas das caixas binárias
    
    Return:
        Um valor representando a soma dos genes do indivíduo."""
        
    gene_a_ser_mutado = random.randint (0,len(individuo) -1)
    individuo[gene_a_ser_mutado]= gene_cb()
    return individuo

def mutacao_cnb (individuo, valor_max_caixa):
    """ Realiza a mutação do individuo
    Args:
        individuo: que deve sofrer mutação
        valor_max_caixa: valor máximo que a caixa pode assumir
    
    Returns:
        Um valor representando a soma dos genes do indivíduo."""
        
    gene_a_ser_mutado = random.randint (0,len(individuo) -1)
    individuo[gene_a_ser_mutado]= gene_cnb(valor_max_caixa)
    return individuo

 #atividade 5
    
def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo 
                                
###############################################################################
#                   Funções da atividade 6                                    #
###############################################################################

