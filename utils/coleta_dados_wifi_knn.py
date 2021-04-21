import pickle
import os
import time
from wifi import Cell
from datetime import date

DATA_COLLECT_PER_CICLE = 20# cliclos que vou deixar executando em cada comodo
segundos = 3 # tempo de esperar em cada coleta de wifis
folder_dir = os.listdir('.') # diretorio corrente
wifi_list_map = Cell.all('wlp3s0') # minha interface de rede que estao listados os WIFI
wifi_list_map = list(wifi_list_map)
wifi_dict = {} # dados
comodo = 'sala' # comodo que estamos executando o colhetor 

def dump_file(data): # cria e/ou salva arquivo com seus dados
    with open('wifi_dict' + '.pkl', 'wb') as p_dump:
        pickle.dump(data, p_dump, pickle.HIGHEST_PROTOCOL)

if 'wifi_dict.pkl' not in folder_dir: # se o 'wifi_dict.pkl' ainda nao esta no diretorio atual
    dump_file(wifi_dict)

with open('wifi_dict' + '.pkl', 'rb') as f:
    wifi_dict = pickle.load(f) # carrega dados gravados no arquivo, para poder ser manipulado

def wifi_array(wifi_list_map): # converte o map para array, para podemos manipula-lo mais facilmente
    wifi_list_array = []
    wifis_listados = []
    for wifi_atual in wifi_list_map:
        wifi_list_array.append([wifi_atual.ssid, wifi_atual.quality, wifi_atual.frequency])
        wifis_listados.append(wifi_atual.ssid)
    
    return wifi_list_array, wifis_listados

def get_qualidade(quality): # retorna valor inteiro da qualidade 
    q = str(quality).split('/') 
    return int(q[0]) # sem normalização, melhor guardar o dado bruto
    # return int(q[0]) / 70 # com um tipo normalização, multiplica por 70 que volta ao dado original


def get_data_hora():
    horario = time.strftime("%H:%M:%S")
    hoje = date.today()
    return str(hoje) +'_'+ str(horario)

wait = (segundos*DATA_COLLECT_PER_CICLE)/60
print('aguarde pelo menos '+ str(wait) +' minuto(s) no comodo '+ comodo +', coletando e processando...')
for index in range(DATA_COLLECT_PER_CICLE): # qtd de vezes que vamos executar a coleta de dados
    if wifi_list_map:
        wifi_list_array, wifis_listados = wifi_array(wifi_list_map)
        print('wifi_list_array: ', wifi_list_array)
        print('wifis_listados: ',wifis_listados)
        print('wifi_list_map: ', wifi_list_map)
        for wifi in wifi_list_array:
            if str.startswith(wifi[2], '2'): # somente as redes WIFI 2GHZ
                qualidade = get_qualidade(wifi[1])
                if comodo in wifi_dict:# ja tem o comodo e o wifi
                    if wifi[0] in wifi_dict[comodo]: # se esse wifi ja foi inserido do dict
                        wifi_dict[comodo][wifi[0]].append((qualidade, get_data_hora()))
                    else:# ainda nao tem este wifi 'x' atual neste sala
                        array_zero = [(0, get_data_hora())] * wifi_dict['qtd_ciclos']# zeros a esquerda
                        array_zero.append(qualidade)
                        wifi_dict[comodo][wifi[0]] = array_zero
                else:# ainda nao tem nem o comodo
                    wifi_dict[comodo] = {}
                    wifi_dict['qtd_ciclos'] = 0
                    wifi_dict[comodo][wifi[0]] = [(qualidade, get_data_hora())]
        for wifi_armazenado in wifi_dict[comodo]:
            if wifi_armazenado not in wifis_listados: # se o wifi atual nao estiver com valor ... rodada no dict
                wifi_dict[comodo][wifi_armazenado].append((0, get_data_hora()))  
        wifi_dict['qtd_ciclos'] += 1
        time.sleep(segundos) # tempo de esperar em cada coleta de wifis
        wifi_list_map = Cell.all('wlp3s0') # atualiza lista de wifi
        wifi_list_map = list(wifi_list_map)
    wait -= segundos/60
    print('Faltam pelo menos '+str(wait)+' minuto(s)...')
print(wifi_dict)
dump_file(wifi_dict) # salva no arquivo


# observações, a interface de rede tem que listar redes 2ghz, teste se isso esta acontecendo caso estaja vazio
# pois se estiver lisando somente as redes wifi 5ghz, provavelmente nao vai entrar no if (str.startswith(wifi.frequency, '2'):

# exemplo de coleta
#wifi_lisxt1: [net:10/70, claro: 30/70 ]
#quarto1: [
#			net:  [10/70],        
#			claro:[30/70]
#		]
#wifi_lisxt2 = [xxx: 15/70,  oi: 30/70, net: 20/70]
#quarto1: [
#			net:  [10/70, 20/70],        
#			claro:[30/70, 0],
#           xxx:  [0, 15/70],
#           oi:   [0, 30/70]
#		]


