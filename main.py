#importando a biblioteca 
from Bio import SeqIO

#Carregando arquivos 
input_file = "ZIKV.fasta"
output_file = "Filtro_seqenv.fasta"
#declarando o tam minimo para a sequencia 
tam_min = 1501

with open (output_file, "w") as output:
    for record in SeqIO.parse(input_file, "fasta"):
        if len(record.seq) >= tam_min:
            SeqIO.write(record, output, "fasta")

print(f"Sequencias filtradas estão salvas em {output_file}.")