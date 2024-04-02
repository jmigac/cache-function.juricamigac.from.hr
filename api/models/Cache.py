from datetime import datetime


class Cache:

    def __init__(self, cache_duration):
        self.cache_time = datetime.now()
        self.experiences = []
        self.projects = []
        self.cache_duration = cache_duration

    def is_cache_expired(self):
        current_time = datetime.now()
        difference = current_time - self.cache_time
        return (difference.seconds > int(self.cache_duration)) or (not self.experiences and not self.projects)
