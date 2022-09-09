# Network_ai_web
```web of data show```
### Dockerfile build
```docker build --build-arg http_proxy="http://child-prc.intel.com:913" --build-arg https_proxy="http://child-prc.intel.com:913" --force-rm --no-cache -t xxx:django_web . ```
### Docker images run
```docker run -itd --name=django_web -p 9999:9999 xxx:django_web /bin/bash```

```docker exec -it django_web /bin/bash```

### Django Web run
```cd /Network_ai_web/django_web```

```python3 manage.py runserver 0.0.0.0:9999```
