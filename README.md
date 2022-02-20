# Challenge - KeyCash - GCP
![download (1)](https://user-images.githubusercontent.com/100058151/154857708-c994ac48-9ba5-4b5d-992b-8f12ca619153.png)

Desafio:

1- Desenvolver um script em python para realizar a ingestão de 50 arquivos JSON semi-estruturados de um storage da minha preferência.
2- Ingerir todas  as informações do meu datalake para o meu DataWareHouse.
3- Criar uma trigger com horário pré-definido para inserir os dados no DW ou realizar a criação de uma trigger que cada arquivo inserido no datalake inicie sua execução.
4- A partir da tabela populada LANDING_TABLE realizar a criação de uma segunda tabela CREDIT_PER_DAY contendo informações particionadas pela data de solicitação de credito do cliente e somátoria do valor de crédito.
5- Utilizando os dados da tabela CREDIT_PER_DAY criar uma visualização a partir da ferramenta de visualização da minha preferência.


Desenho da arquitetura:
![image](https://user-images.githubusercontent.com/100058151/154859481-feb9b2d4-c513-4e99-bd2d-effb67941ad2.png)

Desenvolvimento

Cloud Storage

Foi criado um data lake para armazenar todas as informações de crédito semi-estruturada dentro da pasta input-data e assim que é feito o upload dos arquivos a pipeline se inicia.
![image](https://user-images.githubusercontent.com/100058151/154859718-98decd42-ad27-48d3-96da-5188a5f7bee0.png)

Cloud Data Fusion

Após o upload dos arquivos no bucket, é iniciado a trigger criada em python realizando o carregamento dos dados para o DataWareHouse dentro do Big Query.

Big Query

![image](https://user-images.githubusercontent.com/100058151/154860046-aad37c1b-3883-421a-b4f3-f214339745fc.png)

Foi criado um dataset chamado key-cash contendo as tabelas LANDING_TABLE, CREDIT_PER_DAY e uma visualização da tabela LANDING_TABLE com os dados de valor de crédito somados e agrupados por dia.

TABELA LANDING_TABLE

![image](https://user-images.githubusercontent.com/100058151/154860127-95384c26-4688-4687-bad5-4cae4f0a4454.png)

TABELA CREDIT_PER_DAY

![image](https://user-images.githubusercontent.com/100058151/154860222-8a988b7e-b961-48ea-998d-5a7572857e65.png)

VISUALIZACAO_LANDING_TABLE 

Query Utilizada para criar a visualização e query para inserir os dados na CREDIT_PER_DAY

#VIEW
![image](https://user-images.githubusercontent.com/100058151/154863616-3e23e0a6-47e5-4704-8150-26cfd2f4b273.png)

#CREDIT_PER_DAY
![image](https://user-images.githubusercontent.com/100058151/154860306-4209c2c0-4a78-4e6e-91be-7fe4bff2ed19.png)

DATA STUDIO 

Foi criado uma visualização a partir dos dados da soma de crédito, agregado por dia.

![image](https://user-images.githubusercontent.com/100058151/154866198-eee2f353-efee-4f36-9d1a-4edfbab6e26e.png)






