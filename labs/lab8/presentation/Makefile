SRC = presentation.md
FILES += $(patsubst %.md, %.pdf, $(wildcard *.md))
FILES += $(patsubst %.md, %.html, $(wildcard *.md))

# Фильтры и параметры для pandoc
FILTERS =
PDF_ENGINE = --pdf-engine=xelatex
PDF_OPTIONS = --number-sections
PDF_FORMAT_OPTIONS = -t beamer --slide-level=2

# Тема для reveal.js
REVEALJS_THEME = beige

# Добавляем фильтры
#FILTERS += --citeproc
FILTERS += -F pandoc-crossref  # Раскомментируйте, если хотите использовать pandoc-crossref

# Правило для создания PDF из Markdown
%.pdf: %.md
	-@pandoc "$<" $(FILTERS) $(PDF_ENGINE) $(PDF_OPTIONS) $(PDF_FORMAT_OPTIONS) -o "$@" 2> error.log

# Правило для создания HTML из Markdown
%.html: %.md
	-@pandoc "$<" --embed-resources --standalone -t revealjs -V theme=$(REVEALJS_THEME) -o "$@"

# Цель для создания всех файлов
all: $(FILES)

# Очистка созданных файлов
clean:
	-@rm $(FILES) *~

# Полная очистка
cleanall: clean