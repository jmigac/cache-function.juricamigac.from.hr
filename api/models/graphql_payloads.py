
class Payload:

    def __init__(self):
        self.EXPERIENCES_PAYLOAD = "{\"query\":\"{\\r\\n  experienceArticleCollection(limit: 8) {\\r\\n    items {\\r\\n      title\\r\\n      description\\r\\n      from\\r\\n      until\\r\\n    }\\r\\n  }\\r\\n}\",\"variables\":{}}"
        self.PROJECTS_PAYLOAD = "{\"query\":\"{\\r\\n  projectArticleCollection(limit: 8) {\\r\\n    items {\\r\\n      title\\r\\n      description\\r\\n      technologies\\r\\n    }\\r\\n  }\\r\\n}\",\"variables\":{}}"