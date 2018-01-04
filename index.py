import re
import json
import urllib2

def main(event, context):

    iftttEventName = 'sns_call'

    iftttSecretsList = {'<NOME>':'<SECRET KEY>'}

    sns_event = event['Records'][0]['Sns']

    json_msg   = json.loads(sns_event['Message'])
    alarm_type = sns_event['Subject']
    dominio = re.sub('-awsroute53.*', '', json_msg['AlarmName']).replace('-', '.')
    saude = 'alerta'

    if "OK" in alarm_type:
        saude = 'ok'

    for i in iftttSecretsList:
        webhook_url = 'https://maker.ifttt.com/trigger/{iftttEventName}/with/key/{iftttSecrets}?value1={dominio}&value2={saude}&value3={nome}'.format(iftttEventName=iftttEventName,iftttSecrets=iftttSecretsList[i],dominio=dominio,saude=saude,nome=i)
        req = urllib2.Request(webhook_url)
        urllib2.urlopen(req)
