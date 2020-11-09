# Projeto_dados_epidemiologicos
Repositorio criado para commits referente ao projeto de: "Laboratorio de engenharia de software"

## Requisitos para um correto funcionamento / Build do Sistema:

* Instalar todas as Bilbiotecas presentes no requirements.txt (cada versão do sistema acrescenta mais bibliotecas) Atualmente foi acrescentada diversas bibliotecas novas por conta de problemas com sintaxe 
* utilizar do Banco de Dados Mysql
* Criação de um banco de dados dentro do Mysql com o nome: bd_trabalho (ou alterar o nome do banco para o de sua preferência no arquivo ____init____.py)
* Alterar o app.config no arquivo ____init____.py na linha 9 : 'mysql+pymysql://root:1234@localhost/bd_trabalho' alterando o Usuário (root) e a senha (1234) para os valores correspondentes ao seu Banco de dados.


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

