# Projeto_dados_epidemiologicos
Repositorio criado para commits referente ao projeto de: "Laboratorio de engenharia de software"

1º Entrega Video: https://youtu.be/xbXQdUL0mbU

Descrição Primeira Entrega:

O codigo foi feito na estrutura de pastas padrão de desenvolvimento do Flask:

\Pasta Raiz:

Controle.py: Arquivo que controla a aplicação e starta a mesma

*o controle.py importa o modulo App criado para ser o modulo de aplicação do sistema, dentro do controle .py existe apenas um "if __name__ == "MAIN"
que serve para identificar o modulo principal da aplicação e aplicar o contexto em que será executado o modulo de controle da mesma.
no caso a aplicação está sendo executada como debug=True (onde a aplicação no ambiente virtual não precisa ser reinicializada para aplicar as alterações realizadas      no desenvolvimento), e na porta 8080.
  
Pasta App:

  Pasta templates
  
  *Pasta em que ficaram armazaendos os arquivos HTML do sistema
  
  Pasta static
  
 *Pasta em que ficaram armazenados os arquivos JavaScript e CSS do sistema
 
  Arquivo: __init__.py: Modulo que cria a instância da aplicação flask (app = Flask(_name_)), abaixo da instancia está a importação das rotas do sistema, o mesmo está no fim do arquivo para evitar que o flask entre em um loop inifinito de importação.

 Arquivo: routes.py: importa a instancia do flask que esta em APP e apartir do APP importado instaciamos as rotas do sistema (@app.route('/')), Dentro do arquivo a função"HOME", define qual será a primeira pagina html a ser exibida pela aplicação

\projeto-python: Pasta criada pelo VirtualEnv para armazenar os arquivos do ambiente virtual de desenvolvimento.
