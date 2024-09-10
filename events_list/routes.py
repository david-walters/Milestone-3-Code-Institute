from flask import render_template, request, redirect, url_for, flash
from events_list import app, db

from events_list.models import Event

@app.route('/add_event', methods=['POST'])
def add_event():
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        city = request.form.get('city')
        description = request.form.get('description')
        event_date = request.form.get('event_date')

        new_event = Event(event_name=event_name, city=city, description=description, event_date=event_date)

        try:
            db.session.add(new_event)
            db.session.commit()
            flash('Event added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding event: {str(e)}', 'danger')

        return redirect(url_for('index'))

@app.route('/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        event.city = request.form['city']
        event.event_name = request.form['event_name']
        event.description = request.form['description']
        event.event_date = request.form['event_date']
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('modal_edit_event.html', event=event)

@app.route('/')
def index():
    
    events = Event.query.all()

    return render_template('index.html', events=events)