import requests
from api.models.graphql_payloads import Payload
class ContentfulRequest:

    response_fields = {
        ARTICLE_COLLECTION: "projectArticleCollection",
        EXPERIENCE_COLLECTION: "experienceArticleCollection",
        GRAPHQL: {
            DATA: "data",
            ITEMS: "items"
        }
    }

    def __init__(self, space_id, environment, token):
        self.space_id = space_id
        self.environment = environment
        self.token = token
        self.base_url = f"https://graphql.contentful.com/content/v1/spaces/{self.space_id}/environments/{self.environment}"
        self.payloads = Payload()

    def get_projects(self):
        headers = self.get_headers()
        response = requests.request("POST", self.base_url, headers=headers, data=self.payloads.PROJECTS_PAYLOAD)
        return self.get_response_content(response=response,
                                         field_name=response_fields.ARTICLE_COLLECTION)

    def get_experiences(self):
        headers = self.get_headers()
        response = requests.request("POST", self.base_url, headers=headers, data=self.payloads.EXPERIENCES_PAYLOAD)
        return self.get_response_content(response=response,
                                         field_name=response_fields.EXPERIENCE_COLLECTION)

    def get_response_content(self, response, field_name):
        return response.json()[response_fields.GRAPHQL.DATA][field_name][response_fields.GRAPHQL.ITEMS]

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.token}"
        }