# pandas-nuitka-gui-app-poc
pandas,openpyxlを含むGUIアプリのPoC

コンパイルに関するドキュメント　⇒　https://nuitka.net/doc/user-manual.html

## 使い方
```Powershell
pipenv sync
pipenv shell

.\build.ps1
.\dist\main.exe
```

## コンパイラの比較
|ライブラリ名|シングルバイナリ|対応OS|特性|
|pyinstaller|ok|Win/Mac|手軽だが、解凍処理により起動が遅い|
|py2exe|??|Win|numpy周辺のコンパイル時のエラーが避けられず、断念|
|cx_freeze|NG|Win/Mac|シングルバイナリにできない|
|nuitka|OK|Win/Mac|pythonからCに変換するのでコンパイルが遅いが、起動は早い|