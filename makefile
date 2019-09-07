VENV_DIR=./venv
PIP=$(VENV_DIR)/bin/pip
PYTHON=$(VENV_DIR)/bin/python

PYTHON3_OK := $(shell python3 --version 2>&1)

run: check_env
	$(VENV_DIR)/bin/python app.py

check_env: python3 venv_works

init: $(VENV_DIR) pip_install

venv_works: $(VENV_DIR) $(PYTHON)

python3:
      ifeq ('$(PYTHON3_OK)','')
	$(error package 'python3' not found. Download and install from https://www.python.org/downloads/mac-osx/ or your package manager of choice)
      endif

$(VENV_DIR): python3
	ls $(VENV_DIR) 2>&1 > /dev/null || (python3 -m venv $(VENV_DIR) && $(PIP) install -Ur requirements.txt)

pip_install: $(VENV_DIR)
	$(PIP) install -Ur requirements.txt

clean:
	rm -rf $(VENV_DIR)

.PHONY: run check_env init python3
