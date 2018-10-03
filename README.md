**_HOW TO START._**

![Python Project](img/pandas.jpg)
1) Download Python 37 via link - https://www.python.org/downloads/ (Big yellow button > Download Python 3.7.0)
    Chose ``C://Python37`` as home folder. You should create it before installing.
2) Download PyCharm via link - https://www.jetbrains.com/pycharm/download/ (Better Professional version)
3) While installing all ^, use default path's and agree with everything
4) Clone and open this project via Open Project in PyCharm tool
5) Open terminal, go to foder with ``python.exe`` file
6) Run in terminal
    * ``pip install pandas``
    * ``pip install numpy``
    * ``pip install matplotlib``
7) After running each command wait until library will be completely installed
8) Go to ``First.py``
9) Right click on it, select ``Run 'First``
10) Enjoy **PYTHON** !!!





Добрый день. Итак, лаба 1 будет содержать 8 логических разделов. Схематически можно назвать эту лабу "Работа с датафреймами".  В python для этого существует библиотека pandas
 

1.  Создать ряд переменных, таких как: список, кортеж, список из строк,  pd.Series, numpy вектор, numpy вектор, содержащий  nan, numpy массив M x N  ( заполнять можно любыми значениями и любым удобным способом). N > 30 

2. Из всего набора имеющихся переменных сформировать датафрейм. (показать , что полученный обьект позволяет работать с ним, как с датафреймом см. п. 3) 

3. Применить к столбцам и строкам методы статистического анализа, такие как поиск среднего значения, медианы (персентили и тп)

4. Определить столбец с наименьшим разбросом данных (max - min -> 0) и визуализировать его (убедиться , что визуализация интерпретируема)

5. Удалить столбцы, среднее значение которых наиболее отличается от среднего по всему датафрейму. (удалит столбец с самым большим отклонением со знаком минус и плюс (меньше среднего, больше среднего))

6.  Из столбца , который содержит   numpy массив M x N (где значением ячейки датафрейма есть i-тый элемент массива ) сделать новые столбцы (кол-во столбцов равно M), где i-тый элемент numpy массива содержался бы в каждом последующем стобце датафрейма

7.  Посчитать коэфициент корреляции. Найти интерпретацию полученному значению (если она есть)

8. Удалить столбцы , которые могут смазывать подсчет корреляции (например nan )
