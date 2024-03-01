class AdditionalFeedsTransformer:
    """
    AdditionalFeedsTransformer class is used to transform additional feeds data.

    Args:
        data (dict): A dictionary containing additional feeds data.

    Methods:
        transform_weekly_depth_charts: Transforms the weekly depth charts data by removing unwanted feeds.
        transform_daily_change_log: Transforms the daily change log data by removing unwanted feeds.
        transform_daily_transactions: Transforms the daily transactions data by removing unwanted feeds.
        transform_league_hierarchy: Transforms the league hierarchy data by removing unwanted feeds.
        transform_postgame_standings: Transforms the postgame standings data by removing unwanted feeds.
        transform_seasons: Transforms the seasons data by removing unwanted feeds.
        transform_weekly_injuries: Transforms the weekly_injuries data by removing unwanted feeds.
        remove_unwanted_feeds: Public method to remove unwanted feeds based on the UNWANTED_KEYS.

    Returns:
        dict: The transformed team weekly depth charts data.
        dict: The transformed daily change logs data.
        dict: The transformed daily transactions data.
        dict: The transformed league hierarchy data.
        dict: The transformed postgame standings data.
        dict: The transformed seasons data.
        dict: The Transformed weekly injuries data.
    """

    UNWANTED_KEYS = ["_comment"]

    def __init__(self, data: dict):
        """
        Initializes the AdditionalFeedsTransformer with the provided data.
        """
        self.data = data
        self.remove_unwanted_feeds()

    def remove_unwanted_feeds(self):
        """
        Public method to remove unwanted feeds based on the UNWANTED_KEYS.
        """
        for key in self.UNWANTED_KEYS:
            if key in self.data:
                self.data.pop(key)

    def transform_weekly_depth_charts(self):
        """
        Transforms the weekly depth charts data.
        """
        return self.data

    def transform_daily_change_log(self):
        """
        Transforms the daily change log data.
        """
        return self.data

    def transform_daily_transactions(self):
        """
        Transforms the daily transactions data.
        """
        return self.data

    def transform_league_hierarchy(self):
        """
        Transforms the league hierarchy data.
        """
        return self.data

    def transform_postgame_standings(self):
        """
        Transforms the postgame standings data.
        """
        return self.data

    def transform_seasons(self):
        """
        Transforms the seasons data.
        """
        return self.data

    def transform_weekly_injuries(self):
        """
        Transforms the weekly injuries data.
        """
        return self.data
