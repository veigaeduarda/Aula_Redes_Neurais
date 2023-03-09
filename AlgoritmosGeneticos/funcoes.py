def funcao_objetivo_cb (individuo):
    """ Computa a função objetivo no problema das caixas binárias.
    
    Args:
        n: número de genes dos indivíduo.
    
    Return:
        Um valor representando a soma dos genes do individuo.
    """
    
    return sum (individuo)

