<h1>Desafio 21 - Verificação de Cidade em uma Tupla</h1>

<p>Este código tem como objetivo criar uma tupla de cidades, solicitar ao usuário que informe uma cidade desejada e verificar se a cidade está presente na tupla.</p>

<ol>
<h2><li>Criação da Tupla:</li></h2>

<ul>
<li>Inicia a variável cidadescom uma tupla contendo nomes de cidades.</li>

    cidades = ('São Paulo', 'Rio De Janeiro', 'Minas Gerais')
</ul>

<h2><li>Entrada do Usuário:</li></h2>

<ul>
<li>Utilize a função inputpara permitir que o usuário insira o nome da cidade desejada.</li>
<li>Converta a entrada para o formato do título ( title()) para garantir consistência na comparação.</li>

    cidade = input('Informe a cidade desejada: ').title()
</ul>

<h2><li>Condição de Verificação:</li></h2>

<ul>
<li>Utilize uma estrutura condicional ( if) para verificar se a cidade informada pelo usuário está presente na tupla cidades.</li>
<li>Se a cidade estiver na tupla, imprime 'A cidade está na lista de cidades'.</li>
<li>Caso contrário, imprime 'A cidade não está na lista de cidades'.
Pitão
</li>

    if cidade in cidades:
        print('A cidade está na lista de cidades')
    else:
        print('A cidade não está na lista de cidades')
</ul>
</ol>

<h2>Mensagens Personalizadas:</h2>
<li><b>Presente na Lista:</b> Se a cidade informada estiver na tupla.</li>
<li><b>Ausente na Lista:</b> Se a cidade informada não estiver na tupla.</li>

<h2>Interatividade:</h2>
<p>
O código fornece uma experiência interativa para verificar se a cidade desejada pelo usuário está presente na lista de cidades.
</p>

<h2>Conclusão: </h2>
<p>
Ao executar este código, o usuário receberá uma mensagem abaixo se a cidade desejada estiver ou não na lista de cidades especificadas na tupla. Isso demonstra o uso de tuplas e estruturas condicionais em Python.
</p>