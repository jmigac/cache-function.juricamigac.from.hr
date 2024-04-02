import requests
from api.models.graphql_payloads import Payload
from api.constants.constants import (PROJECT_COLLECTION, EXPERIENCE_COLLECTION,
                                     GRAPHQL_DATA, GRAPHQL_ITEMS, APPLICATION_JSON,
                                     BEARER, HTTP_POST)


class ContentfulRequest:

    def __init__(self, space_id, environment, token):
        self.space_id = space_id
        self.environment = environment
        self.token = token
        self.base_url = f"https://graphql.contentful.com/content/v1/spaces/{self.space_id}/environments/{self.environment}"
        self.payloads = Payload()

    def get_projects(self):
        headers = self.get_headers()
        response = requests.request(HTTP_POST, self.base_url, headers=headers, data=self.payloads.PROJECTS_PAYLOAD)
        return self.get_response_content(response=response,
                                         field_name=PROJECT_COLLECTION)

    def get_experiences(self):
        headers = self.get_headers()
        response = requests.request(HTTP_POST, self.base_url, headers=headers, data=self.payloads.EXPERIENCES_PAYLOAD)
        return self.get_response_content(response=response,
                                         field_name=EXPERIENCE_COLLECTION)

    def get_response_content(self, response, field_name):
        return response.json()[GRAPHQL_DATA][field_name][GRAPHQL_ITEMS]

    def get_headers(self):
        return {
            'Content-Type': APPLICATION_JSON,
            'Authorization': f"{BEARER} {self.token}"
        }
