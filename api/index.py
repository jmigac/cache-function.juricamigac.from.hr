import json
import os
import requests
from datetime import datetime
from flask import Flask, Response
from api.models.Cache import Cache
from api.models.contentful_request import ContentfulRequest

environment = os.environ['ENVIRONMENT']
space_id = os.environ['SPACE_ID']
token = os.environ['APP_TOKEN']
cache_duration = os.environ['CACHE_DURATION']
invalidation_token = os.environ["INVALIDATION_TOKEN"]
app = Flask(__name__)
cache = Cache(cache_duration)
contentful = ContentfulRequest(space_id, environment, token)

@app.route('/experiences')
def experiences():
    experience_articles = ""
    if cache.is_cache_expired() or not cache.experiences:
        response = contentful.get_experiences()
        experience_articles = response
        cache.cache_time = datetime.now()
        cache.experiences = response
    else:
        experience_articles = cache.experiences
    return Response(json.dumps(experience_articles, indent=4), headers={'Access-Control-Allow-Origin': '*'}, mimetype="application/json")

@app.route('/projects')
def projects():
    projects_result = ""
    if cache.is_cache_expired() or not cache.projects:
        response = contentful.get_projects()
        projects_result = response
        cache.cache_time = datetime.now()
        cache.projects = response
    else:
        projects_result = cache.projects
    return Response(json.dumps(projects_result, indent=4), headers={'Access-Control-Allow-Origin': '*'}, mimetype="application/json")

@app.route("/invalidate")
def invalidate():
    message = ""
    user_invalidation_token = requests.args.get('token')
    if user_invalidation_token == invalidation_token:
        cache.projects = []
        cache.experiences = []
        message = "Content is successfully invalidated"
    else:
        message = "Missing token header, content isn't invalidated"
    return Response(message, headers={'Access-Control-Allow-Origin': '*'}, mimetype="application/json")