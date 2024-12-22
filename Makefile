# Paths
REPO_PATH = $(shell pwd)
VENV = $(REPO_PATH)/venv
PYCACHE = $(REPO_PATH)/__pycache__

# Configuration
API_ID = {YOUR_API_ID}
API_HASH = {YOUR_API_HASH}
PHONE = {YOUR_PHONE}
DB_PASS = {YOUR_DB_PASS}
DB_PATH = $(REPO_PATH)/db
DEST_GROUPS = {YOUR_DESTINATION_GROUPS_IDS_COMMA_SEPARATED}
SOURCE_GROUPS = {YOUR_SOURCE_GROUPS_IDS_COMMA_SEPARATED}

all: deploy

bootstrap:
	@echo "Generating db folder"
	mkdir $(DB_PATH)
	@echo "Bootstraping python venv"
	python -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -r requirements.txt
	@echo "Source it using: . $(VENV)/bin/activate"

clean:
	@echo "Removing folders"
	rm -rf $(DB_PATH) $(VENV) $(PYCACHE)

deploy:
	python mirror.py $(API_ID) $(API_HASH) $(PHONE) $(DB_PASS) $(DB_PATH) $(DEST_GROUPS) $(SOURCE_GROUPS)

.PHONY: all bootstrap clean deploy
.SILENT: deploy
