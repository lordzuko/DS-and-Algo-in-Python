class GameEntry:
    """Represents One Entry of list of high scores."""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return print('({0}:{1})'.format(self._name,self._score))
    