'''
Para este desafio, vamos criar um lista com os nomes de três cidades.

Requisão:

- Entra do usuário pesquisando a cidade.

Validar:
- Se a cidade informada está presente

Retorno:
- "A cidade está na lista de cidades"
- "A cidade não está na lista de cidades"

OBS: Você não pode utilizar list[]


'''

#Criando uma tuple
cidades = ('São Paulo', 'Rio De Janeiro', 'Minas Gerais')

#Entrada do usuário

cidade = input('Informe a cidade desejada: ').title()


#Condição para vericar cidade
if cidade in cidades:
    #saida
    print('A cidade está na lista de cidades')
else:
    print('A cidade não esta na lista de cidades')
