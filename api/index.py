import json
import os
from datetime import datetime
from flask import Flask, Response, request
from api.models.Cache import Cache
from api.models.contentful_request import ContentfulRequest
from api.constants.constants import (APPLICATION_JSON, ENVIRONMENT, SPACE_ID,
                                     APP_TOKEN, CACHE_DURATION, INVALIDATION_TOKEN,
                                     ACCESS_CONTROL_ALLOW_ORIGIN, QUERY_TOKEN, SUPABASE_URL,
                                     SUPABASE_KEY)
from supabase import create_client, Client

environment = os.environ[ENVIRONMENT]
space_id = os.environ[SPACE_ID]
token = os.environ[APP_TOKEN]
cache_duration = os.environ[CACHE_DURATION]
invalidation_token = 323
app = Flask(__name__)
cache = Cache(cache_duration)
contentful = ContentfulRequest(space_id, environment, token)

url = os.environ.get(SUPABASE_URL)
key = os.environ.get(SUPABASE_KEY)
Client = create_client(url, key)


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
    return Response(json.dumps(experience_articles, indent=4),
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)


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
    return Response(json.dumps(projects_result, indent=4),
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)


@app.route("/invalidate")
def invalidate():
    message = ""
    user_invalidation_token = request.args.get(QUERY_TOKEN)
    if user_invalidation_token == invalidation_token:
        cache.projects = []
        cache.experiences = []
        message = "Content is successfully invalidated"
    else:
        message = "Missing token header, content isn't invalidated"
    return Response(message,
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)


@app.route("/glucose/<glucose_value>")
def insert_glucose_value(glucose_value):
    Client.table('glucose').insert({"value": glucose_value}).execute()
    return Response("Glucose level successfully inserted",
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)


@app.route("/glucose/latest")
def get_latest():
    data, count = Client.table('glucose').select('*').order('date', desc=True).limit(1).single().execute()
    data_json = json.dumps(data[1], indent=4)
    return Response(data_json,
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)
