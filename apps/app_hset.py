import redis
import os
import time
import json

# Waiting cluster setup
time.sleep(10)

redis_conn = os.environ['REDIS_NODE_1_RESOLVED']
redis_host = redis_conn.split(':')[0]
redis_port = redis_conn.split(':')[1]

r = redis.RedisCluster(host=redis_host, port=int(redis_port))

r.cluster_meet(redis_host, redis_port, target_nodes=redis.RedisCluster.ALL_NODES)

print('Ping result: ' + str(r.ping(target_nodes=redis.RedisCluster.ALL_NODES)))

with open('./data/data.json') as f:
  arr = json.load(f)

start_set = time.perf_counter()
for i, elem in enumerate(arr):
  for item in elem.items():
    r.hset(str(i), key=item[0], value=json.dumps(item[1]))
end_set = time.perf_counter()

start_get = time.perf_counter()
for i, elem in enumerate(arr):
  r.hget(str(i), 'type')
end_get = time.perf_counter()

print(f'HSET time: {end_set - start_set:0.4f} seconds')
print(f'HGET time: {end_get - start_get:0.4f} seconds')

print('Output example: '+str(r.hget(str(1), 'type')))

