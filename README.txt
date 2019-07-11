====================================================================================================
Hello, This is a Django Chat Application using Channels Project and redis server to achieve asyncous.
The web app has customized consumer, backend validation, auth_user_model. Current version offers login and register,one to one chat as well as many to many chat. Deployed IP is subject to change, no domain name avaiable at this moment.

To run it on your own server/mac machine:
1. need Docker,py3.6+, aside from requirements.txt
2. start redis server on docker by  $ docker run -p 6379:6379 -d redis:2.8
3. settings file omitted for safty
4.installations on redis server setup in CHANNELS tutorial II and start redis server on docker https://channels.readthedocs.io/en/latest/tutorial/part_2.html
5. recommend to create superuser and login in /admin path
