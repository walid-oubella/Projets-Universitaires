from biology import *
from json import *

def test_est_base():
    assert est_base('A')
    assert not est_base('Z')
    assert not est_base('')
    print("Test Ok")
    
def test_est_adn():
    assert est_adn("ATGTCAAA")
    assert not est_adn("ATGTZAAJ")
    assert not est_adn(" ")
    print("Test Ok")

def test_arn():
    assert arn("ATGTCAAA") == "ATGUCAAA"
    assert arn("ATTTCAA") == "AUUUCA"
    assert arn("ATGTZAAJ") == None
    print("Test Ok")
               
               
             
def test_arn_to_codons():
    assert arn_to_codons("CGUUAGGGGG") == ["CGU", "UAG", "GGG"]
    assert arn_to_codons("CGUUAGGG") == ["CGU", "UAG", "GGG"]
    assert arn_to_codons("CGUUAGGG") == ["CGU", "UAG"]
    assert arn_to_codons("") == []
    print("Test Ok")

def test_codon_stop():
    assert codon_stop(["CGU", "AAU", "UAA", "GGG", "CGU"],dico) == ["UAA"]
    assert codon_stop(["CGU", "AAU", "GGG", "CGU"],dico) == []
    print("Test Ok")
           
def test_codons_to_aa():
    assert codons_to_aa(["CGU", "AAU", "UAA", "GGG", "CGU"],dico) == ['Arginine', 'Asparagine']
    assert codons_to_aa([],dico) == []
    print("Test Ok")
    
    
    
def test_nextIndice():
    assert nextIndice(["UUU", "AUG", "CGU", "AUG", "UAA", "AAU", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"]),0,['AUG','AAU']) == 1
    assert nextIndice(["UUU", "AUG", "CGU", "AUG", "UAA", "AAU", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"]),2,['AUG','AAU']) == 5
    assert nextIndice(["UUU", "AUG", "CGU", "AUG", "UAA", "AAU", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"]),6,['AUG','AAU']) == 12
    print("Test Ok")

def test_decoupe_sequence():
    assert decoupe_sequence(["UUU", "AUG", "CGU", "AUG", "UAA", "AAU", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],["AUG"], ["AAU"]) == [["UAA"]]
    assert decoupe_sequence(["UUU", "AUG", "CGU", "AUG", "UAA", "AAU", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],["AUG"], ["AAU"]) == []
    print("Test Ok")
    
def test_codons_to_seq_codantes():
    assert codons_to_seq_codantes(["CGU", "UUU", "AUG", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],dico) ==[["CGU", "AUG", "AAU"],["GGG", "CCC", "CGU"]]
    assert not codons_to_seq_codantes(["CGU", "UUU", "AUG", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],dico) == []
    print("test ok")
    
    
def test_codons_to_seq_codantes():
    assert seq_codantes_to_seq_aas([["CGU", "AUG", "AAU"],["GGG", "CCC", "CGU"]],dico) == [["Arginine", "Methionine", "Asparagine"],["Glycine", "Proline", "Arginine"]]
    assert not seq_codantes_to_seq_aas([["CGU", "AUG", "AAU"],["GGG", "CCC", "CGU"]],dico) == ["Arginine", "Methionine", "Asparagine"]
    print("test ok")

def test_adn_encode_molecule():
    assert adn_encode_molecule("CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",dico,["Glycine", "Proline", "Arginine"]) == True
    assert adn_encode_molecule("CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",dico,["Arginine", "Methionine", "Asparagine"]) == True
    assert not adn_encode_molecule("CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",dico,["Methionine", "Asparagine"]) == True
    print("test ok")
    