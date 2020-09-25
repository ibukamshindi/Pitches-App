from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitches, Comments
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db, photos


@main.route('/')
def index():
    """
    View root page function that returns index page and its data
    """

    title = 'Home- Welcome to the Pitch Website'
    pitches = Pitches.get_all_pitches()
    return render_template('index.html', title=title, pitches=pitches)

@main.route('/promotions')
def promotions():
    '''
    View promotions page function that returns the promotions page and its data
    '''
    pitches= Pitches.get_pitches_by_category(1)
    title = 'Promotions'
    return render_template('promotions.html', title = title, pitches = pitches)

@main.route('/pickup_lines')
def pickuplines():
    '''
    View pickuplines page function that returns the pickuplines page and its data
    '''
    pitches= Pitches.get_pitches_by_category(2)
    title = 'Pickup_lines'
    return render_template('pickup_lines.html', title = title, pitches = pitches)


@main.route('/interview')
def interview():
    '''
    View interview page function that returns the interviews page and its data
    '''
    pitches= Pitches.get_pitches_by_category(3)
    title = 'Interview'
    return render_template('interview.html', title = title, pitches = pitches)


# Route for adding a new pitch

@main.route('/new_pitch', methods=['GET', 'POST'])
# @login_required
def new_pitch():
    '''
    Function to check Pitches form
    '''
    form = PitchForm()
    # category = PitchCategory.query.filter_by(id=id).first()

    # if category is None:
    #     abort(404)

    if form.validate_on_submit():
        new_pitch = Pitches(category_id = form.category_id.data, actual_pitch = form.content.data)
        # new_pitch = Pitches(actual_pitch=actual_pitch,
        #                     category_id=category.id)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', pitch_form=form)

# Routes for displaying the different pitches


# @main.route('/category/<int:id>')
# def category(id):
#     '''
#     category route function returns a list of pitches in the category chosen
#     '''

#     category = PitchCategory.query.get(id)

#     if category is None:
#         abort(404)

#     pitches = Pitches.get_pitches(id)
#     return render_template('category.html', category=category, pitches=pitches)


# @main.route('/pitch/<int:id>', methods=['GET', 'POST'])
# @login_required
# def single_pitch(id):
#     '''
#     Function the returns a single pitch for comment to be added
#     '''

#     pitches = Pitches.query.get(id)

#     if pitches is None:
#         abort(404)

#     comment = Comments.get_comments(id)
#     return render_template('pitch.html', pitches=pitches, comment=comment)


# Routes for user authentication
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

# Route to add commments.


@main.route('/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular pitch
    '''
    form = CommentForm()
    pitches = Pitches.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        comment_id = form.comment_id.data
        new_comment = Comments(comment_id=comment_id,
                               user_id=current_user.id, pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.category', id=pitches.category_id))

    return render_template('comment.html', comment_form=form)