
redis_queue: redis-server config/redis_queue.conf
redis_cache: redis-server config/redis_cache.conf
redis_socketio: redis-server config/redis_socketio.conf

web: bench serve  --port 8001


socketio: /home/hilton/.nvm/versions/node/v18.20.8/bin/node apps/frappe/socketio.js


watch: bench watch


schedule: bench schedule

worker:  bench worker 1>> logs/worker.log 2>> logs/worker.error.log

