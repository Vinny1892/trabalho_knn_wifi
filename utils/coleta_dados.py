# a interface de rede nao fica atualizada com todas as redes disponiveis
# entao precisa executar o arquivo 'iwlist.sh' que forçara manter a interface de rede atualizada
# assim, o 'Cell' escaneara a interface corretamente
# lembre de colocar a interface de rede corre parametro do 'Cell'
# comando linux: ip a
import pickle
import os
import time
from wifi import Cell
from datetime import date
import pandas as pd
# from wifi_scan import listar_wifis #lib do carlos

DATA_COLLECT_PER_CICLE = 25# cliclos que vou deixar executando em cada comodo
segundos = 5 # tempo de esperar em cada coleta de wifis
folder_dir = os.listdir('.') # diretorio corrente
perssistencia = [{}, 0]

print('Digite o nome do comodo: sala, varanda, quarto')
comodo = input()

def dump_file(data): # cria e/ou salva arquivo com seus dados
    with open('wifi_dict' + '.pkl', 'wb') as p_dump:
        pickle.dump(data, p_dump, pickle.HIGHEST_PROTOCOL)

if 'wifi_dict.pkl' not in folder_dir: # se o 'wifi_dict.pkl' ainda nao esta no diretorio atual
    dump_file(perssistencia)# crie, e inicia com o 'perssistencia' inicializado

with open('wifi_dict' + '.pkl', 'rb') as f:
    perssistencia = pickle.load(f) # carrega dados gravados no arquivo, para poder ser manipulado

def wifi_array(wifi_list_map): # converte o map para array, para podemos manipula-lo mais facilmente
    wifi_list_dict = {}
    for wifi in wifi_list_map:
        wifi_list_dict[wifi.ssid] = {}
        wifi_list_dict[wifi.ssid]['quality'] = get_qualidade(wifi.quality)
        wifi_list_dict[wifi.ssid]['frequency'] = str(wifi.frequency)
    return wifi_list_dict

def get_qualidade(quality): # retorna valor inteiro da qualidade 
    quality_clean = str(quality).split('/') 
    return int(quality_clean[0]) # sem normalização, melhor guardar o dado bruto
    # return int(q[0]) / 70 # com um tipo normalização, multiplica por 70 que volta ao dado original


def get_data_hora():
    horario = time.strftime("%H:%M:%S")
    hoje = date.today()
    return str(hoje) +'_'+ str(horario)

def preenche_dict_wifis():
    wait = (segundos*DATA_COLLECT_PER_CICLE)/60
    print('aguarde pelo menos '+ str(wait) +' minuto(s) no comodo '+ comodo +', coletando e processando...')
    for index in range(DATA_COLLECT_PER_CICLE): # qtd de vezes que vamos executar a coleta de dados
        wifi_list_map = Cell.all('wlp3s0') # scanner
        wifi_list_map = list(wifi_list_map)

        if wifi_list_map:
            wifi_list_dict = wifi_array(wifi_list_map)
            if 'classe' not in perssistencia[0]:
                perssistencia[0]['classe'] = [comodo]
            else:
                perssistencia[0]['classe'].append(comodo)

            for wifi in wifi_list_dict:
                if str.startswith(wifi_list_dict[wifi]['frequency'], '2'): # somente as redes WIFI 2GHZ
                    if wifi in perssistencia[0]:
                        perssistencia[0][wifi].append(wifi_list_dict[wifi]['quality']) #ligados pela ordem de inserção 
                    else:
                        esquerda_zeros_quality = [0] * perssistencia[1] # zeros a esquerda
                        esquerda_zeros_quality.append(wifi_list_dict[wifi]['quality'])
                        perssistencia[0][wifi] = esquerda_zeros_quality    

            for perssistido in perssistencia[0]:
                #if str.startswith(wifi[2], '2'):
                if perssistido not in wifi_list_dict: # se o wifi que ja foi armazenao nao estiver com na lista de wifis atual
                    if perssistido != 'classe':
                        perssistencia[0][perssistido].append(0) # add zero a direta, representando a falta

            perssistencia[1] += 1

        wait -= segundos/60
        print('Faltam pelo menos '+str(wait)+' minuto(s)...')
        time.sleep(segundos) # tempo de esperar em cada coleta de 

    dump_file(perssistencia) # salva no arquivo

preenche_dict_wifis()
print("____________________________ WIFI DICT ________________________________")
print(perssistencia[0])
print("____________________________ WIFI DICT ________________________________")
print(f"Quantidade de cliclos {perssistencia[1]}")
df = pd.DataFrame(perssistencia[0])
print(df)