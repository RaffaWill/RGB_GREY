def carregar_imagem_png(caminho):
    with open(caminho, 'rb') as f:
        dados = f.read()
    return dados

def salvar_imagem(caminho, dados):
    with open(caminho, 'wb') as f:
        f.write(dados)

def transformar_para_cinza(dados):
    cinza_dados = bytearray()
    for i in range(0, len(dados), 3):
        r = dados[i]
        g = dados[i + 1]
        b = dados[i + 2]
        cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
        cinza_dados.extend([cinza, cinza, cinza])
    return cinza_dados

def transformar_para_binario(dados, limiar=128):
    binario_dados = bytearray()
    for i in range(0, len(dados), 3):
        r = dados[i]
        g = dados[i + 1]
        b = dados[i + 2]
        cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
        binario = 255 if cinza > limiar else 0
        binario_dados.extend([binario, binario, binario])
    return binario_dados

# Caminho da imagem PNG
caminho_imagem = 'imagem.png'

# Carregar a imagem
dados_imagem = carregar_imagem_png(caminho_imagem)

# Transformar para tons de cinza
dados_cinza = transformar_para_cinza(dados_imagem)
salvar_imagem('imagem_cinza.png', dados_cinza)

# Transformar para binário
dados_binario = transformar_para_binario(dados_imagem)
salvar_imagem('imagem_binaria.png', dados_binario)

print("Transformações concluídas!")
