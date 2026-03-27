import random

inicio = [
    "Dessa forma,",
    "No entanto,",
    "Por outro lado,",
    "Assim sendo,",
    "Em linhas gerais,",
    "Considerando o cenário atual,",
    "Do ponto de vista estratégico,"
]

sujeito = [
    "a complexidade dos processos",
    "a necessidade de alinhamento",
    "o planejamento estratégico",
    "a otimização dos recursos",
    "a governança corporativa",
    "o fluxo de trabalho contínuo",
    "a integração entre as áreas"
]

verbo = [
    "exige",
    "possibilita",
    "impulsiona",
    "impacta diretamente",
    "potencializa",
    "garante",
    "viabiliza"
]

complemento = [
    "uma melhor tomada de decisão.",
    "resultados mais assertivos.",
    "maior eficiência operacional.",
    "a entrega contínua de valor.",
    "um ganho significativo de produtividade.",
    "a redução de riscos no processo.",
    "a melhoria contínua dos indicadores."
]

def gerar_frase():
    return f"{random.choice(inicio)} {random.choice(sujeito)} {random.choice(verbo)} {random.choice(complemento)}"

def gerar_texto(qtd_frases=5):
    return " ".join(gerar_frase() for _ in range(qtd_frases))

if __name__ == "__main__":
    print(gerar_texto(5))
