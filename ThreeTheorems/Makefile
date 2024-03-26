mdfiles := $(wildcard *.md)
pdffiles := $(patsubst %.md, %.pdf, $(mdfiles))

all: $(pdffiles)

%.pdf : %.md
	pandoc -s -t beamer --pdf-engine-opt=-shell-escape $< -o $@