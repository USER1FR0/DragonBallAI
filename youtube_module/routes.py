from flask import Blueprint, render_template, request
from youtube_module.service import YoutubeService

youtube_bp = Blueprint(
    "youtube", __name__,
    template_folder="./templates",
    static_folder="./static",
    url_prefix="/youtube"
)

@youtube_bp.route("/")
def youtube_home():
    query   = request.args.get("q", "").strip()
    search  = query or "Dragon Ball Z momentos épicos"
    videos  = YoutubeService.search(search)
    presets = YoutubeService.get_presets()

    return render_template(
        "youtube.html",
        breadcrumbs=[
            {"name": "Inicio", "url": "/"},
            {"name": "Multimedia", "url": None}
        ],
        videos=videos,
        query=query,
        presets=presets,
    )