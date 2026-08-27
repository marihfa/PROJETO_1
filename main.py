None
import random

#dicionario de girias
meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém na internet",
    "VDD": "Abreviação da palavra 'verdade'",
    "BISCOITAR": "Postar fotos ou frases só pra chamar a atenção",
    "HATER": "Pessoa que passa o tempo criticando os outros",
    "VLW": "Abreviação informal para 'valeu'"
}

print("--- Dicionário de Gírias da Internet ---")
print("Escreva uma palavra em MAIÚSCULAS para ver o significado.\n")


for i in range(5):
    palavra = input("Digite a palavra: ")

    if palavra in meme_dict:
        print("->", meme_dict[palavra])
    else:
        print("-> Poxa, ainda não sei essa!")

    print()  

print("Valeu por consultar o dicionário!")
