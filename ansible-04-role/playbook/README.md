# Playbook для установки Clickhouse, Vector и LightHouse
## Описание
Playbook использует следующие роли:  
[clickhouse](https://github.com/AlexeySetevoi/ansible-clickhouse)  
[vector-role](https://github.com/gorelovniko/vector-role)  
[lighthouse-role](https://github.com/gorelovniko/lighthouse-role)  
Документацию по ролям можно посмотреть в соответствующем репозитории.

## Запуск плейбука
Для запуска плейбука необходимо выполнить следующее:
1. Находясь в корневой директории плейбука, выполнить команду ```ansible-galaxy install -r requirements.yml -p roles```. Это скачает все, необходимые для выполнения плейбука, роли.
2. заполнить [inventory файл](./inventory/prod.yml) заранее созданными  на YC виртуальными машинами.
3. Запустить плейбук командой ```ansible-playbook -i inventory/prod.yml site.yml```.

## Порядок выполнения плейбука
1 плей: Запускает роль по установке сlickhouse на всех хостах указанных в группе clickhouse в inventory файле.  
2 плей: Запускает роль по установке vector на всех хостах указанных в группе vector в inventory файле.  
3 плей: Запускает роль по установке nginx и lighthouse на всех хостах указанных в группе lighthouse в inventory файле.

## inventory файл
Перед выполнением плейбука необходимо указать хосты в соответствующие группы в inventory файле.
Inventory файл содержит 3 группы хостов:
1. clickhouse
2. vector
3. lighthouse

На хостах, указанных в группе будет выполнена роль соответствующая имени группы.