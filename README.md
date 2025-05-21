Istruzioni su come trasformare unfile python in eseguibile

```bash
pip install pyinstaller
pyinstaller your_program.py --onefile
```

A questo punto viene creata una cartella denominata "dist" all'interno della quale si trova l'eseguibile e poi una cartella "build" e un file "your_program.spec"

A questo punto per eseguire il progrmma .exe è necessario entrare nella cartella "dist" da linea di comando e digitare:

```bash
.\your_program.exe
```