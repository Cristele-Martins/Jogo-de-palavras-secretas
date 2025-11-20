import random
palavras = ["python", "backend", "servidor","api", "django", "codigo"]
palavra_secreta = random.choice(palavras)
progresso = ["_"] * len(palavra_secreta)

tentativas = 6
letras_tentadas = set()

print("jogo a palavra_secreta!")
print("Adivinhe a palavra:")
print(" ".join(progresso))

while tentativas > 0 and "_" in progresso:
    letra = input("\nDigite uma letra: ").lower()
    if letra in letras_tentadas:
        print("Você ja tento essa letra!")
        continue
    letras_tentadas.add(letra)
    if letra in palavra_secreta:
        print("Boa! A letra está na palavra.")
        for i, I in enumerate(palavra_secreta):
            if I == letra: 
                progresso[i] = letra
    else:
        tentativas -= 1
        print(f"letra errada! Tentativas restantes: {tentativas}")
    print(" ".join(progresso))
if "_" not in progresso:
    print("\nparabens! Você adivinhou a palavra:", palavra_secreta)
else:
    print("\nFim de jogo! A palavra era :", palavra_secreta)