---
## Front matter
title: "Отчёт по лабораторной работе №1


Информационная безопасность"
subtitle: "Настройка рабочего пространства и конфигурация операционной системы на виртуальную машину."
author: "Кармацкий Никита Сергеевич, 


НФИбд-01-21, 1032210061"

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

Настроить рабочее пространство для лабораторных работ, приобрести практические навыки установки операционной системы на виртуальную машину и настройки минимально необходимых для дальнейшей работы сервисов.

# Теоретическое введение

**Oracle VM VirtualBox** — это мощная и бесплатная виртуализационная платформа, разработанная корпорацией Oracle, которая позволяет пользователям создавать и управлять виртуальными машинами на своих компьютерах. [1]

**VMware Fusion**  — гипервизор, позволяющий в среде macOS на базе платформы Intel и AppleSilicon создавать и запускать виртуальные машины, предоставляющие возможность запускать приложения, разработанные для других операционных систем, в том числе Windows и Linux. Поддерживаются как 32-разрядные, так и 64-разрядные версии ОС.

# Выполнение лабораторной работы

## Установка и конфигурация операционной системы на виртуальную машину

### VMware Fusion

Выбор этого гипервизоры был основан на том факте, что VirtualBox до сих пор Beta на процессарах *M* серии от Apple и не хочет устанавливать и создавать машины) 

![(рис. 1. Имя ОС, Размер пямяти и число процессоров)](image/1.png){ #fig:001 width=100% height=100% }

![(рис. 2. Виртуальный жесткий диск)](image/2.png){ #fig:002 width=100% height=100% }

![(рис. 3. Запуск)](image/3.png){ #fig:003 width=100% height=100% }

![(рис. 4. Стартовое меню установки)](image/4.png){ #fig:004 width=100% height=100% }

![(рис. 5. Клавиатура)](image/5.png){ #fig:05 width=100% height=100% }

![(рис. 6. Установка Root пароля)](image/6.png){ #fig:006 width=100% height=100% }

![(рис. 7. Создание пользователя)](image/7.png){ #fig:007 width=100% height=100% }

![(рис. 8. Отключение KDUMP)](image/8.png){ #fig:08 width=100% height=100% }

![(рис. 9. Обновление прааметров Ethernet)](image/9.png){ #fig:09 width=100% height=100% }

![(рис. 10. Установки системы)](image/10.png){ #fig:010 width=100% height=100% }

### Переход в ОС Linux

![(рис. 11. Вход в систему)](image/11.png){ #fig:011 width=100% height=100% }

### Домашнее задание

![(рис. 12. dmesg | less)](image/12.png){ #fig:012 width=100% height=100% }

![(рис. 13. Объем доступной оперативной памяти, версия ядра линукс, частота процессора, модель процессора, тип файловой системы корневого раздела )](image/13.png){ #fig:013 width=100% height=100% }

![(рис. 14. Последовательность монтирования файловых систем)](image/14.png){ #fig:014 width=100% height=100% }

# Вывод

Были настроено рабочее пространство для лабораторных работ, приобретены практические навыки
установки операционной системы на виртуальную машину и настройки минимально необходимых для дальнейшей работы сервисов.

# Список литературы. Библиография

[1] Документация по Virtual Box: https://www.virtualbox.org/wiki/Documentation

[2] Документация по VMware Fusion: https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion
