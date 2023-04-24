### Redis Cluster Task ###

1. JSON с входными данными по пути */data/data.json*. Содержит массив JSON-объектов, каждый из которых интерпретируется как отдельная запись со своим ключом и сохраняется в различных форматах. Py-файлы для каждого из таких вариантов в директории */apps/*.

2. Каждая из нод кластера Redis поднимается со своим конфигом из директории */docker/*. Конфиги отличаются только портом, при этом у каждой ноды свой статический IP. Ноды запускаются каждая в своём контейнере.

3. Python-программа запускается в отдельном контейнере в сети кластера. Результаты работы в файле */output.txt*: время работы *set (hset, zadd, lpush)* и *get (hget, zrange, rpop)*, пример вывода для *get*.

По результатам --- сохранение в виде строк работает сильно быстрее (1 сек против 9 сек для остальных), т.к. нет оверхеда на построение структур. Т.к. JSON-объекты небольшие, скорость извлечения ключей получается примерно одинаковой как для строк, так и для структур.


