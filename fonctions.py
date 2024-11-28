
def addition(x, y):
    res = x+y
    return res


def soustraction(x, y):
    res = x-y
    return res


def noms_binome():
    """
    Affiche les noms des membres du binôme
    Attention, chacun écrit la ligne pour afficher son nom
    """


a = 2
b = 1

print(f"La somme de {a} et {b} vaut {addition(a, b)}")
print(f"La différence de {a} et {b} vaut {soustraction(a, b)}")

noms_binome()
