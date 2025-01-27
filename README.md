# FurMark
- FurMark using Python and OpenGL
- 支持无头模式和pyqt5模式

![furmark](screenshots/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-01-27%20095841.png "furmark")

## 使用

```
python openfurmark.py
python openfurmark.py 1920x1080
python openfurmark.py 1280x720
openfurmark.exe 1920x1080
openfurmark.exe 1280x720
openfurmark.exe
```

## 构建windows
```
pyinstaller --windowed --icon=output.ico openfurmark.py
cp -r copytodist/* dist
```


