#
# Makefile -- build some supporting stuff
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
top:

include common/Makefile.inc

images:
	for dir in $(PAPER_DIRECTORIES);				\
	do								\
		( cd $${dir}; make images );				\
	done
	
all:	common/addbibresources.tex					\
	common/addpackages.tex						\
	common/addpapers.tex						\
	common/Makefile.inc

common-files: common/addbibresources.tex common/addpackages.tex common/addpapers.tex common/Makefile.inc common/includes.inc

common/addbibresources.tex:	common/paperlist scripts/mkbibresources
	bash scripts/mkbibresources

common/addpackages.tex:	common/paperlist scripts/mkpackages
	bash scripts/mkpackages

common/addpapers.tex:	common/paperlist scripts/mkpapers
	bash scripts/mkpapers

common/Makefile.inc common/includes.inc:	common/paperlist scripts/mkmakefile
	bash scripts/mkmakefile

