import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

print(r"""
#################################################
# __  __                       __ _ _           #
#|  \/  | _____   _____       / _(_) | ___  ___ #
#| |\/| |/ _ \ \ / / _ \_____| |_| | |/ _ \/ __|#
#| |  | | (_) \ V /  __/_____|  _| | |  __/\__ \#
#|_|  |_|\___/ \_/ \___|     |_| |_|_|\___||___/#
#################################################
""")
print("Os módulos padrão estão funcionando corretamente!")


def processar_arquivos(txt_path, dir_path):
    
    if not os.path.isfile(txt_path):
        print(f"Erro: O arquivo {txt_path} não foi encontrado.")
        return

    if not os.path.isdir(dir_path):
        print(f"Erro: O diretório {dir_path} não foi encontrado.")
        return

  
    with open(txt_path, 'r') as file:
        ips = [line.strip() for line in file if line.strip()]

    
    arquivos = os.listdir(dir_path)

    arquivos_a_mover = [
        arquivo for arquivo in arquivos
        if any(arquivo == f"{ip}.netsec" for ip in ips)
    ]

    pasta_movidos = os.path.join(dir_path, "movidos")
    os.makedirs(pasta_movidos, exist_ok=True)

    
    for arquivo in arquivos_a_mover:
        origem = os.path.join(dir_path, arquivo)
        destino = os.path.join(pasta_movidos, arquivo)
        shutil.move(origem, destino)

    print(f"Processamento concluído. {len(arquivos_a_mover)} arquivo(s) movido(s) para a pasta 'movidos'.")


root = Tk()
root.withdraw()  
print("Selecione o arquivo TXT com os IPs.")
txt_path = askopenfilename(title="Selecione o arquivo TXT com os IPs", filetypes=[("Arquivos de texto", "*.txt")])

if not txt_path:
    print("Nenhum arquivo selecionado. Saindo...")
    exit()

print("Selecione o diretório contendo os arquivos a serem processados.")
dir_path = askdirectory(title="Selecione o diretório com os arquivos")

if not dir_path:
    print("Nenhum diretório selecionado. Saindo...")
    exit()

processar_arquivos(txt_path, dir_path)
