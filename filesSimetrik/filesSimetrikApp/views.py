from django.shortcuts import render,HttpResponse
import os
import boto3
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine
import json
from  django.core.paginator import Paginator
from decouple import config
# Create your views here.
def getFile(request):
    aws_id = config('AWS_ID')
    aws_secret = config('AWS_SECRET')
    client = boto3.client('s3', aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret)

    bucket_name = config('BUCKET_NAME')

    object_key = config('OBJECT_KEY')

    csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    df = pd.read_csv(StringIO(csv_string))
    engine = createConnection()
    df.to_sql(config('TABLE_NAME'), engine)
    return HttpResponse('Archivo obtenido y cargado a base de datos correctamente')

def createConnection():
    url = 'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'.format(DB_USER=config('DB_USER'),DB_PASSWORD=config('DB_PASSWORD'),DB_HOST=config('DB_HOST'),DB_NAME=config('DB_NAME'))
    eng = create_engine(url)
    return eng

def filter(request):
    page=request.GET.get('page')
    prueba = request.GET
    key= list(prueba.keys())
    values = list(prueba.values())
    engine=createConnection()
    df = pd.read_sql_table(config('TABLE_NAME'),engine)
    for x in range(0,len(key)):
        if(key[x]!='page'):
            if key[x]=='id':
                values[x]= int(values[x])
            if key[x]=='index':
                values[x]= int(values[x])
            df2=df[df[key[x]]==values[x]]

    print(df2)
    result = df2.to_json(orient='index')
    parsed = json.loads(result)
    solution=json.dumps(parsed,indent=4)
    paginator = Paginator(solution,1120)
    solution = paginator.get_page(page)
    print(solution)
    return HttpResponse(solution)

def reorder(request):
    page=request.GET.get('page')
    engine=createConnection()
    df = pd.read_sql_table(config('TABLE_NAME'),engine)
    df = df[['gender','first_name','id','email','ip_address','last_name','index']]
    df2=df.head()
    print(df2)
    result = df2.to_json(orient='index')
    parsed = json.loads(result)
    solution=json.dumps(parsed,indent=4)
    paginator = Paginator(solution,1120)
    solution = paginator.get_page(page)
    return HttpResponse(solution)




  
