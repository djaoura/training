def calculer_factorielle(n):
    if n < 0:
        return "La factorielle n'est pas définie pour les nombres négatifs."
    elif n == 0 or n == 1:
        return 1
    else:
        factorielle = 1
        for i in range(2, n + 1):
            factorielle *= i
        return factorielle

# Demander à l'utilisateur d'entrer un nombre
nombre = int(input("Entrez un nombre entier positif : "))

# Calculer et afficher la factorielle
resultat = calculer_factorielle(nombre)
print(f"La factorielle de {nombre} est {resultat}")