ROOT := ..

.PHONY: help fonts all clean clean-all

help:
	@$(MAKE) -C $(ROOT) help

fonts:
	@$(MAKE) -C $(ROOT) fonts

define build
	@$(MAKE) -C $(ROOT) pdf FILE=lectures/$(1)
	@$(MAKE) -C $(ROOT) open FILE=$(basename $(1)).pdf
endef

intro:
	$(call build,intro.tex)

affine:
	$(call build,affine.tex)

vec-angle-proof:
	$(call build,vector-angle-proof.tex)

vec-questions:
	$(call build,vec-questions.tex)

vector-spaces:
	$(call build,vec-spaces.tex)

linear-functions:
	$(call build,linear-functions.tex)

norm-dist:
	$(call build,norm-dist-std.tex)

matrix-vec:
	$(call build,matrix-vec-linear.tex)

np:
	$(call build,np00.tex)

ndarray:
	$(call build,ndarray.tex)

knn:
	$(call build,knn-example.tex)
	$(call build,knn-house-price.tex)

gradient:
	$(call build,gradient.tex)

least-squares:
	$(call build,least-squares.tex)

all:
	@$(MAKE) -C $(ROOT) all

clean:
	@$(MAKE) -C $(ROOT) clean

clean-all:
	@$(MAKE) -C $(ROOT) clean-all
