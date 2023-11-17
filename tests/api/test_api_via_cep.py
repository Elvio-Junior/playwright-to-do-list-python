from playwright.sync_api import Playwright
from util.validate_json import validate_json
from helpers.via_cep_schema import via_cep_schema

class TestApiViaCep:
    def test_deve_consultar_cep_valido(self, playwright: Playwright):
        request_context = playwright.request.new_context(
            base_url="https://viacep.com.br"
        )

        new_request = request_context.get(url="/ws/14400010/json/")
        validar_json = validate_json(new_request.json(), via_cep_schema)

        assert new_request.ok
        assert validar_json==True

        new_request.dispose()
