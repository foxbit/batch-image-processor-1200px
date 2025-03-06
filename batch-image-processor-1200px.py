import os
from PIL import Image
import sys

def process_image(filepath):
    try:
        # Abre a imagem
        with Image.open(filepath) as img:
            # Obtém as dimensões originais
            width, height = img.size
            
            # Determina se é horizontal ou vertical
            if width > height:
                # Imagem horizontal
                new_width = 2500
                ratio = new_width / width
                new_height = int(height * ratio)
            else:
                # Imagem vertical
                new_height = 2500
                ratio = new_height / height
                new_width = int(width * ratio)
            
            # Redimensiona a imagem
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Prepara o novo nome do arquivo
            filename = os.path.splitext(filepath)[0]
            new_filepath = f"{filename}_converted.jpg"
            
            # Salva a nova imagem em JPG
            if img.mode in ('RGBA', 'LA'):
                # Se a imagem tem canal alpha, converte para RGB
                resized_img = resized_img.convert('RGB')
            
            resized_img.save(new_filepath, 'JPEG', quality=95)
            
            # Fecha as imagens
            resized_img.close()
            
            # Apaga o arquivo original
            os.remove(filepath)
            
            # Renomeia o arquivo convertido para o nome original
            os.rename(new_filepath, filepath.rsplit('.', 1)[0] + '.jpg')
            
            print(f"Processado com sucesso: {filepath}")
            
    except Exception as e:
        print(f"Erro ao processar {filepath}: {str(e)}")
        return False
    
    return True

def process_directory(directory):
    # Contador para estatísticas
    stats = {
        'processados': 0,
        'erros': 0,
        'pulados': 0
    }
    
    # Extensões de imagem suportadas
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    
    # Percorre recursivamente o diretório
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            extension = os.path.splitext(filename)[1].lower()
            
            # Verifica se é uma imagem suportada
            if extension in valid_extensions:
                print(f"Processando: {filepath}")
                if process_image(filepath):
                    stats['processados'] += 1
                else:
                    stats['erros'] += 1
            else:
                stats['pulados'] += 1
                print(f"Arquivo pulado (não é uma imagem suportada): {filepath}")
    
    return stats

def main():
    # Verifica se foi fornecido um diretório como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <diretório>")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    # Verifica se o diretório existe
    if not os.path.isdir(directory):
        print(f"Erro: O diretório '{directory}' não existe.")
        sys.exit(1)
    
    print(f"Iniciando processamento no diretório: {directory}")
    print("----------------------------------------")
    
    # Processa as imagens e obtém as estatísticas
    stats = process_directory(directory)
    
    # Exibe o relatório final
    print("\nRelatório Final:")
    print(f"Imagens processadas com sucesso: {stats['processados']}")
    print(f"Erros durante o processamento: {stats['erros']}")
    print(f"Arquivos pulados (não são imagens): {stats['pulados']}")

if __name__ == "__main__":
    main()