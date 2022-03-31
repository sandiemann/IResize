# IResize
Image resize with FastAPI



API documentation\
HTTP request
GET http://127.0.0.1:8000/resize/

Required parameters:\
*url* (str) : image url\
*height* (int) : desired height\
*width* (int) : desired width

# running app (locally):
run this command on project directory,
```
uvicorn main:app --reload
```

# sample request:
```
http://127.0.0.1:8000/resize/?url=https://i.pinimg.com/736x/47/2b/61/472b61d49bb2c847bb7e0665497af47e.jpg&height=250&width=250
```

