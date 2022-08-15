"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petadoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretdefinitelynotabletobeguessed'

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    pets = Pet.query.order_by(Pet.available).all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["POST", "GET"])
def add_pet():
    """Show the form to add a new pet, or procress the form submission"""

    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet(name = form.name.data,
        species = form.species.data,
        age = form.age.data or None,
        notes = form.notes.data or None,
        photo_url = form.photo_url.data or None,
        available = True)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template(
            "pet_add_form.html", form=form)

@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    """Show pet edit form and handle edit."""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data

        db.session.add(pet)

        db.session.commit()
        return redirect("/")

    else:
        return render_template("pet_display.html", form=form, pet=pet)