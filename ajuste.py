
from Bio import SeqIO

# Defina os arquivos de entrada e saída
input_fasta = "output.fasta"  # Substitua pelo nome do seu arquivo
output_fasta = "filtro_seq.fasta"

# Define o tamanho mínimo da sequência
min_length = 8000

# Filtra as sequências e salva no novo arquivo
with open(output_fasta, "w") as output_handle:
    filtered_records = (record for record in SeqIO.parse(input_fasta, "fasta") if len(record.seq) >= min_length)
    SeqIO.write(filtered_records, output_handle, "fasta")

print(f"Filtragem concluída! Sequências salvas em '{output_fasta}'.")
