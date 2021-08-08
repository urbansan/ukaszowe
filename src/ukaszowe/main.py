from .html_renderer import PremierLeague, ChampionsLeague


def premier():
    obj = PremierLeague()
    obj.save_html_to_file()


def champions():
    obj = ChampionsLeague()
    obj.save_html_to_file()
