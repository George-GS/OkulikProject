import requests



def saby():
    responce = requests.post(
            'https://fix-online.sbis.ru/auth/service/',
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            json={
   "jsonrpc": "2.0",
   "method": "СБИС.Аутентифицировать",
   "params": {
      "Параметр": {
         "Логин": "Карета",
         "Пароль": "Карета123"
      }
   },
   "id": 0
}
        )
    token = responce.json()['result']
    return token




def saby_read(token):
    responce = requests.post(
        'https://fix-online.sbis.ru/service/',
        headers={'Content-Type': 'application/json; charset=UTF-8', "X-SBISSessionID": token},
        json={
              "jsonrpc": "2.0",
              "protocol": 6,
              "method": "Nomenclature.NomenclatureRead",
              "params": {
                "ИдО": 502164,
                "ИмяМетода": "Номенклатура.FormatCard",
                "Params": {
                  "d": [],
                  "s": [],
                  "_type": "record",
                  "f": 0
                }
              },
              "id": 1
            }

    )
    result = responce.json()
    return result

print(f'sbis token: {saby()}')
print(f'Имя номенклатуры: "{saby_read(saby())["result"]["d"][8]}"')