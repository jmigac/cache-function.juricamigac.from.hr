import json
import os
import requests
from datetime import datetime
from flask import Flask, Response
from api.models.Cache import Cache

environment = os.environ['ENVIRONMENT']
space_id = os.environ['SPACE_ID']
token = os.environ['APP_TOKEN']
cache_duration = os.environ['CACHE_DURATION']
app = Flask(__name__)
cache = Cache(cache_duration)

@app.route('/experiences')
def experiences():
    experience_articles = ""
    if cache.is_cache_expired() or not cache.experiences:
        url = f"https://graphql.contentful.com/content/v1/spaces/{space_id}/environments/{environment}"
        payload = "{\"query\":\"{\\r\\n  experienceArticleCollection(limit: 8) {\\r\\n    items {\\r\\n      title\\r\\n      description\\r\\n      from\\r\\n      until\\r\\n    }\\r\\n  }\\r\\n}\",\"variables\":{}}"
        headers = {
          'Content-Type': 'application/json',
          'Authorization': f"Bearer {token}"
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        response_field = response_data['data']
        response_collection = response_field['experienceArticleCollection']
        response_collection_items = response_collection['items']
        experience_articles = response_collection_items
        cache.cache_time = datetime.now()
        cache.experiences = response_collection_items
    else:
        experience_articles = cache.experiences
    return Response(json.dumps(experience_articles, indent=4), mimetype="text/plain")

@app.route('/projects')
def projects():
    projects = ""
    if cache.is_cache_expired() or not cache.projects:
        url = f"https://graphql.contentful.com/content/v1/spaces/{space_id}/environments/{environment}"
        payload = "{\"query\":\"{\\r\\n  projectArticleCollection(limit: 8) {\\r\\n    items {\\r\\n      title\\r\\n      description\\r\\n      technologies\\r\\n    }\\r\\n  }\\r\\n}\",\"variables\":{}}"
        headers = {
          'Content-Type': 'application/json',
          'Authorization': f"Bearer {token}"
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        response_field = response_data['data']
        response_collection = response_field['projectArticleCollection']
        response_collection_items = response_collection['items']
        projects = response_collection_items
        cache.cache_time = datetime.now()
        cache.projects = response_collection_items
    else:
        projects = cache.projects
    return Response(json.dumps(projects, indent=4), mimetype="text/plain")
