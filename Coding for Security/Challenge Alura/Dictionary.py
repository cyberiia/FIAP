print('\033[1;35m'+" ___      _     _   _         ___ ___   _   ___  "+'\033[m')
print('\033[1;35m'+"| _ ) ___| |___| |_(_)_ __   | __|_ _| /_\ | _ \ "+'\033[m')
print('\033[1;35m'+"| _ \/ _ \ / -_)  _| | '  \  | _| | | / _ \|  _/ "+'\033[m')
print('\033[1;35m'+"|___/\___/_\___|\__|_|_|_|_| |_| |___/_/ \_\_|   "+'\033[m\n')
                                                 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ficha dos Alunos

alunos = {
    88107:{'Aluno': 'André Gabriel Rodrigues',     # Nome completo
           'Idade': '22',                          # Idade
           'Notas': [9, 8, 10, 9, 10, 9, 10, 10]},  # Notas nas 7 disciplinas

    85492:{'Aluno': 'Verônica Ferreira Araújo',
           'Idade': '20',
           'Notas': [7, 9, 9, 8, 10, 8, 10, 9]},

    87447:{'Aluno': 'Danilo da Silva Pacheco',
           'Idade': '21',
           'Notas': [7, 6, 4, 5, 4, 5, 3, 6]},

    82901:{'Aluno': 'Thaynara Gonçalves Santos',
           'Idade': '23',
           'Notas': [5, 6, 4, 5, 4, 5, 3, 6]},

    89335:{'Aluno': 'Victor Hugo Andrade',
           'Idade': '26',
           'Notas': [6, 7, 10, 8, 8, 9, 6, 10]},

    89074:{'Aluno': 'Augusto Marques de Souza',
           'Idade': '19',
           'Notas': [4, 8, 3, 5, 4, 5, 3, 6]},

    88451:{'Aluno': 'Fabiana Bueno Soares',
           'Idade': '22',
           'Notas': [10, 9, 7, 5, 4, 5, 3, 6]},
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Base de Dados

for matricula, dados in alunos.items():
    
    print('\033[36m'+"Nº matrícula:"+'\033[1;m', matricula)
    print('\033[36m'+"Aluno:"+'\033[1;m', dados['Aluno'])
    print('\033[36m'+"Idade:"+'\033[1;m', dados['Idade'])
    print('\033[36m'+"Curso:"+'\033[1;m'+" Defesa Cibernética\n")

    # Notas
    disciplinas = {
        "Cybersecurity & Hacker Skills": dados['Notas'][0],
        "Coding for Security":           dados['Notas'][1],
        "Hardware Hacking":              dados['Notas'][2],
        "IT Governance":                 dados['Notas'][3],
        "Linux Services Applications":   dados['Notas'][4],
        "Network Architect Solutions":   dados['Notas'][5],
        "Security Management":           dados['Notas'][6],
        "Windows Services Applications": dados['Notas'][7],
    }
    for matéria, notas in disciplinas.items():
        print(f"{matéria}: {notas}")

    # Média Final
    média = float((dados['Notas'][0] + dados['Notas'][1] + dados['Notas'][2] + dados['Notas'][3] + dados['Notas'][4] + dados['Notas'][5] + dados['Notas'][6] + dados['Notas'][7]) / 8)
    print(f"\nMédia Final: {média:.1f}")


    # Aprovado ou Reprovado
    if média >= 6:
        print("Situação: " + '\033[32m'+"Aprovado!"+'\033[1;m\n')
    else:
        print("Situação: " + '\033[31m'+"Reprovado!"+'\033[1;m\n')
    
    print('+━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━+\n')
