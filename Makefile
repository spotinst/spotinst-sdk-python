all:
	$(shell pydocmd generate) 
	$(shell cp -r _build/pydocmd/ docs/)
	$(shell rm -rf _build/)