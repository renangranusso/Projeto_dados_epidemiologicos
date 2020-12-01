# Projeto_dados_epidemiologicos
Repositorio criado para commits referente ao projeto de: "Laboratorio de engenharia de software"

## Requisitos para um correto funcionamento / Build do Sistema:

* Instalar todas as Bilbiotecas presentes no requirements.txt (cada versão do sistema acrescenta mais bibliotecas) Atualmente foi acrescentada diversas bibliotecas novas por conta de problemas com sintaxe 
* utilizar do Banco de Dados Mysql
* Criar de uma base de dados dentro do Mysql com o nome: bd_trabalho, ou especificar uma base de dados de sua preferência em: 'mysql+pymysql://root:1234@localhost/__bd_trabalho__' na linha 9 do arquivo __initi.py__.
* Alterar o app.config no arquivo ____init____.py (presente na pasta App) na linha 9 : 
'mysql+pymysql://__root__:__1234__@localhost/bd_trabalho'
alterando o Usuário (__root__) e a senha (__1234__) para os valores correspondentes ao seu Banco de dados.
* Arquivo Controle.py é o arquivo que starta a aplicção.
* Para abrir a primeira pagina, colocar o endereço de IP local seguido por /index.


## 1º Entrega Video: https://youtu.be/xbXQdUL0mbU

#### Descrição Primeira Entrega:
* O codigo foi feito na estrutura de pastas padrão de desenvolvimento do Flask.

## 2º Entrega Vídeo: https://youtu.be/sF-I4BqtJic

#### Descrição Segunda Entrega:
* Foi realizado a navegação completa entre as Páginas do sistema, através de Rotas, e inserido o Primeiro Cadastro de dados e Leitura de dados no Banco de Dados.



## Estrutura da Aplicação

###### \Pasta Raiz: 
* Pasta Raiz da Aplicação

###### Controle.py: 
* Arquivo que controla a aplicação e starta a mesma

* o controle.py importa o modulo App criado para ser o modulo de aplicação do sistema, dentro do controle .py existe apenas um "if __name__ == "MAIN"
que serve para identificar o modulo principal da aplicação e aplicar o contexto em que será executado o modulo de controle da mesma.
no caso a aplicação está sendo executada como debug=True (onde a aplicação no ambiente virtual não precisa ser reinicializada para aplicar as alterações realizadas      no desenvolvimento), e na porta 8080.
  
### Pasta App:
  * Pasta em que ficam os arquivos Front end do sistema e os modulos de configurações

  ###### Pasta templates:
  * Pasta em que ficaram armazaendos os arquivos HTML do sistema
  
  ###### Pasta static:
 * Pasta em que ficaram armazenados os arquivos JavaScript e CSS do sistema
 
  ###### Arquivo __init__.py: 
  
  * Modulo que cria a instância da aplicação flask (app = Flask(_name_)), abaixo da instancia está a importação das rotas do sistema, o mesmo está no fim do arquivo para evitar que o flask entre em um loop inifinito de importação.

 ###### Arquivo routes.py: 
 * Arquivos de rotas do sistema

