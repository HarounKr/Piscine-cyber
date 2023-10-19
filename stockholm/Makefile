all: create_dir copy_files install_python install_packages run_scripts

create_dir:
	@echo "Création du dossier Toto dans le home..."
	mkdir -p ~/infection

copy_files:
	@echo "Copie des fichiers dans le dossier actuel vers Toto..."
	cp create_files.py generate_key.py stockholm.py ~/infection

install_python:
	@echo "Installation de Python3 et pip3..."
	sudo apt-get update
	sudo apt-get install -y python3 python3-pip

install_packages:
	@echo "Installation de la librairie de cryptographie..."
	pip3 install cryptography
	pip3 install Faker

run_scripts:
	@echo "Exécution des scripts Python..."
	cd ~/infection && python3 generate_key.py
	cd ~/infection && python3 create_files.py