# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

update:
	# Update documentation on my webserver using rsync over ssh
	# /usr/bin/rsync --progress --delete -e 'ssh -i ~/.ssh/id_rsa' -avz build/html/  penfold.owt.com:/htdocs/st7789py/
	# update docs directory of this repo using rsync
	/usr/bin/rsync --progress --delete -avz build/html/ ../docs/
