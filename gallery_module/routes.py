from flask import Blueprint, render_template, request, jsonify
from .service import GalleryService

gallery_bp = Blueprint(
    "gallery", __name__,
    template_folder="./templates",
    static_folder="./static",
    static_url_path="/gallery_static",
    url_prefix="/"
)


@gallery_bp.route("/")
def gallery_home():
    page        = request.args.get("page", 1, type=int)
    name        = request.args.get("name", "")
    race        = request.args.get("race", "")
    affiliation = request.args.get("affiliation", "")
    gender      = request.args.get("gender", "")

    data = GalleryService.get_characters(
        page=page, limit=10,
        name=name, race=race,
        affiliation=affiliation, gender=gender
    )

    return render_template(
        "gallery.html",
        breadcrumbs=[{"name": "Inicio", "url": None}],
        characters=data.get("items", []) if data else [],
        meta=data.get("meta", {}) if data else {},
        filters={"name": name, "race": race, "affiliation": affiliation, "gender": gender}
    )


@gallery_bp.route("/character/<int:character_id>")
def character_detail(character_id):
    """Endpoint JSON para el modal de detalles (llamado via fetch)"""
    data = GalleryService.get_character(character_id)
    if not data:
        return jsonify({"error": "No encontrado"}), 404
    return jsonify(data)