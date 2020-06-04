
.DEFAULT_GOAL := help

USER = ec2-user
HOST = beta.threeplusone.com
DIR = /var/www/html

# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

weyl:  ## Build weyl
	latexmk -xelatex weyl.tex

gates: ## Build on_gates
	latexmk -xelatex on_gates.tex

circuits:  ## Build latex circuits
	cd circuits && ./latex_circuits.py

clean:	## Clean
	latexmk -C


.PHONY: help
.PHONY: circuits