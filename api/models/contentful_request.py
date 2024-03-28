import requests
from api.models.graphql_payloads import Payload
class ContentfulRequest:

    def __init__(self, space_id, environment, token):
        self.space_id = space_id
        self.environment = environment
        self.token = token
        self.base_url = f"https://graphql.contentful.com/content/v1/spaces/{self.space_id}/environments/{self.environment}"
        self.payloads = Payload()

    def get_projects(self):
        headers = self.get_headers()
        response = requests.request("POST", self.base_url, headers=headers, data=self.payloads.PROJECTS_PAYLOAD)
        response_data = response.json()
        response_field = response_data['data']
        response_collection = response_field['projectArticleCollection']
        return response_collection['items']

    def get_experiences(self):
        headers = self.get_headers()
        response = requests.request("POST", self.base_url, headers=headers, data=self.payloads.EXPERIENCES_PAYLOAD)
        response_data = response.json()
        response_field = response_data['data']
        response_collection = response_field['experienceArticleCollection']
        return response_collection['items']

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.token}"
        }