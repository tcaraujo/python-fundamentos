# palavra ="essa frase é curta"
# palavra.lower()
# vogal = palavra.count('a') + palavra.count('e')
# + palavra.count('i')
# + palavra.count('o')
# + palavra.count('u')

# consoante =  vogal - len(palavra)
# variavel = " "
# palavra.cont('essa frase é curta')
# str.cont.vogal
# vogal = ('a, e, i, o, u')
# retorno = consoante - variavel

# len(palavra)
# vogal = "aeiou"
# consoante "b:z"
# lower.(palavra)
# upper.(palavra)

palavra = input()
palavra = palavra.lower()
# contagem = 0
# contagem = contagem+palavra.count('a')
# contagem += palavra.count('e')
# contagem += palavra.count('i')
# contagem += palavra.count('o')
# contagem += palavra.count('u')
# total_caracteres = len(palavra)
# espacos = palavra.count(" ")

# consoantes = total_caracteres - contagem - espacos
contagem = sum([palavra.count(x) for x in 'aeiou'])
consoantes = len(palavra) - contagem - palavra.count(" ")

print("Contagem de Vogais: {}".format(contagem))
print("Contagem de Consoantes: {}".format(consoantes))
