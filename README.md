Tag version:

v1.0

Release title:

FASTA Reader — Лабораторная работа №13

Release description
FASTA Reader (v1.0)

Программа для чтения и анализа биоинформатических файлов в формате FASTA.
Реализовано в рамках лабораторной работы №13.

Возможности

Чтение FASTA-файлов с использованием генераторов — подходит для больших файлов.

Автоматическое определение типа последовательности:

Нуклеотидная (ДНК/РНК)

Белковая

Класс Seq — хранит последовательность и информацию о ней.

Класс FastaReader — безопасно считывает файлы, проверяет формат и возвращает объекты Seq.

Полностью документировано с помощью pdoc.

Имеется UML-диаграмма классов.

Пример использования
from fasta_reader import FastaReader

reader = FastaReader("examples/example.fasta")

if reader.check():
    for seq in reader.read():
        print(f"Заголовок: {seq.inf}")
        print(f"Последовательность: {seq}")
        print(f"Длина: {len(seq)}")
        print(f"Тип: {seq.alph()}")

Структура проекта
fasta_reader_lab13/
│
├── fasta_reader/
│   ├── init.py
│   ├── reader.py
│   └── seq.py
│
├── examples/
│   ├── example.fasta
│   └── demo.py
│
├── docs/                 ← HTML-документация (pdoc)
│
├── uml.puml              ← UML исходник
├── uml.png               ← UML диаграмма классов
└── README.md

Документация

Документация автоматически генерируется с помощью pdoc:

python -m pdoc fasta_reader -o docs


Готовые файлы документации находятся в папке docs
(их можно открыть в браузере).

UML-диаграмма классов

Установка и запуск
git clone https://github.com/skolkodetails/fasta_reader.git
cd fasta_reader
python examples/demo.py

Автор
Вера Мищенко 
