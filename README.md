Projeto Exemplo OCR com Correção Ortográfica

Descrição do Projeto:

Este projeto tem como objetivo extrair texto de imagens e arquivos PDF utilizando OCR e aplicar correção ortográfica ao texto extraído. O texto corrigido é, então, salvo em um arquivo TXT.

Funcionalidades:

1. Extração de Texto de Imagem: Realiza OCR em `exemplo_ocr.jpg` para extrair o texto.
2. Conversão e Extração de Texto de PDF: Converte cada página do PDF `Mussum Ipsum.pdf` em imagem, extrai o texto de cada página e salva as imagens no diretório `paginas`.
3. Correção Ortográfica: Aplica correção ortográfica ao texto extraído do PDF utilizando a biblioteca pyspellchecker.
4. Salvamento do Texto Corrigido: Salva o texto final corrigido em `texto_extraido_corrigido.txt`.

Requisitos:

- Python 3.x
- Bibliotecas Python:
- pytesseract: (https://pypi.org/project/pytesseract/)
- pdf2image: (https://pypi.org/project/pdf2image/)
- Pillow: (https://pypi.org/project/Pillow/)
- pyspellchecker: (https://pypi.org/project/pyspellchecker/)

Instalação:

1. Clone o repositório ou baixe os arquivos do projeto.
2. Instale as dependências necessárias com o seguinte comando: pip install pytesseract pdf2image pillow pyspellchecker
3. Poppler: 
- Baixe o Poppler para Windows acessando este repositório: (https://github.com/oschwartz10612/poppler-windows/releases).
- Extraia os arquivos e localize a pasta `bin`.
- O caminho para o Poppler já está definido no código:
  poppler_dir = r"C:\Users\Eduar\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"
 

Como Executar:

1. Certifique-se de que os arquivos `exemplo_ocr.jpg` e `Mussum Ipsum.pdf` estejam na mesma pasta que o `main.py`.
2. Execute o script principal com o comando: python main.py
3. O script irá:
- Extrair e exibir o texto da imagem `exemplo_ocr.jpg`.
- Converter cada página do PDF em imagens, salvando-as no diretório `paginas`.
- Extrair o texto de cada página do PDF.
- Aplicar correção ortográfica ao texto extraído.
- Salvar o texto corrigido no arquivo `texto_extraido_corrigido.txt`.

Processo de Desenvolvimento:

- Planejamento: O objetivo era integrar OCR para extração de texto de imagens e PDFs, seguido por uma etapa de correção ortográfica.
- Implementação:
- A função `extrair_texto_imagem` extrai o texto da imagem utilizando pytesseract.
- A função `extrair_texto_pdf` converte o PDF em imagens e extrai o texto de cada página.
- A função `corrigir_texto` utiliza a biblioteca **pyspellchecker** para corrigir o texto extraído, com otimização através de um cache.
- A função `salvar_texto_em_arquivo` grava o texto corrigido em um arquivo TXT.
- Testes: Foram realizados testes para verificar a correta extração e correção do texto.
- Documentação: Comentários no código e este README.md descrevem o processo e as instruções de execução.
