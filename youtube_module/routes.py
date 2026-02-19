from flask import Blueprint, render_template


youtube_bp = Blueprint(
    "youtube",
    __name__,
    template_folder="./templates",
    static_folder="./static",
    url_prefix="/YouTube"
)

@youtube_bp.route("/")
def youtube_home():
    return render_template(
        "youtube.html",
        breadcrumbs=[{"name": "Inicio", "url": "/"}, {"name": "Multimedia", "url": "/YouTube/"}]
    )
