
class Payload:

    def __init__(self):
        self.EXPERIENCES_PAYLOAD = Payload.get_experiences_payload()
        self.PROJECTS_PAYLOAD = Payload.get_projects_payload()
        self.HOME_PAGE_PAYLOAD = Payload.get_homepage_payload()

    @staticmethod
    def get_homepage_payload():
        return """
        {
          homePage(id: "3rqB44b52XLXHtmKiSPgqC") {
            title
            teaser {
              title
              description
              url
              width
              height
            }
            experiencesCollection(limit: 8) {
              items {
                title
                description
                from
                until
              }
            }
            projectsCollection(limit: 8) {
              items {
                title
                description
                technologies
              }
            }
          }
        }
        """

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
