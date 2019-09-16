from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from src import db
from src.components.c_events.forms import AddForm, DelForm
from src.models.event import Events

events_blueprint = Blueprint('event',
                             __name__,
                             template_folder='../../templates')


@events_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        image_url = form.image_url.data
        price = form.price.data
        address = form.address.data
        time = form.time.data
        organizer_id = current_user.id
        # Add new Event to database
        new_pup = Events(name=name, description=description, image_url=image_url,
                         price=price, address=address, time=time, organizer_id=organizer_id)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('event.list'))

    return render_template('events/add.html', form=form)


@events_blueprint.route('/list')
def list():
    # Grab a list of events from database.
    events = Events.query.all()
    return render_template('events/list.html', events=events)


@events_blueprint.route('/list/<int:evt_id>')
def ev_detail(evt_id):
    # Grab a list of events from database.
    event = Events.query.get_or_404(evt_id)
    return render_template('events/event_detail.html', event=event)


@events_blueprint.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Events.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('event.list'))
    return render_template('events/delete.html', form=form)
