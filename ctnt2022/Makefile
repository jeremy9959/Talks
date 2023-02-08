talk : padic_fourier.pdf 

padic_fourier.pdf : padic_fourier.md 
	pandoc --slide-level=2 -t beamer -o padic_fourier.pdf padic_fourier.md

padic_fourier.tex : padic_fourier.md	
	pandoc --standalone --slide-level=2 -t beamer -o padic_fourier.tex padic_fourier.md

