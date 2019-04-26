all: main-poster.pdf main.pdf

main.pdf: main.tex
	pdflatex -shell-escape main.tex

main-poster.pdf: main-poster.tex
	pdflatex -shell-escape main-poster.tex

clean:
	rm -f *.log *.aux *.out *.nav *.snm *.toc main.pdf main-poster.pdf

realclean:
	rm -f *.tex~
	rm -f *.pdf~
	rm -f Makefile~
	make clean;