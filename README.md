# tink
В файле train.py происходит чтение текстов либо из заданной директории, либо из stdin, после чего тексты очищаются. Затем происходит обучение модели: для каждого префикса длины от 1 до 4 слов создаётся банк возможных продолжений с их вероятностями, после чего модель сохраняется в заданный файл

В файле generate.py сначала достаётся модель из заданного файла, затем происходит генерация фраз

В папке data хранятся тексты для обучения
