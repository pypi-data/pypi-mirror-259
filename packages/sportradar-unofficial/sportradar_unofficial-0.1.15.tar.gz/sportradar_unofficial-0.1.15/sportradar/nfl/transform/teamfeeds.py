class TeamFeedsTransformer:
    """
    TeamFeedsTransformer class is used to transform team feeds data.

    Args:
        data (dict): A dictionary containing team roster data.

    Methods:
        transform_team_roster(): Transforms the team roster data by removing unwanted feeds.

    Returns:
        dict: The transformed team roster data.
    """

    UNWANTED_KEYS = ["_comment"]

    def __init__(self, data: dict):
        self.data = data
        self.remove_unwanted_feeds()

    def remove_unwanted_feeds(self):
        for key in self.UNWANTED_KEYS:
            if key in self.data:
                self.data.pop(key)

    def transform_team_roster(self):
        return self.data

    def transform_seasonal_statistics(self):
        return self.data

    def transform_team_profile(self):
        return self.data
