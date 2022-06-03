from codejana_flask import app, db
from flask import render_template, url_for, redirect, flash, request
from codejana_flask.forms import SignUpForm, LoginForm, RequestHelpForm, PaymentOption, MockCreditCardPayment, TakeJobForm, StartJobForm, arrivedForm, finishJobForm, completeJobForm, forgotPasswordForm, ratingForm
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

# array used
request_info = []   # this will hold requests made by users
rap_jobs = []   # this will hold requests by users but specifically made to be seen by mechanics
rap_jobs_taken = []
job_started = []
arrival = []
job_completed=[]
requests_completed=[]
user_emails = []
current_client = ['sam@dot.com']
current_rap = ['bob@mechanic.com']

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
                current_rap.append(request.form.get('email'))
                return redirect(url_for('rapProfile'))
            # if log in is client, go to client profile
            else:
                # flash(f'Login successfull for {form.email.data}', category='success')
                # user_emails.append(request.form.get('email'))
                current_client.append(request.form.get('email'))
                return redirect(url_for('clientProfile'))
                
        else:
            flash(f'Login unsuccessfull for {form.email.data}', category='danger')
            return redirect(url_for('login'))
        
 
    return render_template('login.html', title='Login', form=form)

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
            current_client[-1], request.form.get('problem_description'), request.form.get('location'), request.form.get('plate_number'), request.form.get('car_model'), 'Searching for Mechanic'
        ])
        rap_jobs.append ([
            current_client[-1], request.form.get('problem_description'), request.form.get('location'), request.form.get('plate_number'), request.form.get('car_model'), 'Searching for Mechanic'
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
    return render_template('rapProfile.html', current_rap=current_rap, title='rapProfile')


@app.route('/clientProfile')
def clientProfile():
    return render_template('clientProfile.html', current_client=current_client, title='clientProfile')

@app.route('/claim_progress', methods=['POST', 'GET'])
def claim_progress():
    return render_template('claimProgress.html', entries=request_info, current_client=current_client, title='Claim Progress')

@app.route('/claim_history', methods=['POST', 'GET'])
def claim_history():
    return render_template('claimHistory.html', entries=request_info, current_client=current_client, title='Claim History')

@app.route('/viewRequests',  methods=['POST', 'GET'])
def viewRequests():
    form = TakeJobForm()
    if request.method == "POST":
        if form.accept_job.data != '':
            index = int(request.form.get('accept_job')) -1
            request_info[index][-1] = 'Mechanic found'
            rap_jobs[index][-1] = "You have taken this job"
            rap_jobs_taken.append([rap_jobs[index][0], rap_jobs[index][1], rap_jobs[index][2], rap_jobs[index][3], rap_jobs[index][4], rap_jobs[index][5], current_rap[-1]])
        if form.decline_job.data != '':
            index = int(request.form.get('decline_job')) -1
            rap_jobs.pop(index)
        
    return render_template('viewRequests.html', entries=request_info, jobs=rap_jobs, title='View Requests', form=form)

@app.route('/currentJobs', methods=['POST', 'GET'])
def currentJobs():
    return render_template('currentJobs.html', current=rap_jobs_taken, current_rap=current_rap, title='Current Jobs')

@app.route('/startJob', methods=['POST', 'GET'])
def startJob():
    start_form = StartJobForm()
    if request.method == "POST":
        job_started.append([request.form.get('distance'), request.form.get('location'), request.form.get('time'), request.form.get('name')])
        return redirect(url_for('jobProgress'))
    return render_template('startJob.html', current=rap_jobs_taken, title='Start Job', start_form=start_form)

@app.route('/startJobConfirmation', methods=['POST', 'GET'])
def startJobConfirmation():
    return render_template('startJobConfirmation.html', job_started=job_started, title='Start Job Confirmation')

@app.route('/clientNotifications', methods=['POST', 'GET'])
def clientNotifications():
    return render_template('clientNotifications.html', job_started=job_started, arrival=arrival, title='Your notifications')

@app.route('/jobProgress', methods=['GET','POST'])
def jobProgress():
    arrived = arrivedForm()
    finish = finishJobForm()
    if arrived.validate_on_submit():
        flash(f'Client has been notified that you have arrived', category='success')
        arrival.append('Assitance have arrived to your location')
    
    return render_template('jobProgress.html', current=rap_jobs_taken, arrival=arrival, title='Progress of current job', arrived=arrived, finish=finish)


@app.route('/jobComplete', methods=['POST', 'GET'])
def jobComplete():
    jobCompleted= completeJobForm()
    if jobCompleted.validate_on_submit():
        # job_completed consists of the client's problem, the client's location, client's plate number, client's model, final report submitted, and rating
        job_completed.append([rap_jobs_taken[0][0], rap_jobs_taken[0][1], rap_jobs_taken[0][2], rap_jobs_taken[0][3],  rap_jobs_taken[0][4], request.form.get('report'), 'No rating submited', current_rap[-1]])

        requests_completed.append([rap_jobs_taken[0][0], rap_jobs_taken[0][1], rap_jobs_taken[0][2], rap_jobs_taken[0][3], rap_jobs_taken[0][4], request.form.get('report'), 'No rating submited'])
        flash(f'You have completed this job, good job.', category='success')
    return render_template('jobComplete.html', current=rap_jobs_taken, title='Job complete', jobCompleted=jobCompleted)

@app.route('/historyOfRequests', methods=['POST', 'GET'])
def historyOfRequests():
    return render_template('historyOfRequests.html', requests_completed=requests_completed, current_client=current_client, title='History of requests')

@app.route('/historyOfJobs', methods=['POST', 'GET'])
def historyOfJobs():
    return render_template('historyOfJobs.html', jh=job_completed, current_rap=current_rap, title='History of jobs')

@app.route('/plansAndPrices', methods=['POST', 'GET'])
def plansAndPrices():
    return render_template('plansAndPrices.html', title='Plans and Prices')

@app.route('/help', methods=['POST', 'GET'])
def help():
    return render_template('help.html', title='Help Page')

@app.route('/guest', methods=['POST', 'GET'])
def guest():
    return render_template('guest.html', title='Guest Page')

@app.route('/forgotPassword', methods=['POST', 'GET'])
def forgotPassword():
    forgotPassword=forgotPasswordForm()
    if forgotPassword.validate_on_submit():
        flash(f'Details to reset your password has been sent to your email', category='success')
    return render_template('forgotPassword.html', title='Forgot Password', forgotPassword=forgotPassword)

@app.route('/ratings', methods=['POST', 'GET'])
def ratings():
    rating=ratingForm()
    if rating.validate_on_submit():
        if rating.job_number.data != '':
            index = int(request.form.get('job_number')) -1
            if rating.give_rating.data != '':
                requests_completed[index][-1] = request.form.get('give_rating')
                job_completed[index][-2] = request.form.get('give_rating')
    return render_template('ratings.html', requests_completed=requests_completed, title='Ratings page', rating=rating)

@app.route('/download', methods=['POST', 'GET'])
def download():
    return render_template('download.html', title='Download page')