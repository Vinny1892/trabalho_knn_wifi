import subprocess
import sys
from functools import reduce
__TARGET_FIELDS = ['ESSID', 'Quality', 'Frequency']

# wlp2s0
def __executa_comando_para_listagem_de_wifis(interface_de_rede):
    comando = "iwlist {interface} scan |grep -e ESSID -e Quality -e Frequency".format(interface=interface_de_rede)
    process = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, text=True)
    return process.stdout

def __filtra_dados_stdout(stdout):
    return len(list(filter(lambda x: x in stdout, __TARGET_FIELDS))) > 0
    
def __ajusta_dados_do_stdout(stdout_list):
    return list(filter(__filtra_dados_stdout, list(map(str.strip, str(stdout_list).splitlines()))))

def __agrupa_wifis(dados):
    matriz_de_wifis = []
    for i in range(0, len(dados), 3):
        wf = dados[i:i+3]
        freq, qual, ssid = wf
        matriz_de_wifis.append([ssid, qual, freq])
    return matriz_de_wifis

def __normaliza_ssid(ssid_str):
    return str(ssid_str).split(':')[1].replace('"','').strip()

def __normaliza_quality(quality_str):
    return str(quality_str).split(" ")[0].split('=')[1]

def __normaliza_frequency(freq_str):
    return str(freq_str).split(" ")[0].split(':')[1]

def __normaliza_dados(dados):
    return {
        "ssid": __normaliza_ssid(dados[0]),
        "quality": __normaliza_quality(dados[1]),
        "frequency": __normaliza_frequency(dados[2])
    }

def __aplicar_normalizacao_de_dados(matriz):
    return list(map(__normaliza_dados, matriz))

def listar_wifis(interface_de_rede = 'wlp2s0'):
    stdout = __executa_comando_para_listagem_de_wifis(interface_de_rede)
    dados_brutos = __ajusta_dados_do_stdout(stdout)    
    wifis_agrupados = __agrupa_wifis(dados_brutos)
    return __aplicar_normalizacao_de_dados(wifis_agrupados)
