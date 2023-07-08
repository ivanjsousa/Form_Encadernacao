
def gerar_conteudo(valor, fm, ab):
    conteudo = f"Projeto: {valor['proj']}\n" \
               f"Cliente: {valor['client']}\n" \
               f"Telefone: {valor['tel']}\n" \
               f"E-mail: {valor['email']}\n" \
               f"Tipo: {', '.join(x for x in fm.Lista_Tipo if valor[x] is True)}.\n" \
               f"Com: {', '.join(x for x in fm.Lista_Acabamento if valor[x] is True)}.\n" \
               f"Impressão: {', '.join(x for x in fm.Lista_Impressao if valor[x] is True)}.\n" \
               f"Papelão da Capa de: {', '.join(x for x in fm.Lista_Papelao if valor[x] is True)}.\n" \
               f"O projeto terá {valor[ab.quantidade]} unidade(s) no formato {valor[ab.formato]}, " \
               f"revestimento em {valor[ab.revestimento]} e papel {valor[ab.guarda]} para a guarda, " \
               f"o miolo com papel {valor[ab.miolo]} e terá {valor[ab.paginas]} páginas."
    return conteudo
