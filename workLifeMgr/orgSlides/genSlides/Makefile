ALL: all-redirect

DVIPDFM = dvipdfmx

#texfiles = \

all-redirect: allNotes.pdf todoNotes.pdf habits.pdf weekSched.pdf

all: allNotes.pdf habits.pdf todoNotes.pdf weekSched.pdf

force: all

allNotes.pdf: allNotes.tex
	pdflatex allNotes

habits.pdf: content_shapeList.tex
	pdflatex habitNotes

todo.pdf: todoNotes.tex
	pdflatex todoNotes

weekSched.pdf: weekSched.tex
	pdflatex weekSched

privateNotes.pdf: privateNotes.tex
	pdflatex privateNotes

publicNotes.pdf: publicNotes.tex
	pdflatex publicNotes

codingNotes.pdf: codingNotes.tex
	pdflatex codingNotes

lifeNotes.pdf: lifeNotes.tex
	pdflatex lifeNotes

workNotes.pdf: workNotes.tex
	pdflatex workNotes

uSchedPoster-vk.pdf: uSchedPoster-vk.tex
	pdflatex uSchedPoster-vk

clean:
	rm -f *.aux *.toc *.log *.bbl *.blg uSchedPoster-vk.pdf allNotes.pdf
