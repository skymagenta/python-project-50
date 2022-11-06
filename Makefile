
install: # построить дерево зависимостей проекта, и установить все пакеты (poetry создаст виртуальное окружение и установит пакет в него)
	poetry install

test: # запускает тесты
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint: # запускает линтер
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

package-install: # установка пакета из операционной системы
	python3 -m pip install --user dist/*.whl


.PHONY: install test lint selfcheck check build