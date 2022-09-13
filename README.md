# Network_ai_web
```web of data show```
### Dockerfile build
```docker build --build-arg http_proxy="http://xxx.com:888" --build-arg https_proxy="https://xxx.com:888" --force-rm --no-cache -t xxx:django_web . ```
### Docker images run
```docker run -itd --name=django_web -p 9999:9999 xxx:django_web /bin/bash```

```docker exec -it django_web /bin/bash```

### Django Web run
```git clone https://github.com/wangrh-python/Network_ai_web.git ```

```cd Network_ai_web/django_web```

```python3 manage.py runserver 0.0.0.0:9999```

```Enter in the URL of the browser --> server IP address : port```
