from sportradar.nfl.workspace.datastore import DataStore, SportRadarFetcher

class DraftsFeeds:
    """This class is reponsible for extraction of draft feeds from SportRadar."""

    def __init__(self, base_url):
        """
        Initialize an instance of the class.
        :param base_url: The base URL for the API.
        :type base_url: str
        """
        self.base_url = base_url

    def get_draft_summary(
        self, access_level, version, language_code, year, file_format, api_key
    ):
        """
        Get the depth_charts for a given team_id
        :param access_level:
        :param version:
        :param language_code:
        :param year: Year in 4 digit format (YYYY).
        :param file_format:
        :param api_key:
        :return: The draft_summary for the given year
        """
        datastore = DataStore(SportRadarFetcher())
        result = datastore.fetch_data(
            url=f"{self.base_url}/{access_level}/{version}/{language_code}/{year}/draft.{file_format}?api_key={api_key}"
        )
        return result

    def get_prospects(
        self, access_level, version, language_code, year, file_format, api_key
    ):
        """
        Get the prospects for a given year
        :param access_level:
        :param version:
        :param language_code:
        :param year: Year in 4 digit format (YYYY).
        :param file_format:
        :param api_key:
        :return: The prospects for the given year
        """
        datastore = DataStore(SportRadarFetcher())
        result = datastore.fetch_data(
            url=f"{self.base_url}/{access_level}/{version}/{language_code}/{year}/prospects.{file_format}?api_key={api_key}"
        )
        return result

    def get_team_draft_summary(
        self, access_level, version, language_code, year, team_id, file_format, api_key
    ):
        """ "
         Get the team_draft_summary for a given team_id
        :param access_level:
        :param version:
        :param language_code:
        :param year: Year in 4 digit format (YYYY).
        :param team_id:
        :param file_format:
        :param api_key:
        :return: The team draft summary for the given team year,
        """
        datastore = DataStore(SportRadarFetcher())
        result = datastore.fetch_data(
            url=f"{self.base_url}/{access_level}/{version}/{language_code}/{year}/teams/{team_id}/draft.{file_format}?api_key={api_key}"
        )
        return result

    def get_top_prospects(
        self, access_level, version, language_code, year, file_format, api_key
    ):
        """ "
         Get the top_prospects for a given team_id
        :param access_level:
        :param version:
        :param language_code:
        :param year: Year in 4 digit format (YYYY).
        :param file_format:
        :param api_key:
        :return: The team top prospects for the given year
        """
        datastore = DataStore(SportRadarFetcher())
        result = datastore.fetch_data(
            url=f"{self.base_url}/{access_level}/{version}/{language_code}/{year}/top_prospects/.{file_format}?api_key={api_key}"
        )
        return result

    def get_trades(
        self, access_level, version, language_code, year, file_format, api_key
    ):
        """ "
         Get the top_prospects for a given team_id
        :param access_level:
        :param version:
        :param language_code:
        :param year: Year in 4 digit format (YYYY).
        :param file_format:
        :param api_key:
        :return: The team top prospects for the given year
        """
        datastore = DataStore(SportRadarFetcher())
        result = datastore.fetch_data(
            url=f"{self.base_url}/{access_level}/{version}/{language_code}/{year}/trades/.{file_format}?api_key={api_key}"
        )
        return result
