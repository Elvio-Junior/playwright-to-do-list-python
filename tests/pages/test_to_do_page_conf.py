import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("home_page_to_do_list")
class TestToDoListConf:

    def test_deve_acessar_pagina_to_do_list_conf(self, home_page_to_do_list):

        expect(home_page_to_do_list.elements["header_playwright"]).to_be_visible()
        expect(home_page_to_do_list.elements["input_data"]).to_be_visible()
        expect(home_page_to_do_list.elements["message_to_do_mvc"]).to_be_visible()
        expect(home_page_to_do_list.elements["to_do_list"]).not_to_be_visible()

    def test_deve_estar_vazia_lista_conf(self, home_page_to_do_list):

        expect(home_page_to_do_list.elements["to_do_list"]).to_have_count(0)

    def test_deve_inserir_tarefas_na_lista_conf(self, home_page_to_do_list):

        home_page_to_do_list.input_to_do_list('Make Coffe')
        expect(home_page_to_do_list.elements["to_do_list"]).to_have_count(1)
