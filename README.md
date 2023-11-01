# CALCULADORA SIMPLES COM PYSIMPLEGUI

Um projeto simples apresentado num reels publicado no instagram @cvti.novaiguacu.
Visava apresentar de maneira simplificada um recurso para construção de interfaces graficas produzido em python, para informações profundas a respeito da biblioteca, leia a documentação oficial: https://www.pysimplegui.org/en/latest/ 

# Sobre o projeto

O visual do PySimpleGUI é programado de maneira a tabela, ou seja, como uma grade. O elemento que vier na possição (0,0) da grade irá aparecer na posição (0,0) na tela. Por exemplo: 

![image](https://github.com/jo4o0rn3ll4s/Calculadora_Simples_com_PySimpleGUI/assets/65920201/cb60688e-ddbe-461b-9289-bc0a0b8f9848)

Note na linha 9 que o primeiro e unico elemento é: sg.text('Calculadora em PYTHON')
Quando gerado a janela, o mesmo aparece na mesma posição.

![image](https://github.com/jo4o0rn3ll4s/Calculadora_Simples_com_PySimpleGUI/assets/65920201/047f23ec-46ee-4141-87b8-1ff6c5da7a41)

Da mesma forma os outros elementos obedecem a mesma regra de posicionamento.


# Sobre a funcionabilidade

O PySimpleGUI funciona sobre eventos, ou seja, a cada clique na janela, um evento é disparado. No caso do nosso programa, utilizamos 4 botões para disparar 4 eventos possíveis.
Cada botão possui sua 'Key=', com ela dizemos que "código" o PySimpleGUI deve disparar quando aquele botão for clicado. Depois, dentro do laço infinito de execução da janela, verificamos se a variavel 'event' é igual ao 'código do evento x', sendo x um evento qualquer.
No nosso programa, a titulo de exemplo, temos em um botão 'key = soma', com isso, quando o botão for apertado, temos a palavra 'soma' atrelado a variavel 'event'. Dentro do loop, verificamos se o 'event == soma' e então realizamos a tarefa desejada para essa escolha, neste caso, a soma dos valores nos campos 'sg.input'.

![image](https://github.com/jo4o0rn3ll4s/Calculadora_Simples_com_PySimpleGUI/assets/65920201/a23c0be8-94e9-43ca-adb2-40c9d3719296)

# Considerações finais

Obrigado por se interessar nesse simples conteudo, e espero que tenha gostado. Aproveite a biblioteca do PySimpleGUI pois ela é muito versatil.
Caso deseje baixar o programa utilizado no video, o mesmo está disponivel em 'src/main.py'.
