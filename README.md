# Gerador de Tabelas de Fichas

Conjunto de funções pra gerar um HTML com diversas fichas, HTML esse que é
feito pra ser convertido pra PDF, ajudando a imprimir essas fichas.
Configurando os parâmetros das funções corretamente, é possível customizar
quantas fichas por coluna cada página vai ter, quantas colunas, se vai ter
imagens cada uma das fichas e afins.

Uma pequena ferramenta que fiz pra ajudar uma amiga num projeto pessoal. Esse
script é feito pra ser importado como uma bilioteca e usar as funções que ele
expôe, mas é possível editá-lo pra user de script ou coisa assim.

<p align="center">
    <img src="docs/demo.png" alt="demo">
</p>

## Test Drive

Clone o repositório na sua máquina e rode o script `data_to_html.py`. Ele
deve usar o template de HTML em `template/base.html` pra gerar um arquivo
`index.output.html`.

> [!INFO]
> Eu usei o `mock/base.html` pra me guiar, você pode usar ele pra entender como
> código final vai parecer, mais ou menos.

## Customizando

```py
def gerar_html_e_escrever(
    matriz,         # Lista de números, cada card terá 4
    output,         # Nome do arquivo final
    template_html,  # Template pra gerar o HTML, olhe o arquivo `template/base.html` antes!
    imagem,         # URL da imagem de cada ficha, pode ser omitido se não quizer imagem
    descricao,      # Pequeno texto inferior que cada ficha pode ter
    font_tamanho,   # Tamanho da fonte, use unidades CSS como `9pt` ou `1.5rem`
):
```

Alguns detalhes: se a imagem for omitida, a página terá um espaço em branco
onde a imagem ficaria; e se a matríz não tiver um tamanho que seja múltiplo de
quatro, o prograva vai simplesmente ignorar os números finais -- por exemplo:
se você passar uma lista com 22 números ele vai gerar 4 cards e vai ignorar
os últimos 2 porque não conseguir completar um novo card.

Nada te impede de editar o CSS dentro de `template/base.html` também se quiser
avançar na customização, e ainda pode editar a parte lógica desse arquivo de
template se você tiver coragem.
