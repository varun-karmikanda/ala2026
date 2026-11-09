SHELL := /bin/sh

FONT_DIR ?= fonts
LATEXMK ?= latexmk
OPEN ?= open

STIX_URL := https://mirrors.ctan.org/fonts/stix2-otf/STIXTwoMath-Regular.otf
LIBERTINUS_URL := https://github.com/alerque/libertinus/releases/download/v7.051/Libertinus-7.051.zip

FONT_FILES := \
	$(FONT_DIR)/STIXTwoMath-Regular.otf \
	$(FONT_DIR)/LibertinusSerif-Regular.otf \
	$(FONT_DIR)/LibertinusSerif-Bold.otf \
	$(FONT_DIR)/LibertinusSerif-Italic.otf \
	$(FONT_DIR)/LibertinusSans-Regular.otf \
	$(FONT_DIR)/LibertinusSans-Bold.otf \
	$(FONT_DIR)/LibertinusSans-Italic.otf

TEX_FILES := $(shell find . -type f -name '*.tex' -not -path './build/*' -not -path './venv/*')

.PHONY: help fonts pdf all list clean clean-all open

help:
	@echo "Portable LaTeX build commands:"
	@echo "  make fonts                         Download and verify bundled fonts"
	@echo "  make pdf FILE=lectures/intro.tex  Build one document"
	@echo "  make all                           Build every .tex document"
	@echo "  make list                          List available .tex documents"
	@echo "  make open FILE=lectures/intro.pdf Open a generated PDF"
	@echo "  make clean                         Remove LaTeX auxiliary files"
	@echo "  make clean-all                     Remove auxiliary files and PDFs"

fonts: $(FONT_FILES)

$(FONT_DIR)/.directory:
	mkdir -p "$(FONT_DIR)"
	touch "$@"

$(FONT_DIR)/STIXTwoMath-Regular.otf: | $(FONT_DIR)/.directory
	@set -e; \
	tmp="$@.download"; \
	echo "Downloading STIX Two Math..."; \
	curl --fail --location --silent --show-error --retry 3 -o "$$tmp" \
		"$(STIX_URL)"; \
	mv "$$tmp" "$@"; \
	rm -f "$$tmp"; \
	test -s "$@"

$(FONT_DIR)/LibertinusSerif-Regular.otf: | $(FONT_DIR)/.directory
	@set -e; \
	tmp="$(FONT_DIR)/libertinus.zip"; \
	extract="$(FONT_DIR)/.libertinus-extract"; \
	echo "Downloading Libertinus font bundle..."; \
	curl --fail --location --silent --show-error --retry 3 -o "$$tmp" "$(LIBERTINUS_URL)"; \
	rm -rf "$$extract"; \
	mkdir -p "$$extract"; \
	unzip -q "$$tmp" -d "$$extract"; \
	find "$$extract" -type f -name '*.otf' -exec cp {} "$(FONT_DIR)" \;; \
	rm -rf "$$extract"; \
	rm -f "$$tmp"; \
	test -s "$@"

$(FONT_DIR)/LibertinusSerif-Bold.otf \
$(FONT_DIR)/LibertinusSerif-Italic.otf \
$(FONT_DIR)/LibertinusSans-Regular.otf \
$(FONT_DIR)/LibertinusSans-Bold.otf \
$(FONT_DIR)/LibertinusSans-Italic.otf: $(FONT_DIR)/LibertinusSerif-Regular.otf
	@test -s "$@"

pdf: fonts
	@test -n "$(FILE)" || (echo "Usage: make pdf FILE=path/to/document.tex" >&2; exit 2)
	@test -f "$(FILE)" || (echo "Document not found: $(FILE)" >&2; exit 2)
	$(LATEXMK) -xelatex --shell-escape -cd "$(FILE)"

all: fonts
	@set -e; \
	for file in $(TEX_FILES); do \
		echo "Building $$file"; \
		$(LATEXMK) -xelatex --shell-escape -cd "$$file"; \
	done

list:
	@printf '%s\n' $(TEX_FILES)

open:
	@test -n "$(FILE)" || (echo "Usage: make open FILE=path/to/document.pdf" >&2; exit 2)
	$(OPEN) "$(FILE)"

clean:
	@find . -type f \( -name '*.aux' -o -name '*.log' -o -name '*.nav' \
		-o -name '*.out' -o -name '*.snm' -o -name '*.toc' -o -name '*.vrb' \
		-o -name '*.fls' -o -name '*.xdv' -o -name '*.fdb_latexmk' \) -delete
	@find . -type d \( -name '_minted' -o -name '*.message.minted' \) -prune -exec rm -rf {} +

clean-all: clean
	@echo "Auxiliary files removed; existing PDFs were left untouched."
