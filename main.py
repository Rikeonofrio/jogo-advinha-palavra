import random
 
name = input(str('Qual é o seu nome ?'))
print(f"Boa sorte {name}")

palvaras = ['ovo', 'python', 'jogos', 'advogados', 'faculdade', 'escola', 'cidades',
'restaurantes', 'jantar']

w = random.choice(palvaras)
turns = 6
guesses = ''


while turns > 0:
    failed = 0
    
    for char in w:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win")
        print(f"A palavra é {w}")
        break

    guess = input("adivinhe a plavara:")
    guesses += guess

    if guess not in w:
        turns -= 1
        print("Errou")
        print(f"voce tem mais {turns} chances para palpites")
        if turns == 0:
            print("voce perdeu")
            

    




    
