
class BaseProvider:
    """
    Class for provider
    """

    @classmethod
    def create_response(cls, messages: list):
        raise Exception("A provider need a 'create_response class.'")