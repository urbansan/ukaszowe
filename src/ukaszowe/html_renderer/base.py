import requests


class IncorrectResponseStatus:
    def __init__(self, code_recieved):
        msg = f"Recieved incorrect code {code_recieved}"
        super().__init__(msg)


class BaseGameHtmlListRender:
    ROOT_URL = "https://www.scorebat.com/video-api/v1/"

    @property
    def games_label(self):
        raise NotImplementedError

    @property
    def default_filename(self):
        raise NotImplementedError

    @classmethod
    def _get_response_dict(cls):
        response = requests.get(cls.ROOT_URL)
        if response.status_code != 200:
            raise IncorrectResponseStatus(response.status_code)
        return response.json()

    def _get_html_elements(self):
        response = self._get_response_dict()
        html_elements = []
        for game_record in response:
            competiton = game_record["competition"]["name"]
            # if competiton == 'ENGLAND: Premier League' or 'CHAMPIONS LEAGUE' in competiton:
            if competiton == self.games_label:
                title = game_record["title"]
                mecz = game_record["embed"]
                nie_wiem = "<h1>" + title + "</h1>" + mecz
                html_elements.append(nie_wiem)
        return html_elements

    def get_html(self):
        elements = self._get_html_elements()
        return "\n".join(elements)

    def save_html_to_file(self, filename=None):
        filename = filename or self.default_filename
        try:
            myfile = open(filename, "w")
        except PermissionError:
            input(f"Please close file: {filename}")
            myfile = open(filename, "w")
        myfile.write(self.get_html())
        myfile.close()
