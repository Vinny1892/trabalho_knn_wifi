KNN com wifi
Nesta atividade você deverá desenvolver um localizador de cômodos utilizando KNN.



Fase 1 (Peso 2): Coleta de dados - Você deverá coletar pelo menos 50 exemplos (localizações) em sua casa em no mínimo três diferentes cômodos da sua casa. O cômodo deverá ser o atributo classe de cada exemplo. A captura dos dados vc deverá obter os SSID e a força do sinal de todas as redes WIFI visíveis ao seu dispositivo. Quanto mais variado for o seu conjunto melhor será a sua qualidade. Portanto tente fazer coletas em direntes horários e localizações.



Por exemplo, no seu quarto em cima da cama em uma leitura da parte da manha voce obtenha rede A com força de 90%, rede B com força de 70% e rede C com força de 20%.  No seu quarto em cima da escrivaninha na parte da tarde você obtenha rede A com força de 85%, rede B com força de 65% e a rede C não aparece.



Assim esses dois exemplos irão compor a base da seguinte maneira


| RedeA 	| RedeB 	| RedeC 	| classe 	|
|:-----:	|:-----:	|:-----:	|:------:	|
|   40  	|   70  	|   20  	| quarto 	|
|   85  	|   65  	|   0   	|  sala  	|







O conjunto de atributos (colunas) deverá ser a união de todos os nomes de SSID das redes encontradas. Em caso de não existir leitura da rede em determinado ponto o valor no ponto deverá ser definido como zero.





Fase 2 (peso 1): Separação do conjunto em treino, validação e teste nas proporções de 70% ,15%  e 15% respectivamente. 



Fase 3 (peso 2): Treino e ajuste de parâmetros.  Utilizando o conjunto de validação, encontre o melhor  conjunto de parâmetros para o seu problema. Vc pode utilizar a quantidade de vizinhos, diferentes valores de p, pesos, etc. 





Fase 4 (peso 3): Avaliação com o teste. Com o melhor conjunto de parâmetros avaliado utilizado F1, faça o treinamento utilizando treino + validação, e reporte a accuracy_score,precision_score,recall_score,f1_score e a confusion_matrix utilizando o teste.  


# 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:


| <img  src="https://avatars.githubusercontent.com/u/41531003?v=4"  width="100px;"  alt="Foto do Vinicius Espindola no GitHub"/><br>  Vinicius Espindola 	| <img src="https://avatars.githubusercontent.com/u/43382610?v=4" width="100px;" alt="Foto do Kaio"/><br> Kaio Lino Mitsuharu 	| <img src="https://avatars.githubusercontent.com/u/43504729?v=4" width="100px;" alt="Foto do Carlitos"/><br> Carlos Neto 	| <img src="https://avatars.githubusercontent.com/u/69649310?v=4" width="100px;" alt="Foto do Geferson"/><br> Gefferson Alves 	| <img src="https://avatars.githubusercontent.com/u/40043611?v=4" width="100px;" alt="Foto do Rafel"/><br> Rafael Junio 	|
|--------------------------------------------------------------------------------------------------------------------------------------------------------	|:---------------------------------------------------------------------------------------------------------------------------:	|-------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------	|

[comment]: <> (<table>)

[comment]: <> (<tr>)

[comment]: <> (<td  align="center">)

[comment]: <> (<a  href="#">)

[comment]: <> (<img  src="https://avatars2.githubusercontent.com/u/41531003?s=460&v=4"  width="100px;"  alt="Foto do Vinicius Espindola no GitHub"/><br>)

[comment]: <> (<sub>)

[comment]: <> (<b>Vinicius Espindola</b>)

[comment]: <> (</sub>)

[comment]: <> (</a>)

[comment]: <> (</td>)


[comment]: <> (<td align="center">)

[comment]: <> (<a href="#">)

[comment]: <> (<img src="https://avatars.githubusercontent.com/u/43382610?v=4" width="100px;" alt="Foto do Mark Zuckerberg"/><br>)

[comment]: <> (<sub>)

[comment]: <> (<b>Kaio Lino Mitsuharu</b>)

[comment]: <> (</sub>)

[comment]: <> (</a>)

[comment]: <> (</td>)

[comment]: <> (<td align="center">)

[comment]: <> (<a href="#">)

[comment]: <> (<img src="https://avatars.githubusercontent.com/u/43504729?v=4" width="100px;" alt="Foto do Carlitos"/><br>)

[comment]: <> (<sub>)

[comment]: <> (<b>Carlos Neto</b>)

[comment]: <> (</sub>)

[comment]: <> (</a>)

[comment]: <> (</td>)

[comment]: <> (<td align="center">)

[comment]: <> (<a href="#">)

[comment]: <> (<img src="https://avatars.githubusercontent.com/u/69649310?v=4" width="100px;" alt="Foto do Carlitos"/><br>)

[comment]: <> (<sub>)

[comment]: <> (<b>Gefferson Alves</b>)

[comment]: <> (</sub>)

[comment]: <> (</a>)

[comment]: <> (</td>)

[comment]: <> (<td align="center">)

[comment]: <> (<a href="#">)

[comment]: <> (<img src="https://avatars.githubusercontent.com/u/40043611?v=4" width="100px;" alt="Foto do Rafael Junio"/><br>)

[comment]: <> (<sub>)

[comment]: <> (<b>Gefferson Alves</b>)

[comment]: <> (</sub>)

[comment]: <> (</a>)

[comment]: <> (</td>)

[comment]: <> (</tr>)

[comment]: <> (</table>)





