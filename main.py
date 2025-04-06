from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from spellchecker import SpellChecker  # Certifique-se de que pyspellchecker está instalado


# Função para extrair texto de uma imagem usando OCR
def extrair_texto_imagem(caminho_imagem, idioma='por'):
    # Abre a imagem e extrai o texto utilizando pytesseract.
    # caminho_imagem: Caminho para o arquivo de imagem.
    # idioma: Código do idioma para o OCR (padrão 'por' para português).
    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem, lang=idioma)
    return texto


# Função para converter um PDF em imagens e extrair o texto de cada página
def extrair_texto_pdf(caminho_pdf, poppler_path, idioma='por'):
    # Converte cada página do PDF em imagem, salva a imagem e extrai o texto via OCR.
    # caminho_pdf: Caminho para o arquivo PDF.
    # poppler_path: Caminho para a pasta 'bin' do Poppler.
    # idioma: Código do idioma para o OCR (padrão 'por' para português).
    imagens = convert_from_path(caminho_pdf, poppler_path=poppler_path)  # Converte o PDF em uma lista de imagens
    texto_total = ""

    for i, img in enumerate(imagens):
        # Define o caminho para salvar a imagem de cada página
        caminho_imagem = f"paginas/pagina{i}.jpg"
        img.save(caminho_imagem, "JPEG")
        print(f"Página {i} salva como imagem: {caminho_imagem}")

        # Extrai o texto da imagem da página
        texto_pagina = pytesseract.image_to_string(img, lang=idioma)
        texto_total += texto_pagina + "\n"

    # Retorna o texto completo extraído de todas as páginas
    return texto_total


# Função para aplicar correção ortográfica ao texto extraído, com cache para otimização
def corrigir_texto(texto):
    # Aplica correção ortográfica simples palavra por palavra usando pyspellchecker.
    # Implementa um cache para evitar recalcular a correção para palavras já processadas.
    spell = SpellChecker(language='pt')
    palavras = texto.split()  # Divide o texto em palavras
    texto_corrigido = []
    cache = {}  # Dicionário para armazenar correções já realizadas

    for palavra in palavras:
        palavra_lower = palavra.lower()
        if palavra_lower in cache:
            # Usa a correção já calculada anteriormente
            correcao = cache[palavra_lower]
        elif palavra_lower in spell:
            # Se a palavra estiver correta, adiciona-a ao cache e ao resultado
            correcao = palavra
            cache[palavra_lower] = correcao
        else:
            # Se a palavra estiver incorreta, obtém a sugestão
            correcao = spell.correction(palavra_lower)
            # Se não houver sugestão, mantém a palavra original
            if correcao is None:
                correcao = palavra
            cache[palavra_lower] = correcao
        texto_corrigido.append(correcao)

    # Reconstroi o texto corrigido a partir da lista de palavras
    return " ".join(texto_corrigido)


# Função para salvar o texto em um arquivo TXT
def salvar_texto_em_arquivo(texto, nome_arquivo):
    # Salva o texto fornecido em um arquivo com codificação UTF-8.
    # texto: Texto a ser salvo.
    # nome_arquivo: Nome do arquivo de saída.
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)
    print(f"Texto salvo no arquivo {nome_arquivo}")


if __name__ == "__main__":
    # Extração de texto da imagem "exemplo_ocr.jpg"
    texto_imagem = extrair_texto_imagem("exemplo_ocr.jpg")
    print("Texto extraído da imagem:")
    print(texto_imagem)

    # Extração de texto do PDF "Mussum Ipsum.pdf"
    # Caminho do Poppler conforme especificado originalmente
    poppler_dir = r"C:\Users\Eduar\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"
    texto_pdf = extrair_texto_pdf("Mussum Ipsum.pdf", poppler_path=poppler_dir)

    # Correção ortográfica do texto extraído do PDF
    texto_pdf_corrigido = corrigir_texto(texto_pdf)

    # Salvando o texto corrigido em um arquivo TXT
    salvar_texto_em_arquivo(texto_pdf_corrigido, "texto_extraido_corrigido.txt")