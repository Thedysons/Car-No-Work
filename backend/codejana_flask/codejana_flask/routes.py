from codejana_flask import app, db
from flask import render_template, url_for, redirect, flash, request
from codejana_flask.forms import SignUpForm, LoginForm, RequestHelpForm, PaymentOption, MockCreditCardPayment
from codejana_flask.models import User

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='Home')

@app.route('/about')
def about():
    return render_template('About.html',title='About')

@app.route('/account')
def account():
    return render_template('Account.html',title='Account')


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    form=SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}', category="success")
        return redirect(url_for('login'))
    return render_template('signUp.html', title='Sign Up', form=form)


user_emails = []

@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    # if form.validate_on_submit():
    #     user=User.query.filter_by(email=form.email.data).first()
    #     if form.email.data==user.email and form.password.data==user.password:
    #         user_emails.append(form.email.data)
    #         if form.email.data[-13:] == '@mechanic.com':
    #             # flash(f'Log in successful for {form.email.data}', category='success')
    #             return redirect(url_for('rapProfile'))
    #         # if log in is client, go to client profile
    #         else:
    #             # flash(f'Login successfull for {form.email.data}', category='success')
    #             return redirect(url_for('clientProfile'))
            # __________



    if request.method == "POST":
        
        user=User.query.filter_by(email=form.email.data).first()
        if form.email.data==user.email and form.password.data==user.password:
            if form.email.data[-13:] == '@mechanic.com':
                # flash(f'Log in successful for {form.email.data}', category='success')
                return redirect(url_for('rapProfile'))
            # if log in is client, go to client profile
            else:
                # flash(f'Login successfull for {form.email.data}', category='success')
                user_emails.append(request.form.get('email') )
                return redirect(url_for('clientProfile'))
                
        else:
            flash(f'Login unsuccessfull for {form.email.data}', category='danger')
            return redirect(url_for('login'))
        
 
    return render_template('login.html', title='Login', form=form)

request_info = []
@app.route('/requestHelp', methods=['POST', 'GET'])
def requestHelp():
    form=RequestHelpForm()
    # if form.validate_on_submit():
    #     request_info.append([form.problem_description.data, form.location.data, form.plate_number.data, form.car_model.data])
    #     return redirect(url_for('requestHelp2'))

    if request.method == "POST":
        # request_info.append ((
        #     request.form.get('problem_description'), request.form.get('location'), request.form.get('plate_number'), request.form.get('car_model')
        # ))
        request_info.append ([
            request.form.get('problem_description'), request.form.get('location'), request.form.get('plate_number'), request.form.get('car_model'), 'Searching for Mechanic'
        ])
        return redirect(url_for('requestHelp2'))
    return render_template('requestHelp.html',title='requestHelp', form=form)

@app.route('/requestHelp2', methods=['POST', 'GET'])
def requestHelp2():
    form=PaymentOption()
    if form.validate_on_submit():
        if form.payment_option.data == 'Membership':
            flash(f'Payent option is membership', category='success')
            return redirect(url_for('membership'))
        elif form.payment_option.data == 'Plan Membership':
            flash(f'Payent option is one off', category='success')
            return redirect(url_for('one_off_payment'))
        else:
             return redirect(url_for('one_off_payment'))
    return render_template('requestHelp2.html',title='requestHelp2', form=form)

@app.route('/membership', methods=['POST', 'GET'])
def membership():
    form=MockCreditCardPayment()
    if form.validate_on_submit():
        return redirect(url_for('confirm_payment'))
    return render_template('membership.html',title='membership', form=form)

@app.route('/one_off_payment', methods=['POST', 'GET'])
def one_off_payment():
    form=MockCreditCardPayment()
    if form.validate_on_submit():
        return redirect(url_for('confirm_payment'))
    return render_template('oneOffPayment.html',title='membership', form=form)

@app.route('/confirm_payment', methods=['POST', 'GET'])
def confirm_payment():
    return render_template('confirmOffPayment.html',title='membership')

@app.route('/rapProfile')
def rapProfile():
    return render_template('rapProfile.html', title='rapProfile')

@app.route('/clientProfile')
def clientProfile():
    return render_template('clientProfile.html', emails=user_emails, title='clientProfile')

@app.route('/claim_progress', methods=['POST', 'GET'])
def claim_progress():
    return render_template('claimProgress.html', entries=request_info, title='Claim Progress')

@app.route('/claim_history', methods=['POST', 'GET'])
def claim_history():
    return render_template('claimHistory.html', entries=request_info, title='Claim History')

@app.route('/viewRequests',  methods=['POST', 'GET'])
def viewRequests():
     return render_template('viewRequests.html', entries=request_info, title='View Requests')


# @app.route('/requestHelp')
# def requestHelp():
#     return render_template('requestHelp.html',title='requestHelp')