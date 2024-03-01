import requests

class AvailableRecordings:
    """
    Module containing the `AvailableRecordings` class for fetching recordings from an API.

    :class:`AvailableRecordings`:
        This class provides methods to interact with an API for fetching available recordings.

        :ivar base_url: The base URL for the API.

        :ivar NFL_LEAGUE: Class attribute representing the NFL league.

        :method:`__init__`:
            Initializes the instance of `AvailableRecordings`.

            :param base_url: The base URL for the API.

        :method:`construct_query`:
            Formulates the GraphQL query for fetching recordings and returns it.

            :return: The GraphQL query string for fetching recordings.

        :method:`post_json_data`:
            Sends a POST request with JSON data and GraphQL query.

            :param query: The GraphQL query to be sent in the request.
            :param league: The specific league to fetch. Default is `NFL_LEAGUE`.
    """

    NFL_LEAGUE = "nfl"

    def __init__(self, base_url):
        """
        Initialize the instance of AvailableRecordings.
        :param base_url: The base URL for the API.
        """
        self.base_url = base_url

    def construct_query(self):
        """
        Formulate the GraphQL query for fetching recordings and return it.
        :return: The GraphQL query string for fetching recordings.
        """
        return """
            query getRecordings($league: String){
                recordings(league: $league){
                    id
                    scheduled
                    meta
                    league
                    start
                    end
                    title
                    apis {
                        name
                        description
                        formats
                    }
                }
            }
        """

    def post_json_data(self, query, league=NFL_LEAGUE):
        """
        Send a POST request with JSON data and GraphQL query.
        :param query: The GraphQL query to be sent in the request
        :param league: The specific league to fetch
        """
        headers = {"Content-Type": "application/json"}
        json_data = {"query": query, "variables": {"league": league}}

        try:
            response = requests.post(self.base_url, headers=headers, json=json_data)
            return response
        except requests.exceptions.RequestException as err:
            return None
