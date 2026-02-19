from flask import Blueprint, render_template

core_bp = Blueprint(
    "core",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/core_static"  
)

