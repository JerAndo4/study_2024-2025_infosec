---
## Front matter
title: "Отчет по пятому этапу индивидуального проекта"
subtitle: "Информационная безопасность"
author: "Кармацкий Никита Сергеевич"

babel-lang: russian 
babel-otherlangs: english 
mainfont: Arial 
monofont: Courier New 
fontsize: 9pt

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
fontsize: 9pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I16n polyglossia
polyglossia-lang:
  name: russian
  options:
  - spelling=modern
  - babelshorthands=true
polyglossia-otherlangs:
  name: english
## I16n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.6
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Научиться использовать Burp Suite.

# Теоретическое введение

Burp Suite представляет собой набор мощных инструментов безопасности веб-приложений, которые демонстрируют реальные возможности злоумышленника,
проникающего в веб-приложения. Эти инструменты позволяют сканировать,
анализировать и использовать веб-приложения с помощью ручных и автоматических методов. Интеграция интерфейсов этих инструментов обеспечивает полную
платформу атаки для обмена информацией между одним или несколькими инструментами, что делает Burp Suite очень эффективной и простой в использовании
платформой для атаки веб-приложений. [@parasram].


# Выполнение лабораторной работыё

Запускаем локальный сервер Apache (рис. 1).

![Запуск локального сервера](image/1.PNG){#fig:001 width=70%}

Запускаем инструмент Burp Suite (рис. [-@fig:002]).

![Запуск приложения](image/2.PNG){#fig:002 width=70%}

Измененяем настроек сервера для работы с proxy и захватом данных с помощью Burp Suite (рис. [-@fig:003]).

![Настройки сервера](image/3.PNG){#fig:003 width=70%}

Изменяем настройки Proxy инструмента Burp Suite для дальнейшей работы (рис. [-@fig:004]).

![Настройки Burp Suite](image/4.PNG){#fig:004 width=70%}

Во вкладке Proxy устанавливаем "Intercept is on" (рис. [-@fig:005]).

![Настройки Proxy](image/5.PNG){#fig:005 width=70%}

Чтобы Burp Suite исправно работал с локальным сервером, наобходимо установить параметр `network_allow_hijacking_loacalhost` на `true` (рис. [-@fig:006]).

![Настройки параметров](image/6.PNG){#fig:006 width=70%}

Пытаемся зайти в браузере на DVWA, тут же во вкладки Proxy появляется захваченный запрос. Нажимаем "Forward", чтобы загрузить страницу (рис. [-@fig:007]).

![Получаемые запросы сервера](image/7.PNG){#fig:007 width=70%}

Загрузилась страница авторизации, текст запроса поменялся (рис. [-@fig:008]).

![Страница авторизации](image/8.PNG){#fig:008 width=70%}

История запросов хранится во вкладке Target (рис. [-@fig:009]).

![История запросов](image/9.PNG){#fig:009 width=70%}

Попробуем ввести данные в веб-приложении и нажмем `Login`. В запросе увидим строку, в которой отображаются введенные нами данные, то есть поле для ввода (рис. [-@fig:010]).

![Ввод случайных данных](image/10.PNG){#fig:010 width=70%}

Этот запрос так же можно найти во вкладке Target, там же жмем правой кнопкой мыши на хост нужного запроса, и далее нажимаем "Send to Intruder" (рис. [-@fig:011]).

![POST-запрос с вводом пароля и логина](image/11.PNG){#fig:011 width=70%}

Попадаем на вкладку Intruder, видим значения по умолчанию у типа атаки и наш запрос (рис. [-@fig:012]).

![Вкладка Intruder](image/12.PNG){#fig:012 width=70%}

Изменяем значение типа атаки на Cluster bomb и проставляем специальные символы у тех данных в форме для ввода, которые будем пробивать, то есть у имени пользователя и пароля (рис. [-@fig:013]).

![Изменение типа атаки](image/13.PNG){#fig:013 width=70%}

Так как мы отметили два параметра для подбора, то нам нужно два списка со значениями для подбора. Заполняем первый список в `Payload setting` (рис. [-@fig:014]).

![Первый Simple list](image/14.PNG){#fig:014 width=70%}

Переключаемся на второй список и добавляем значения в него. В строке request count видим нужное количество запросов, чтобы проверить все возможные пары пользователь-пароль (рис. [-@fig:015]).

![Второй Simple list](image/15.PNG){#fig:015 width=70%}

Запускаем атаку и начинаем подбор (рис. [-@fig:016]).

![Запуск атаки](image/16.PNG){#fig:016 width=70%}

При открытии результата каждого post-запроса можно увидеть полученный get-запрос, в нем видно, куда нас перенаправило после выполнения ввода пары пользователь-пароль. В представленном случае с подбором пары admin-admin нас перенаправило на login.php, это значит, что пара не подходит (рис. [-@fig:017]).

![Результат запроса](image/17.PNG){#fig:017 width=70%}

Проверим результат пары admin-password во вкладке Response, теперь нас перенаправляет на страницу index.php, значит пара должна быть верной (рис. [-@fig:018]).

![Результат запроса](image/18.PNG){#fig:018 width=70%}

Дополнительная проверка с использованием Repeater, нажимаем на нужный нам запрос правой кнопкой мыши и жмем "Send to Repeater" (рис. [-@fig:019]).

![Дополнительная проверка результата](image/19.PNG){#fig:019 width=70%}

Переходим во вкладку "Repeater" (рис. [-@fig:020]).

![Вкладка Repeater](image/20.PNG){#fig:020 width=70%}

Нажимаем "send", получаем в Response в результат перенаправление на index.php (рис. [-@fig:021]).

![Окно Response](image/21.PNG){#fig:021 width=70%}

После нажатия на `Follow redirection`, получим нескомпилированный html код в окне Response (рис. [-@fig:022]).

![Изменение в окне Response](image/22.PNG){#fig:022 width=70%}

Далее в подокне Render получим то, как выглядит полученная страница (рис. [-@fig:023]).

![Полученная страница](image/23.PNG){#fig:023 width=70%}
# Вывод

Научились использовть инструмент Burp Suite

# Список литературы

