all: reporte_1 reporte_2

reporte_1: apuntes.tex
	pdflatex apuntes.tex
	pdflatex apuntes.tex
	pdflatex apuntes.tex
	evince apuntes.pdf

reporte_2: apuntes_2.tex
	pdflatex apuntes_2.tex
	pdflatex apuntes_2.tex
	pdflatex apuntes_2.tex
	evince apuntes_2.pdf
clean: 
	rm -f *.log *.aux *.pdf *.gz *.out
