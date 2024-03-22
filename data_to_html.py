import random as r
import jinja2 as j2

TEMPLATE_HTML_PADRAO = "template/base.html"
IMAGEM_PADRAO = "https://i.pinimg.com/originals/7a/7e/a1/7a7ea1d7fbededa69475b\
                26829077e0c.png".replace(" ", "")
DESCRICAO_PADRAO = "Lorem ipsum, dolor sit amet consectetur adipisicing elit."
OUTPUT_PADRAO = "index.output.html"
FONT_TAMANHO_PADRAO = "9.125pt"


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
                        ficha_atual.append(lista_num[indice])
                    else:
                        ficha_atual.append(None)

                celulas_ficha = tuple(ficha_atual)

                coluna_atual.append((None, None, None, None)
                                    if None in celulas_ficha
                                    else celulas_ficha)

            pagina_atual.append(coluna_atual)

        resultado.append(pagina_atual)

    return resultado


def gerar_html(matriz, template_html=TEMPLATE_HTML_PADRAO,
               imagem=IMAGEM_PADRAO, descricao=DESCRICAO_PADRAO,
               font_tamanho=FONT_TAMANHO_PADRAO):
    f"""Dado um template, essa função vai gerar o HTML baseado nos dados da
    matriz de fichas nos parâmetros. As dimensões de cada página será definida
    pelo formato da matríz, por exemplo, quantas sublistas ela vai ter vai
    determinar a quantidade de páginas no total, as sub sub listas a quantidade
    de colunas, e assim por diante.

    :param list[list[list[tuple[int]]]] matriz:
        Uma matríz multidimensional; Lista de páginas, que são listas de
        fichas, que são lista de células que são tuplas de números.
    :param str template_html:
        Caminho para o arquivo de template HTML, precisa ser um arquivo
        compatível com o Jinja2. O padrão é {TEMPLATE_HTML_PADRAO}.
    :param str | None imagem:
        Imagem para o banner de cada ficha, se for uma string vazia ou nulo,
        a página vai só renderizar um espaço em branco onde o a imagem ficaria.
        O padrão é {IMAGEM_PADRAO}.
    :param str descricao:
        Pequeno texto que vai ficar em baixo de cada ficha, por padrão é apenas
        um Lorem Ipsum para ocupar espaço.
    :param str font_tamanho:
        Tamanho de fonte que o CSS irá utilizar para determinar o tamanho de
        tudo, não só as fontes. É importante que essa string seja compatível
        com as unidades de medida do CSS. Por padrão é {FONT_TAMANHO_PADRAO}.

    Um adendo, caso você esteja usando dimensões customizadas para o formato
    da variável matriz, então você talvez queira mudar o tamanho da fonte,
    quantidade de colunas, etc. pro conteúdo caber nas páginas.

    :returns str:
        HTML (não minificado) gerado apartir dos dados providos.
    """
    with open(template_html, "r") as th:
        jinja = j2.Template(th.read())

        return jinja.render({
            "font_tamanho": font_tamanho,
            "matriz": matriz,
            "imagem": imagem or None,
            "descricao": descricao
        })


def gerar_html_e_escrever(matriz, output, template_html=TEMPLATE_HTML_PADRAO,
                          imagem=IMAGEM_PADRAO, descricao=DESCRICAO_PADRAO):
    f"""Essa função funciona em volta da função 'gerar_html()', a diferença é
    que essa usa o output da anterior pra escrever o HTML gerado num arquivo
    especificado pelo usuário.

    :param list[list[list[tuple[int]]]] matriz:
        Uma matríz multidimensional; Lista de páginas, que são listas de
        fichas, que são lista de células que são tuplas de números.
    :param str template_html:
        Caminho para o arquivo de template HTML, precisa ser um arquivo
        compatível com o Jinja2. O padrão é {TEMPLATE_HTML_PADRAO}.
    :param str | None imagem:
        Imagem para o banner de cada ficha, se for uma string vazia ou nulo,
        a página vai só renderizar um espaço em branco onde o a imagem ficaria.
        O padrão é {IMAGEM_PADRAO}.
    :param str descricao:
        Pequeno texto que vai ficar em baixo de cada ficha, por padrão é apenas
        um Lorem Ipsum para ocupar espaço.
    :param str font_tamanho:
        Tamanho de fonte que o CSS irá utilizar para determinar o tamanho de
        tudo, não só as fontes. É importante que essa string seja compatível
        com as unidades de medida do CSS. Por padrão é {FONT_TAMANHO_PADRAO}.
    """
    resultado = gerar_html(matriz, template_html, imagem, descricao)

    with open(output, "w") as op:
        op.write(resultado)


if __name__ == "__main__":
    matriz = converter_para_matriz([r.randint(1000, 9999)
                                    for _ in range(5000 * 4)])
    gerar_html_e_escrever(matriz, OUTPUT_PADRAO)
