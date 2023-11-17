clear:
	@printf "Limpando arquivos temporários... "
	@rm -f dist/*.gz
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete

packages:
	@printf "Instalando bibliotecas... "
	@pip install -q --no-cache-dir -r requirements/test.txt
	@echo "OK"

env-create: clear env-destroy
	@printf "Criando ambiente virtual... "
	@python3 -m venv py-venv
	@echo "OK"

env-destroy:
	@printf "Destruindo ambiente virtual... "
	@rm -Rf py-venv
	@echo "OK"

install-playwright:
	@printf "Instalando browsers - Playwright... "
	@playwright install
	@echo "OK"

install: packages install-playwright

py-test:
	@python3 -m pytest

py-test-chromium:
	@python3 -m pytest --browser chromium

py-test-to-do-list:
	@python3 -m pytest -k "TestToDoListClass"

py-test-api:
	@python3 -m pytest tests/api/test_api_via_cep.py

py-test-report:
	@python3 -m pytest --html=report/report.html

py-test-video:
	@python3 -m pytest tests/test_playwright_def.py --video on

py-test-screen:
	@python3 -m pytest tests/test_playwright_def.py --screenshot on

py-test-debug:
	@PWDEBUG=1 python3 -m pytest tests/test_playwright_def.py -s

py-generate-tests:
	@playwright codegen demo.playwright.dev/todomvc