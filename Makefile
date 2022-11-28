
install: # построить дерево зависимостей проекта, и установить все пакеты (poetry создаст виртуальное окружение и установит пакет в него)
	poetry install

test: # запускает тесты
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint: # запускает линтер
	poetry run flake8 gendiff

build: # сборка дистрибутива / пакета (без его установки)
	poetry build

package-install: # установка пакета из операционной системы (установка ранее собранного дистрибутива)
	python3 -m pip install --user dist/*.whl
 
 package-install-without-building: # установка пакета без сборки дистрибутива
	python3 -m pip install .

.PHONY: install test lint build