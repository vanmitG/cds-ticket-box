from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from src import db
# from src.components.ticket_comp.forms import BuyForm
# from src.models.ticket import Tickets

tickets_blueprint = Blueprint('ticket_blt',
                              __name__,
                              template_folder='../../templates')


@tickets_blueprint.route('/buy/<int:evt_id>', methods=['GET', 'POST'])
@login_required
def buy(evt_id):
    # form = BuyForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     description = form.description.data
    #     image_url = form.image_url.data
    #     price = form.price.data
    #     address = form.address.data
    #     time = form.time.data
    #     organizer_id = current_user.id
    #     # Add new Event to database
    #     new_pup = Events(name=name, description=description, image_url=image_url,
    #                      price=price, address=address, time=time, organizer_id=organizer_id)
    #     db.session.add(new_pup)
    #     db.session.commit()
    #     return redirect(url_for('event.list'))

    return render_template('tickets/buy_ticket.html', evt_id=evt_id)
