
class Payload:

    def __init__(self):
        self.EXPERIENCES_PAYLOAD = Payload.get_experiences_payload()
        self.PROJECTS_PAYLOAD = Payload.get_projects_payload()

    @staticmethod
    def get_projects_payload():
        return """
        {
            projectArticleCollection(limit: 8) {
                items {
                    title
                    description
                    technologies
                }
            }
        }
        """

    @staticmethod
    def get_experiences_payload():
        return """
        {
            experienceArticleCollection(limit: 8) {
                items {
                    title
                    description
                    from
                    until
                }
            }
        }
        """
