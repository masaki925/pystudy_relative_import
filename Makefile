
usage:
	@echo "make clean_cache"

clean_cache:
	find . -name __pycache__ |xargs rm -rf
