# Minimal Makefile for Stratum course
# Wraps sphinx-build for local development.
# GitHub Pages deployment is handled by .github/workflows/deploy.yml

SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = docs
BUILDDIR    = _build

.PHONY: help html clean livehtml

help:
	@echo "Usage:"
	@echo "  make html       Build the course site to _build/html"
	@echo "  make livehtml   Build and serve with auto-reload (requires sphinx-autobuild)"
	@echo "  make clean      Remove all build output"

html:
	@$(SPHINXBUILD) -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html
	@echo ""
	@echo "Build complete. Open _build/html/index.html to preview."

livehtml:
	@sphinx-autobuild $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html \
		--watch docs \
		--open-browser

clean:
	@rm -rf $(BUILDDIR)
	@echo "Build directory removed."
