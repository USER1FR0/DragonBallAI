from flask import Config, Flask, render_template
from  configs.config import BaseConfig
from gallery_module.routes import gallery_bp
import os
from youtube_module.routes import youtube_bp
from core.routes import core_bp

def create_app():
    app = Flask(
                __name__,   
                template_folder = './core/templates',
                static_folder=None 
            )
    app.config.from_object(BaseConfig)
    
    app.register_blueprint(gallery_bp)
    app.register_blueprint(youtube_bp)
    app.register_blueprint(core_bp)
    print(core_bp.static_folder)

    
    @app.context_processor
    def inject_config():
        return dict(config=app.config)
    
    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)