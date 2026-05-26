tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# ============================================================
# 1. ENTRADA DE DADOS
# ============================================================


while True:
    try:
        quantidade = int(input("Insira a quantidade de eventos: "))
        if quantidade > 0:
            break
        else:
            print("A quantidade de eventos deve ser maior que zero.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


for i in range(quantidade):
    print(f"\n--- Evento {i + 1} ---")

    tipo = input("Tipo (ex: desmatamento, queimadas): ").strip()
    pais = input("País: ").strip()
    regiao = input("Região: ").strip()
    cidade = input("Cidade: ").strip()


    while True:
        try:
            area = float(input("Área afetada (km²): "))
            if area > 0:
                break
            else:
                print("A área deve ser maior que zero.")
        except ValueError:
            print("Por favor, insira um número válido para a área.")


    while True:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))
            if 1 <= intensidade <= 10:
                break
            else:
                print("A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("Por favor, insira um número inteiro válido para a intensidade.")


    while True:
        try:
            num_ocorrencias = int(input("Número de ocorrências: "))
            if num_ocorrencias > 0:
                break
            else:
                print("O número de ocorrências deve ser maior que zero.")
        except ValueError:
                print("Por favor, insira um número inteiro válido para as ocorrências.")


    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(num_ocorrencias)

# ============================================================
# 2. ANÁLISE DE DADOS
# ============================================================


total_eventos = len(tipos_eventos)


soma_areas = 0
for area in areas_afetadas:
    soma_areas += area


soma_intensidades = 0
for intens in intensidades:
    soma_intensidades += intens
media_intensidades = soma_intensidades / total_eventos


maior_area = max(areas_afetadas)
indice_maior_area = areas_afetadas.index(maior_area)


maior_ocorrencias = max(ocorrencias)
indice_maior_ocorrencias = ocorrencias.index(maior_ocorrencias)
regiao_mais_ocorrencias = regioes[indice_maior_ocorrencias]


soma_densidades = 0
for i in range(total_eventos):
    soma_densidades += ocorrencias[i] / areas_afetadas[i]
densidade_media = soma_densidades / total_eventos


eventos_acima_media = 0
for intens in intensidades:
    if intens > media_intensidades:
        eventos_acima_media += 1


maior_intensidade = max(intensidades)
candidatos = []
for i in range(total_eventos):
    if intensidades[i] == maior_intensidade:
        candidatos.append(i)


indice_critico = candidatos[0]
for idx in candidatos:
    if areas_afetadas[idx] > areas_afetadas[indice_critico]:
        indice_critico = idx

# ============================================================
# 3. RELATÓRIO DE RESULTADOS
# ============================================================

print("\n========================================")
print("        RELATÓRIO DE ANÁLISE")
print("========================================")
print(f"\nTotal de eventos registrados: {total_eventos}")
print("\n----------------------------------------")
print("Resumo Geral")
print("----------------------------------------")
print(f"Área total afetada: {soma_areas:.0f} km²")
print(f"Média de intensidade: {media_intensidades:.1f}")
print("\n----------------------------------------")
print("Análises")
print("----------------------------------------")
print(f"Região com maior número de ocorrências: {regiao_mais_ocorrencias}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")
print("\n----------------------------------------")
print("Evento Mais Crítico")
print("----------------------------------------")
print(f"Tipo: {tipos_eventos[indice_critico]}")
print(f"Local: {cidades[indice_critico]}, {regioes[indice_critico]}, {paises[indice_critico]}")
print(f"Intensidade: {intensidades[indice_critico]}")
print(f"Área afetada: {areas_afetadas[indice_critico]:.0f} km²")
print("\n========================================")
print(f"Total de desastres registrados: {total_eventos}")
