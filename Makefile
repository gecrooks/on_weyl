
.DEFAULT_GOAL := help

# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

build:  ## Build weyl
	latexmk -xelatex on_weyl.tex

clean:	## Clean
	latexmk -C


.PHONY: help
.PHONY: circuits