# TelegramBot

Este projeto consiste na criação de um bot para o Telegram cuja funcionalidade é mandar sinopses da One Piece Wiki para o usuário. Para isso, foi necessário o uso de diferentes bibliotecas para que suas funções se complementassem.

BeautifulSoup: 
Responsável por encontrar e escrever nos arquivos os resumos dos arcos e links de cada página.

Selenium: 
Responsável por abrir o navegador e fornecer cliques para as páginas seguintes.

Requests: 
Responsável pelas requisições HTTP's das páginas.

Telepot: 
Responsável para trabalhar com a API do telegram.

Arquivos:

Sinopses.py:
Foi a ideia primária do projeto, automatiza cliques e busca a sinopse de cada arco da obra.

Funcoes.py:
Contém as funções que foram inicialmente utilizadas no arquivo de sinopses, facilitando reaproveitamento de código nos outros arquivos.

Encontrarlink.py:
Aproveita a ideia do arquivo de sinopses e , em vez de escrever os resumos de cada arco, escreve os links.

Links.txt:
Arquivo que contém os links de todos os arcos, serve para que o arquivo do bot possa acessar o link do arco especificado pelo usuário através do número do arco pedido.


