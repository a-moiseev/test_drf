# Тестовое задание Django проект с использованием Django REST Framework

Запуск проекта:

```
docker build -t drf
docker run drf -p 8000:8000
```

Загрузка файла:

```
curl POST -F title={title} -F file=@{filename} 127.0.0.1:8000/upload/
```

Получение списка загруженных файлов:

```
curl 127.0.0.1:8000/upload/
```
