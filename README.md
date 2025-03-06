# Processador de Imagens - Redimensionamento e Conversão

## Descrição

Este script Python foi desenvolvido para processar automaticamente coleções de imagens em lote. Ele percorre recursivamente todas as pastas e subpastas em um diretório especificado, redimensionando imagens e convertendo-as para o formato JPG com alta qualidade.

## Funcionalidades

- **Processamento recursivo**: Analisa todas as pastas e subpastas do diretório informado
- **Redimensionamento inteligente**:
  - Imagens horizontais: Largura definida para 1200px com altura proporcional
  - Imagens verticais: Altura definida para 1200px com largura proporcional
- **Conversão automática para JPG**: Converte imagens de diferentes formatos para JPG
- **Remoção dos originais**: Remove os arquivos originais após o processamento
- **Relatório detalhado**: Fornece estatísticas sobre o processamento realizado
- **Tratamento de erros**: Identifica e reporta problemas durante o processamento

## Suporte a formatos

O script suporta os seguintes formatos de imagem:
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Pré-requisitos

- Python 3.x
- Biblioteca Pillow (PIL)

## Instalação

1. Clone este repositório ou baixe o arquivo `redimensionar_imagens.py`
2. Instale a biblioteca Pillow:

```bash
pip install Pillow
```

## Uso

Execute o script passando o caminho do diretório que contém as imagens como argumento:

```bash
python redimensionar_imagens.py "caminho/para/diretorio"
```

### Exemplo

```bash
python redimensionar_imagens.py "/home/usuario/fotos"
```

## Como funciona

1. O script percorre recursivamente todas as pastas e subpastas no diretório especificado
2. Para cada imagem encontrada com formato suportado:
   - Determina se a imagem é horizontal ou vertical
   - Redimensiona mantendo a proporção conforme a orientação
   - Converte para JPG com qualidade 95%
   - Remove o arquivo original
   - Mantém o nome de arquivo original com extensão .jpg
3. Ao final, exibe um relatório com o número de:
   - Imagens processadas com sucesso
   - Erros durante o processamento
   - Arquivos pulados (não são imagens)

## Compatibilidade com diferentes versões do Pillow

O script é compatível com versões antigas e novas da biblioteca Pillow, utilizando técnicas de tratamento de exceção para garantir o funcionamento em diferentes ambientes.

## Considerações sobre desempenho

O script utiliza o algoritmo de reamostragem Lanczos para garantir alta qualidade no redimensionamento das imagens. Este é um dos métodos que produz os melhores resultados visuais, embora seja mais lento que métodos mais simples como o bilinear.

## Personalização

Você pode personalizar facilmente o script modificando os seguintes parâmetros:

- Tamanho máximo das imagens (atualmente definido como 1200px)
- Qualidade da compressão JPEG (atualmente definida como 95%)
- Formatos de imagem suportados

## Aviso de segurança

**Importante**: Este script remove permanentemente os arquivos originais. Recomenda-se fazer um backup das imagens antes de executá-lo pela primeira vez.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

## Licença

[Insira sua licença preferida aqui, como MIT, GPL, etc.]
