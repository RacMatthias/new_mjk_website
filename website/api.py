from flask import Blueprint, jsonify

from .database import db, Artwork

api = Blueprint("api",  __name__, url_prefix = "/api")


@api.route("/add-artwork")
def add_artwork():
    new_artwork = Artwork(
        title="Neu2",
        size="150x150", 
        technique="Tusche", 
        path_to_image="/img/new2.jpg"
    )
    try:
        db.session.add(new_artwork)
        db.session.commit()

        return "API/add-artwork"
    except:
        return "failed"


@api.route("/delete-artwork")
def delete_artwork():
    return "API/delete-artwork"


@api.route("/show-all")
def show_all():
    list_of_artwork = Artwork.query.all()

    artworks = {}
    for artwork_name in list_of_artwork:
        artworks[artwork_name.title] = [
            artwork_name.size, 
            artwork_name.technique, 
            artwork_name.path_to_image
        ]

    return f"Result:\n {artworks}"


@api.route("/show-tables")
def show_tables():
    tables = Artwork.metadata.tables.keys()
    return f"{tables}"