all: famVsFriends.pdf tm8.pdf

force:
	rm -f paper.pdf
	make all

famVsFriends.pdf: tm.tex content_famVsFriends.tex
	pdflatex tm.tex content_famVsFriends.tex

tm8.pdf: tm8.tex content_tm8.tex
	pdflatex tm8.tex content_tm8.tex

clean:
	rm -f *.aux *.toc *.log *.bbl *.blg *.pdf
