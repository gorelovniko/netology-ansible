Lighthouse-role
=========

Роль устанавливает ПО Nginx и Lighthouse.

Предварительные требования
------------

Предполагается что роль будет выполняться на deb-based дистрибутивах Linux (Debian, Ubuntu).  
Предполагается что на машине уже будет установлена утилита unzip.

Переменные роли
--------------

В [переменных по умолчанию](./defaults/main.yml) указана версия ПО Nginx 1.18.0, в случае необходимости её нужно изменить.  
В [изменяемых переменных](./defaults/main.yml) указан порт по которому будет слушать ПО Lighthouse. По умолчанию это порт 80, в случае необходимости его можно изменить.

Зависимости
------------

Нет зависимостей

Пример плейбука с использованием роли
----------------
Пример для использования на машинах на которых уже установлена утилита Unzip:
```
- name: Install Lighthouse
  hosts: lighthouse
  roles:
    - lighthouse-role
```

Пример с установкой утилиты Unzip в рамках pre_tasks в плее использующем данную роль:
```
- name: Install Lighthouse
  hosts: lighthouse
  pre_tasks:
    - name: install unzip
      become: true
      ansible.builtin.apt:
        name: unzip
        state: present
        update_cache: yes
  roles:
    - lighthouse-role
```

License
-------

Free

Author Information
------------------
GorelovNN
