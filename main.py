from pyscript import document

# Tables pour afficher les éléments
S = document.getElementById("stack")
Q = document.getElementById("queue")
e = document.getElementById("e")

# Fonctions de manipulation des données
def empty(S):
    return S.childElementCount == 0

def insert(S, i, x):
    S.insertCell(i).append(x)

def push(S, x):
    insert(S, -1, x)

def queue(S, x):
    insert(S, 0, x)

def stacktop(S):
    return int(S.children[S.childElementCount - 1].textContent)

def pop(S):
    x = stacktop(S)
    S.deleteCell(S.childElementCount - 1)
    return x

def small_step():
    if empty(e):
        push(e, pop(Q))
    elif not empty(S) and stacktop(e) < stacktop(S):
        queue(Q, pop(S))
    else:
        push(S, pop(e))

def start(lst):
    while not empty(S): pop(S)
    while not empty(Q): pop(Q)
    for x in lst:
        push(Q, x)
