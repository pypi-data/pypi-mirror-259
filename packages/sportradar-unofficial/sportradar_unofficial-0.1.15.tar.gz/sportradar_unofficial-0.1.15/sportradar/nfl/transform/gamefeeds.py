class GameFeedsTransformer:
    """
    Class to transform game feeds data.

    Attributes:
        UNWANTED_KEYS (list): List of unwanted keys to be removed from the data dictionary.

    Args:
        data (dict): The game feeds data dictionary.

    Methods:
        transform_boxscore: Transforms the boxscore data.
        transform_game_roster: Transforms the game roster data.
        transform_game_statistics: Transforms the game statistics data.
    """

    UNWANTED_KEYS = ["_comment", "_id"]

    def __init__(self, data: dict):
        self.data = data
        self.remove_unwanted_feeds()

    def remove_unwanted_feeds(self):
        for key in self.UNWANTED_KEYS:
            if key in self.data:
                self.data.pop(key)

    def flatten_dict(self, parent_key='', sep='.'):
        flattened_dict = {}
        for key, value in self.data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key

            if isinstance(value, dict):
                flattened_dict.update(flatten_dict(value, new_key, sep=sep))
            else:
                flattened_dict[new_key] = value

        return flattened_dict

    def transform_boxscore(self):
        return self.data

    def transform_game_roster(self):
        return self.data

    def transform_game_statistics(self):
        return self.data
