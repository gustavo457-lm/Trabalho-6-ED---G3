from Node import Node

class HashTable:
    def __init__(self, M):
        self.M = M
        self.N = 0
        self.table = [None]*M
        self.quant = [0]*M

    def hashFirstL(self, key):
        h = 0
        h = ord(key[0]) - ord('A')
        return h

    def hash_nativo(self, key):
        return hash(key) % self.M

    def _hash(self, key):
        h = 0
        for c in key:
            h = (31*h + ord(c)) % self.M
        return h
    
    def insert(self, key, indHash):
        novo = Node(key)
        if indHash == 1:
            i = self.hashFirstL(key)
        if indHash == 2:
            i = self.hash_nativo(key)
        if indHash == 3:
            i = self._hash(key)
        if (self.table[i] != None):
            aux = self.table[i]
            self.table[i] = novo
            self.table[i].prox = aux
        else:
            self.table[i] = novo
        self.N+=1
        self.quant[i] += 1

    def search(self, key, indHash):
        if self.N > 0:
            if indHash == 1:
                i = self.hashFirstL(key)
            if indHash == 2:
                i = self.hash_nativo(key)
            if indHash == 3:
                i = self._hash(key)
            atual = self.table[i]
            while(atual != None):
                if(atual.key == key):
                    return atual
                else:
                    atual = atual.prox
        return None

    def remove(self, key, indHash):
        if self.N > 0:
            if indHash == 1:
                i = self.hashFirstL(key)
            if indHash == 2:
                i = self.hash_nativo(key)
            if indHash == 3:
                i = self._hash(key)
            atual = self.table[i]
            anterior = self.table[i]
            while(atual != None):
                if(atual.key == key):
                    if (atual == anterior):
                        self.table[i] = atual.prox
                    else:
                        anterior.prox = atual.prox
                    self.N -=1
                    self.quant[i] -=1
                    return True
                else:
                    anterior = atual
                    atual = atual.prox
            return False
    
                  