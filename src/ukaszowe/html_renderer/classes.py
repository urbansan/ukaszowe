from .base import BaseGameHtmlListRender


class PremierLeague(BaseGameHtmlListRender):
    @property
    def games_label(self):
        # return "ENGLAND: Premier League"
        return "INTERNATIONAL: Club Friendlies"

    @property
    def default_filename(self):
        return "index_premier.html"


class ChampionsLeague(BaseGameHtmlListRender):
    @property
    def games_label(self):
        return "CHAMPIONS LEAGUE"

    @property
    def default_filename(self):
        return "index_champions.html"


class EkstraKlasa(BaseGameHtmlListRender):
    @property
    def games_label(self):
        return "Polisz Klasa:D"

    @property
    def default_filename(self):
        return "index_polish.html"

    # try:
    # print('Respond status %s' % (response.status_code))
    # log_file = open(r"C:\Users\LK\Desktop\log.txt", "a")
    # log_file.write("\nConnection with API: %s" % (datetime.datetime.now()))
    # log_file.close()

    # except:
    # print('Respond status %s' % (response.status_code))
    # log_file = open(r"C:\Users\LK\Desktop\log.txt", "a", "utf-8-sig")
    # log_file.write("\nAPI connection error: %s" % (datetime.datetime.now()))
    # log_file.close()

    # json_response = response.json()
    # jprint(json_response)

    # html_elements = []

    # for n in range(len(tablica)):
    #     # print(tablica[n])
    #     my_file.write(tablica[n])

    # for element in tablica:
    # print(tablica[n])

    # print("Numbers of videos: %s" % (counter))

    # copy_file()
