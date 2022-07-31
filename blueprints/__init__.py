from blueprints.projects import project_api

def register_blueprints(app):
    app.register_blueprint(project_api)
    
