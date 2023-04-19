from json import *

adn = ['A','T','G','C']
def est_base(c):
    return c in adn
def est_adn(s):
    for c in s:
        if not est_base(c):
            return False
    return True


def arn(adn):
    t = []
    arn = ''
    if not est_adn(adn):
        return None
    
    for c in adn:
        t.append(c)
        
    for i,c in enumerate(t):
        if c == 'T':
            t[i] ='U'
            
    for c in t:
        arn += c
        
    return arn

def arn_to_codons(arn):
    t = []
    codon = ''
    if len(arn)%3 != 0:
        j = len(arn)%3
        arn = arn[0 : len(arn)-j]
        
    for i in range(len(arn)//3):
        for i in range(3):
            codon += arn[i]
        t.append(codon)
        codon = ''
        arn = arn[3::]
        
    return t

def load_dico_codons_aa(filename):
    fichier = open(filename,"r")
    json = fichier.read()
    fichier.close()
    dico = loads(json)
    return dico

def codon_stop(codons,dico):
    t = []
    for v in codons:
        if v not in dico.keys():
            t.append(v)
    return t

def codons_stop_correct(dico):
    stop = []
    bases = "AUGC"
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            k = 0
            while k < 4:
                if bases[i] + bases[j] + bases[k] not in dico:
                    stop.append(bases[i] + bases[j] + bases[k])
                k += 1
            j += 1
        i += 1
    return stop


def codons_to_aa(codons, dico):
    t = []
    stop = codon_stop(codons,dico)
    
    for v in codons:
        if v in stop:
            return t
        if v in dico.keys():
            t.append(dico[v])
    return t
    
def nextIndice(tab, ind, elements):
    for i in range(ind,len(tab)):
        if tab[i] in elements:
            return ind
        ind += 1
    return len(tab)



def decoupe_sequence(seq,start,stop):
    tab = []
    ind_debut = nextIndice(seq,0,start)
    ind_fin = nextIndice(seq,0,stop)
    while ind_debut < len(seq):
        tabtmp = []
        for i in range(ind_debut,ind_fin-1):
            tabtmp.append(seq[i+1])
        tab.append(tabtmp)
        ind_debut = nextIndice(seq,ind_fin,start)
        ind_fin = nextIndice(seq,ind_debut,stop)
    
    return tab
    

def codons_to_seq_codantes(seq_codons,dico):
    start = ['AUG']
    stop = codons_stop_correct(dico)
    return decoupe_sequence(seq_codons,start,stop)


def seq_codantes_to_seq_aas(seq_codons,dico):
    tab = []
    seqco = codons_to_seq_codantes(seq_codons,dico)
    for t in seqco:
        tab.append(codons_to_aa(t,dico))
    return tab

def adn_encode_molecule(br,dico,sq_aa):
    ar = arn(br)
    codons = arn_to_codons(ar)
    seq_aa = seq_codantes_to_seq_aas(codons,dico)
    for t in seq_aa:
        return sq_aa in seq_aa
