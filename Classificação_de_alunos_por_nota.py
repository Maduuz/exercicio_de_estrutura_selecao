# Inicializando as listas para armazenar os nomes e notas
alunos = ["João", "Maria", "Lucas", "Ana", "Pedro", "Laura", "Carlos", "Julia", "Marcos"]  # Lista de nomes dos alunos
notas = [8.5, 4.0, 9.0, 7.8, 5.5, 3.0, 6.0, 2.5, 4.5]  # Lista de notas dos alunos

# Calculando a média da turma
media = sum(notas) / len(notas)  # Soma todas as notas e divide pelo número de alunos
print(f"\nA média da turma é: {media:.2f}\n")  # Exibe a média da turma com duas casas decimais

# Classificando cada aluno como Aprovado ou Reprovado
for i in range(9):
    status = "Aprovado" if notas[i] >= 5 else "Reprovado"  # Verifica se a nota é >= 5 para aprovação
    print(f"Aluno: {alunos[i]} - Nota: {notas[i]} - Status: {status}")  # Exibe nome, nota e status