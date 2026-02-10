import requests


def auth():
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    body = {
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
    responce = requests.post('https://fix-online.sbis.ru/auth/service/', json=body, headers=headers).json()
    token = responce['result']
    print(token)
    return token

def read_cart():

    token = auth()

    headers = {'Content-Type': 'application/json; charset=UTF-8', 'X-SBISSessionID' : f'{token}'}
    body = {"jsonrpc":"2.0","protocol":6,"method":"Nomenclature.FolderRead","params":{"FolderId":538388},"id":1}

    responce1 = requests.post('https://fix-online.sbis.ru/service/', json=body, headers=headers).json()

    folder_name = responce1['result']['d'][7]
    print(folder_name)
    assert folder_name == 'ГС База'
    return folder_name

def upd_fol():
    token = auth()

    new_name_fold = 'Новое название товара 5'

    headers = {'Content-Type': 'application/json; charset=UTF-8', 'X-SBISSessionID': f'{token}'}
    body = {
   "jsonrpc": "2.0",
   "protocol": 6,
   "method": "Nomenclature.NomenclatureUpdate",
   "params": {
      "Запись": {
         "d": [
            538449,
            f"{new_name_fold}",
            f"{new_name_fold}",
            {
               "d": [
                  [
                     "КодНомки123",
                     -1,
                     -1,
                     0,
                     None,
                     None,
                     None
                  ]
               ],
               "s": [
                  {
                     "n": "code",
                     "t": "Строка"
                  },
                  {
                     "n": "id",
                     "t": "Число целое"
                  },
                  {
                     "n": "type",
                     "t": "Число целое"
                  },
                  {
                     "n": "packing",
                     "t": "Число целое"
                  },
                  {
                     "n": "packImage",
                     "t": "Строка"
                  },
                  {
                     "n": "partyCode",
                     "t": "Строка"
                  },
                  {
                     "n": "accountCode",
                     "t": "JSON-объект"
                  }
               ],
               "_type": "recordset",
               "f": 1
            },
            True
         ],
         "s": [
            {
               "t": "Число целое",
               "n": "id"
            },
            {
               "t": "Строка",
               "n": "name"
            },
            {
               "t": "Строка",
               "n": "nameBase"
            },
            {
               "t": "Выборка",
               "n": "codes"
            },
            {
               "t": "Логическое",
               "n": "needSync"
            }
         ],
         "_type": "record",
         "f": 0
      }
   },
   "id": 1
}

    responce2 = requests.post('https://fix-online.sbis.ru/service/', json=body, headers=headers).json()

    print(responce2)


upd_fol()
# fff