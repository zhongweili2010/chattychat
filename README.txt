1.windows users use setting.py/channel_layers/default/config/
hosts [('192.168.99.100', 6379)]
  mac users users use hosts [('127.0.0.1', 6379)] 

2.local testing follow installation steps and redis setup in CHANNELS tutorial II and start redis server on docker more info to Steven

3. drop db.sqlite3 if database conflicts cannot be resolved also remove all migration files except __init__

4. to debug db, recommend to create superuser and login in /admin path
