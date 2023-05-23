from ShiningPandaPage import *


def test_panda(driver):
    panda = Panda(driver)
    panda.open_url()
    panda.assert_panda_title_by_text()
