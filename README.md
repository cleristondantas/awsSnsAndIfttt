# awsSnsAndIfttt

Uma simples função lambda da AWS para notificar um applet no IFTTT

## Como instalar

### IFTTT
- Obter sua SECRET KEY no ifttt [Webhooks settings](https://ifttt.com/services/maker_webhooks/settings)

### AWS Lambda

- Crie uma nova função AWS LAMBDA, ex.: `sns-and-iftt`
- User Python 2.7
- Cole o conteúdo do arquivo `index.py`
- Substitua `<NOME>` e `<SECRET KEY>` por seu nome e sua SECRET KEY obtida anteriormente
- Em `iftttEventName` defini como `sns_notification`, mas você pode alterar para qualquer outro valor.
- As outras opções, deixei como padrão

### SNS

- Crie um novo Tópico SNS
- Crie uma `subscription` com o `protocol` AWS LAMBDA e o `endpoint` a nossa funcao `sns-and-iftt`

### IFTTT

- Crie um novo Applet
- Em `this` escolha `Webhooks` e escolha `Receive a web request`
- Em `Event Name`, digite o nome que definiu em `iftttEventName`, no meu caso `sns_notification`
- Em `that` escolha `VoIP Calls`, mas pode definir outra ação.. Escolha `Call my device`
- Abrirá a tela para digitar a mensagem de voz, na função defini três `values`, `value1` = dominio, `value2` = a saude do domínio e `value3` = nome vinculado a SECRET_KEY

Pronto!

caso queira testar, basta chamar essa url: 
`https://maker.ifttt.com/trigger/sns_notification/with/key/<SECRET_KEY>?value1=<DOMINIO>&value2=<SAUDE>&value3=<NOME>`


### Agradecimentos
Agradecimento ao [@danilop](https://github.com/danilop/) pelo projeto [CloudWatchAlarm2IFTTT](https://github.com/danilop/CloudWatchAlarm2IFTTT) que serviu de base para este projeto
