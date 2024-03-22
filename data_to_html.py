import random as r


def converter_para_matriz(lista_num, colunas_pp=2, fichas_pc=3, celulas_pf=4):
    """Converte uma lista de números para uma matríz compatível com as funções
    que convertem esse tipo de matríz num arquivo HTML convertível para PDF.
    É importante que as regras de como esses números já sejam pre definidas
    direto na variável lista_num, isso só vai mudar as coisas de lugar e criar
    sub listas, nenhuma verificação será tomada!

    :param list[int] lista_num:
        Lista com os valores aleatórios de cada célula pra cada ficha.
    :param int colunas_pp:
        Variável de configuração, quantas colunas cada página (colunas por
        página) deve ter no HTML final. O padrão é 2.
    :param int fichas_pc:
        Variável de configuração, quantas fichas cada coluna (fichar por
        coluna) deve ter em cada página. O padrão é 3.
    :param int celulas_pf:
        Variável de configuração, quantas células cada ficha (células por
        ficha) deve ter no HTML final. O padrão é 4.

    :returns list[list[list[tuple[int]]]]:
        Uma matríz multidimensional; Lista de páginas, que são listas de
        fichas, que são lista de células que são tuplas de números.
    """
    celulas_pp = colunas_pp * fichas_pc * celulas_pf
    total_paginas = (len(lista_num) + celulas_pp - 1) // celulas_pp
    resultado = []

    print(total_paginas)

    for pagina in range(total_paginas):
        pagina_atual = []

        for coluna in range(colunas_pp):
            coluna_atual = []

            for ficha in range(fichas_pc):
                ficha_atual = []

                for celula in range(celulas_pf):
                    indice = pagina * celulas_pp + coluna * fichas_pc\
                        * celulas_pf + ficha * celulas_pf + celula

                    if indice < len(lista_num):
                        ficha_atual.append(indice)
                    else:
                        ficha_atual.append(None)

                coluna_atual.append(tuple(ficha_atual))

            pagina_atual.append(coluna_atual)

        resultado.append(pagina_atual)

    return resultado


if __name__ == "__main__":
    matriz = converter_para_matriz([r.randint(1000, 9999)
                                    for _ in range(15 * 4)])
    print(matriz)
