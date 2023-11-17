import pytest
from pages.to_do_page import ToDoPage
from playwright.sync_api import Page, expect

class TestToDoListClass:

    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self, page: Page):
        self.to_do_page = ToDoPage(page)
        
        self.to_do_page.go_to()
        
        yield

    def test_deve_acessar_pagina_to_do_list_class(self):

        expect(self.to_do_page.elements["header_playwright"]).to_be_visible()
        expect(self.to_do_page.elements["input_data"]).to_be_visible()
        expect(self.to_do_page.elements["message_to_do_mvc"]).to_be_visible()
        expect(self.to_do_page.elements["to_do_list"]).not_to_be_visible()

    def test_deve_estar_vazia_lista_class(self):

        expect(self.to_do_page.elements["to_do_list"]).to_have_count(0)

    def test_deve_inserir_tarefas_na_lista_class(self):

        self.to_do_page.input_to_do_list('Make Coffe')

        expect(self.to_do_page.elements["to_do_list"]).to_have_count(1)
