# Создай config.txt с настройками:
# timeout=10
# browser=chrome
# headless=false
#
# Прочитай файл и преобразуй в словарь

def read_config():
    gs_dict = {}

    with open('config.txt', 'r') as gs_file:
        for item in gs_file:
                item = item.strip()
                key, value = item.split('=')
                gs_dict[key] = value

    return gs_dict

print(read_config())