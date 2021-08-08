class InvalidJsonLeagueInput(Exception):
    def __init__(self, league_type):
        txt = f"Could not find elements for league '{league_type}'"
        super().__init__(txt)


def elo(*args):
    joined_args = " | ".join(args)
    print(joined_args)
    if len(args) < 2:
        raise InvalidJsonLeagueInput("Polska Liga")
    else:
        raise ValueError(joined_args)


try:
    elo("1", "2", "3")
except InvalidJsonLeagueInput as err:
    print("caught exception:", err, repr(err), sep=" | ")
except ValueError as err:
    print("caught second exception:", err, repr(err), sep=" | ")
else:
    print("no exception was generated")
finally:
    print("this is always printed")
