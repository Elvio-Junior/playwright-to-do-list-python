class ToDoPage:
  def __init__(self, page):
    self.page = page
    self.elements = {
      'header_playwright': page.get_by_role(role='heading', name='todos'),
      'input_data': page.get_by_placeholder(text="What needs to be done?"),
      'message_to_do_mvc': page.get_by_text(text="This is just a demo of TodoMVC for testing, not the real TodoMVC app."),
      'to_do_list': page.get_by_test_id(test_id='todo-title')
    }

  def go_to(self):
    self.page.goto('https://demo.playwright.dev/todomvc')

  def input_to_do_list(self, to_do_item):
    self.elements["input_data"].fill(to_do_item)
    self.elements["input_data"].press('Enter')
