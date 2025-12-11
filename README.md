# One Piece Logbook Language (OPL)

Este documento é a documentação completa e o guia de execução para a linguagem de programação esotérica OPL, criada como um projeto para a disciplina de Paradigmas de Programação.

## 1. Visão Geral

A OPL - One Piece Language é uma linguagem esotérica de propósito geral, apresentada como uma narrativa temática baseada no universo do anime One Piece. Nela os programas são escritos como trechos de um diário de bordo, que apresentam comandos ocultos dentro do código “disfarçados” como uma ação dentro da tripulação.
Em síntese, a lógica do programa é: o texto pode parecer uma história comum, mas palavras-chave escondidas são comandos formais interpretados pelo “Den Den Mushi Virtual” (máquina abstrata da linguagem).
Basicamente, ela aborda o código como uma jornada, onde o programador é o Capitão e o programa é um Diário de Bordo. A OPL trabalha com uma fita de inteiros, chamada de Baú do Tesouro, onde cada posição do baú é uma célula inteira e o Lápis do Navegador é um ponteiro que representa o índice do baú atual.


## 2. Configuração e Execução

Para utilizar a OPL, é necessário ter o Python 3.11 instalado. O projeto consiste em um interpretador(`opl_interpreter.py`) que interpreta um código OPL (`.opl`) e seus comandos, formando uma pilha de comandos para o terminal para ser executado.

**Comando Genérico para Tradução:**

Para traduzir qualquer programa, utilize o seguinte comando no terminal, na pasta raiz do projeto:

```bash
python opl_interpreter.py nome_do_arquivo.opl
```

O interpretador irá ler o código contido no arquivo e executará, terá sua saída diretamente pelo terminal

## 3. Sintaxe e Comandos

### 3.1 Estrutura do Código

Todo código OPL é iniciado pela expressão `Tripulação reunida !` e finalizado pela expressão `Fim da Jornada.`.

**Sintaxe:**

```opl
Tripulação reunida !
    // Comandos OPL.
Fim da Jornada.
```

### 3.2 Manipulação do Tesouro

OPL conta com uma lista de 1000 elementos de "baú do tesouro", cada um armazendo um inteiro (inicialmente 0).
Para atribuir diretamente um valor a célula usa-se o comando "Mudar recompensa para " que é case insensitive.

**Sintaxe:**
```
Mudar recompensa para  <valor>
```

**Exemplo:**

```opl
Mudar recompensa para 10
```

**Operações:**

"Aumentar recompensa" (case insensitive) soma 1 ao valor do tesouro.
"Pagar a Nami" (case insensitive) subtrai 1 do valor do tesouro.
"Gomu Gomu no" (case sensitiva) multiplica o valor do tesouro por 2.
"Santoryuu" (case sensitive) divide o valor do tesouro por 2.
"Usar Rumble Ball" (case sensitive) zera o valor do tesouro.


**Sintaxe:**
```
Aumentar recompensa 
Pagar Nami
Gomu Gomu no
Santoryuu
Usar Rumble Ball
```

**Exemplo:**

```opl
Mudar recompensa para 10
Aumentar recompensa 
Pagar Nami
Gomu Gomu no
Santoryuu
Usar Rumble Ball
```
###3.3 Avançar nas Células
Para avançar nas células dos baús de tesouro existem dois comando: para avançar e voltar na lista

**Avançar na lista(Seguir Log Pose)**

Avança uma "casa" no mapa(lista)

**Sintaxe:**
```
Seguir Log Pose
```

**Exemplo:**

```opl
Seguir Log Pose
```

**Voltar na lista(Voltar para resgatar)**
Volta para o elemento anterior da lista


**Sintaxe:**
```
Voltar para resgatar 
```

**Exemplo:**

```opl
Seguir Log Pose
Seguir Log Pose
Voltar para resgatar
```

### 3.4 Entrada e Saída de Dados

Em OPL a entrada e saída de dados se dá por 4 comandos principais que permitem imprimir coisas na tela e o usuário entrar com dados

**Saída de Dados **

"Registrar Entrada no Diário:" printa strings na tela.

**Sintaxe:**
```
Registrar Entrada no Diário: <expressao>
```

**Exemplo:**

```opl
Registrar Entrada no Diário: We are on the Cruise. We are!
```

"Gritar nível de poder" imprime na tela o valor do tesouro atual.

**Sintaxe:**
```
Gritar nível de poder
```

**Exemplo:**

```opl
Mudar recompensa para 15
Gritar nível de poder
```

"Ler Poneglyph" imprime o caracter da baú do tesouro.
### 3.5 Estruturas de Controle

**Sintaxe:**
```
Ler Poneglyph 
```

**Exemplo:**

```opl
Ler Poneglyph 
```

"Den Den Mushi tocou" atribui o valor inserido pelo usuário ao tesouro.

**Sintaxe:**
```
Den Den Mushi tocou 
```

**Exemplo:**

```opl
Den Den Mushi tocou 
```

### 3.5 Estrutura Condicional
OPL possui estrutura condicional que permite verificar se o valor do tesouro é maior, menor ou igual a um número

**Sintaxe:**
```
Se o Tesouro Atual for Maior/Menor/Igual que/a <valor> {
      //Código
}
```

**Exemplo:**

```opl
Mudar recompensa para 25
Se o Tesouro Atual for Maior que 10 {
     Registrar Entrada no Diário: Tesouro é maior que 10
     Se o Tesouro Atual for Menor que 20 {
           Registrar Entrada no Diário: E menor que 20
     }
}
```
### 3.6 Estrutura de Repetição 
OPL possui estrutura de repetição que repete um bloco de código até o valor do tesouro seja igual a 0

**Sintaxe:**
```
Enquanto houver esperança... {
     //Código 
}
```

**Exemplo:**

```opl
Mudar recompensa para 10
Enquanto houver esperança... {
     Registrar Entrada no Diário: Hello World!
     Pagar a Nami
}
```




