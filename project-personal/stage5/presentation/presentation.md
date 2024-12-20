---
## Front matter
## Front matter
lang: ru-RU
title: "Индивидуальный проект"
subtitle: "Этап 5"
author: " Кармацкий Н. С. Группа НФИбд-01-21 "
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 12 Октября 2024

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---
## Цель работы

Научиться использовать Burp Suite.

## Теоретическое введение

Burp Suite представляет собой набор мощных инструментов безопасности веб-приложений, которые демонстрируют реальные возможности злоумышленника,
проникающего в веб-приложения. Эти инструменты позволяют сканировать,
анализировать и использовать веб-приложения с помощью ручных и автоматических методов. Интеграция интерфейсов этих инструментов обеспечивает полную
платформу атаки для обмена информацией между одним или несколькими инструментами, что делает Burp Suite очень эффективной и простой в использовании
платформой для атаки веб-приложений

# Выполнение лабораторной работы

##

Запускаем локальный сервер Apache (рис. [-@fig:001]).

![Запуск локального сервера](image/1.PNG){#fig:001 width=47%}

##

Запускаем инструмент Burp Suite (рис. [-@fig:002]).

![Запуск приложения](image/2.PNG){#fig:002 width=47%}

##

Измененяем настроек сервера для работы с proxy и захватом данных с помощью Burp Suite (рис. [-@fig:003]).

![Настройки сервера](image/3.PNG){#fig:003 width=47%}

##

Изменяем настройки Proxy инструмента Burp Suite для дальнейшей работы (рис. [-@fig:004]).

![Настройки Burp Suite](image/4.PNG){#fig:004 width=47%}

##

Во вкладке Proxy устанавливаем "Intercept is on" (рис. [-@fig:005]).

![Настройки Proxy](image/5.PNG){#fig:005 width=47%}

##

Чтобы Burp Suite исправно работал с локальным сервером, наобходимо установить параметр `network_allow_hijacking_loacalhost` на `true` (рис. [-@fig:006]).

![Настройки параметров](image/6.PNG){#fig:006 width=47%}

##

Пытаемся зайти в браузере на DVWA, тут же во вкладки Proxy появляется захваченный запрос. Нажимаем "Forward", чтобы загрузить страницу (рис. [-@fig:007]).

![Получаемые запросы сервера](image/7.PNG){#fig:007 width=47%}

##

Загрузилась страница авторизации, текст запроса поменялся (рис. [-@fig:008]).

![Страница авторизации](image/8.PNG){#fig:008 width=47%}

##

История запросов хранится во вкладке Target (рис. [-@fig:009]).

![История запросов](image/9.PNG){#fig:009 width=47%}

##

Попробуем ввести данные в веб-приложении и нажмем `Login`. В запросе увидим строку, в которой отображаются введенные нами данные, то есть поле для ввода (рис. [-@fig:010]).

![Ввод случайных данных](image/10.PNG){#fig:010 width=47%}

##

Этот запрос так же можно найти во вкладке Target, там же жмем правой кнопкой мыши на хост нужного запроса, и далее нажимаем "Send to Intruder" (рис. [-@fig:011]).

![POST-запрос с вводом пароля и логина](image/11.PNG){#fig:011 width=47%}

##

Попадаем на вкладку Intruder, видим значения по умолчанию у типа атаки и наш запрос (рис. [-@fig:012]).

![Вкладка Intruder](image/12.PNG){#fig:012 width=47%}

##

Изменяем значение типа атаки на Cluster bomb и проставляем специальные символы у тех данных в форме для ввода, которые будем пробивать, то есть у имени пользователя и пароля (рис. [-@fig:013]).

![Изменение типа атаки](image/13.PNG){#fig:013 width=47%}

##

Так как мы отметили два параметра для подбора, то нам нужно два списка со значениями для подбора. Заполняем первый список в `Payload setting` (рис. [-@fig:014]).

![Первый Simple list](image/14.PNG){#fig:014 width=47%}

##

Переключаемся на второй список и добавляем значения в него. В строке request count видим нужное количество запросов, чтобы проверить все возможные пары пользователь-пароль (рис. [-@fig:015]).

![Второй Simple list](image/15.PNG){#fig:015 width=40%}

##

Запускаем атаку и начинаем подбор (рис. [-@fig:016]).

![Запуск атаки](image/16.PNG){#fig:016 width=47%}

##

При открытии результата каждого post-запроса можно увидеть полученный get-запрос, в нем видно, куда нас перенаправило после выполнения ввода пары пользователь-пароль. В представленном случае с подбором пары admin-admin нас перенаправило на login.php, это значит, что пара не подходит (рис. [-@fig:017]).

![Результат запроса](image/17.PNG){#fig:017 width=47%}

##

Проверим результат пары admin-password во вкладке Response, теперь нас перенаправляет на страницу index.php, значит пара должна быть верной (рис. [-@fig:018]).

![Результат запроса](image/18.PNG){#fig:018 width=47%}

##

Дополнительная проверка с использованием Repeater, нажимаем на нужный нам запрос правой кнопкой мыши и жмем "Send to Repeater" (рис. [-@fig:019]).

![Дополнительная проверка результата](image/19.PNG){#fig:019 width=47%}

##

Переходим во вкладку "Repeater" (рис. [-@fig:020]).

![Вкладка Repeater](image/20.PNG){#fig:020 width=47%}

##

Нажимаем "send", получаем в Response в результат перенаправление на index.php (рис. [-@fig:021]).

![Окно Response](image/21.PNG){#fig:021 width=47%}

##

После нажатия на `Follow redirection`, получим нескомпилированный html код в окне Response (рис. [-@fig:022]).

![Изменение в окне Response](image/22.PNG){#fig:022 width=47%}

##

Далее в подокне Render получим то, как выглядит полученная страница (рис. [-@fig:023]).

![Полученная страница](image/23.PNG){#fig:023 width=47%}

## Выводы

Научились использовть инструмент Burp Suite
