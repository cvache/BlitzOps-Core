# BlitzOps-Core
Core service for BlitzOps

## Deploy with docker compose

```
$ docker compose up -d
Creating network "nginx-flask-mongo_default" with the default driver
Pulling mongo (mongo:)...
latest: Pulling from library/mongo
423ae2b273f4: Pull complete
...
...
Status: Downloaded newer image for nginx:latest
Creating nginx-flask-mongo_mongo_1 ... done
Creating nginx-flask-mongo_backend_1 ... done
Creating nginx-flask-mongo_web_1     ... done

```

## Expected result

Listing containers must show three containers running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                      NAMES
24e1e7c3d3ce   blitzops-core-api   "uvicorn app.main:ap…"   4 minutes ago   Up 4 minutes   0.0.0.0:80->80/tcp         fastapi
4750dae94938   mongo               "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes   0.0.0.0:27017->27017/tcp   blitzops-core-mongo-1
```

After the application starts, navigate to `http://localhost:80` in your web browser or run:
```
$ curl localhost:80
{"message":"OK"}
```

Stop and remove the containers
```
$ docker compose down
```
