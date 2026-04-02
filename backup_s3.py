import boto3
import os
from datetime import datetime

pasta_local = r'C:\backup_teste'
bucket = 'site-josevictor-123'

data_hoje = datetime.now().strftime('%Y-%m-%d')
log_file = f'log_backup_{data_hoje}.txt'

s3 = boto3.client('s3')

with open(log_file, 'a') as log:
    for arquivo in os.listdir(pasta_local):
        caminho_completo = os.path.join(pasta_local, arquivo)

        if os.path.isfile(caminho_completo):
            try:
                nome_s3 = f'backup_testeJV1/{data_hoje}/{arquivo}'
                s3.upload_file(caminho_completo, bucket, nome_s3)

                msg = f'{arquivo} enviado com sucesso\n'
                print(msg)
                log.write(msg)

            except Exception as e:
                erro = f'Erro ao enviar {arquivo}: {str(e)}\n'
                print(erro)
                log.write(erro)