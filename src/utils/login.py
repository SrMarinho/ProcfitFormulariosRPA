def generatePossiblesLogins(nome_completo: str) -> list:
    preposicoes = {'DA', 'DE', 'DO', 'DAS', 'DOS', 'E'}
    
    # Processa o nome: maiúsculas, divide e remove preposições
    partes = [
        parte for parte in nome_completo.upper().strip().split()
        if parte not in preposicoes
    ]
    
    if len(partes) < 2:
        raise ValueError('Nome incompleto. Não foi possível gerar logins.')
    
    primeiro_nome = partes[0]
    sobrenomes_relevantes = partes[1:]  # Todos os sobrenomes (exceto preposições)
    
    # Gera logins no padrão NOME.SOBRENOME, em ordem de relevância
    logins = []
    for sobrenome in sobrenomes_relevantes:
        logins.append(f"{primeiro_nome}.{sobrenome}")
    
    return logins