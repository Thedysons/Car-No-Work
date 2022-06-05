from codejana_flask import app, db
from flask import render_template, url_for, redirect, flash, request
# from codejana_flask.codejana_flask.forms import downloadForm
from codejana_flask.forms import SignUpForm, LoginForm, RequestHelpForm, PaymentOption, MockCreditCardPayment, TakeJobForm, StartJobForm, arrivedForm, finishJobForm, completeJobForm, forgotPasswordForm, ratingForm, downloadForm
from codejana_flask.models import User
from sqlalchemy.exc import IntegrityError

# the route for the home page
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='Home')

# the route for the about page
@app.route('/about')
def about():
    return render_template('About.html',title='About')

# the route for the account page which is not used in final production
@app.route('/account')
def account():
    return render_template('Account.html',title='Account')

# route for the sign up page
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    # declaring the sign up form
    form=SignUpForm()
    # try to sign up user if user has not 
    try:
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created successfully for {form.username.data}', category="success")
            return redirect(url_for('login'))
    except IntegrityError as e:
        flash(f'{form.email.data} already exists', category="danger")
        return redirect(url_for('sign_up'))
    return render_template('signUp.html', title='Sign Up', form=form)

# array used
request_info = []   # this will hold requests made by users
rap_jobs = []   # this will hold requests by users but specifically made to be seen by mechanics
rap_jobs_taken = []
job_started = []
arrival = []
job_completed = []
job_completed=  [
                    ['sam@dot.com', 'Flat Tire', 'NSW', '1234', 'Mazda', 'Tire fixed.', '5', 'bob@mechanic.com'], ['raveena@dot.com', 'Drove my car into a lake', 'NSW', '8189', 'BMW i4', 'Car Towed back to the shop to drain all the water out of it.', '5', 'bob@mechanic.com'],
                    ['jack@dot.com', 'Ran out of fuel', 'NSW', '4321', 'Toyota Supra', 'Filled up clients car with E10 to full', '3', 'bob@mechanic.com'], ['keegan@dot.com', 'Flat Tire', 'NSW', '1234', 'Mazda', 'Tire fixed.', '5', 'bob@mechanic.com'],
                    ['tom@dot.com', 'Flat Car Battery', 'NSW', '0010', 'Honda Jazz', 'Battery Replaced', '4.8', 'bob@mechanic.com'], ['ludy@dot.com', 'Drove into a pole and smahed a headlight', 'NSW', '2001', 'VW ID Buzz', 'Headlight fixed.', '2.1', 'bob@mechanic.com'],
                    ['sam2@dot.com', 'Flat Tire', 'NSW', '1234', 'Mazda', 'Tire fixed.', '5', 'jeff@mechanic.com'], ['raveena2@dot.com', 'Drove my car into a lake', 'NSW', '8189', 'BMW i4', 'Car Towed back to the shop to drain all the water out of it.', '5', 'jeff@mechanic.com'],
                    ['jack2@dot.com', 'Ran out of fuel', 'NSW', '4321', 'Toyota Supra', 'Filled up clients car with E10 to full', '5', 'jeff@mechanic.com'], ['keegan2@dot.com', 'Flat Tire', 'NSW', '1234', 'Mazda', 'Tire fixed.', '5', 'jeff@mechanic.com'],
                    ['tom2@dot.com', 'Flat Car Battery', 'NSW', '0010', 'Honda Jazz', 'Battery Replaced', '4.8', 'jeff@mechanic.com'], ['ludy2@dot.com', 'Drove into a pole and smahed a headlight', 'NSW', '2001', 'VW ID Buzz', 'Headlight fixed.', '2.1', 'jeff@mechanic.com'],
                    ['sam3@dot.com', 'Flat Tire', 'NSW', '1234', 'Mazda', 'Tire fixed.', '5', 'jim@mechanic.com'], ['raveena3@dot.com', 'Drove my car into a lake', 'NSW', '8189', 'BMW i4', 'Car Towed back to the shop to drain all the water out of it.', '5', 'jim@mechanic.com'],
                    ['jack3@dot.com', 'Ran out of fuel', 'NSW', '4321', 'Toyota Supra', 'Filled up clients car with E10 to full', '5', 'jim@mechanic.com'], ['keegan3@dot.com', 'Flat Tire', 'NSW', '1234', 'Mazda', 'Tire fixed.', '5', 'jim@mechanic.com'],
                    ['tom3@dot.com', 'Flat Car Battery', 'NSW', '0010', 'Honda Jazz', 'Battery Replaced', '4.8', 'jim@mechanic.com'], ['ludy3@dot.com', 'Drove into a pole and smahed a headlight', 'NSW', '2001', 'VW ID Buzz', 'Headlight fixed.', '2.1', 'jim@mechanic.com'],
                    ['ludy4@dot.com', 'Car turned into a motorbike', 'QLD', '000', 'Spaceship 3000', 'Motorbike is cool, so nothing was changed.', '5', 'johnny@mechanic.com'],
                    ['sam4@dot.com', 'Car Exploded', 'UOW campus', 'b00m', 'Tesla Model 3', 'Built Car in lego parts from scratch', '4.5', 'johnny@mechanic.com']
                ]
requests_completed=[]
user_emails = []
current_client = ['sam@dot.com']
current_rap = ['bob@mechanic.com']
client_notifications = []

@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    try:
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
    except AttributeError as e:
        flash(f'{form.email.data} does not have an account, please check the email and try again or sign up', category='danger')
        return redirect(url_for('login'))

        
 
    return render_template('login.html', title='Login', form=form)

@app.route('/requestHelp', methods=['POST', 'GET'])
def requestHelp():
    form=RequestHelpForm()
    if request.method == "POST":
        if (len(request_info) == 0) or (any(current_client[-1] not in sublist for sublist in request_info)):
            request_info.append ([
                current_client[-1], request.form.get('problem_description'), request.form.get('location'), request.form.get('plate_number'), request.form.get('car_model'), 'Searching for Mechanic'
            ])
            rap_jobs.append ([
                current_client[-1], request.form.get('problem_description'), request.form.get('location'), request.form.get('plate_number'), request.form.get('car_model'), 'Searching for Mechanic'
            ])
            return redirect(url_for('requestHelp2'))
        elif (len(request_info) > 0) and (any(current_client[-1] in sublist for sublist in request_info)):
            flash(f'You have already made a request, you cannot make more than one request at a time', category='danger')
            return redirect(url_for('requestHelp'))
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
        if (len(rap_jobs_taken) == 0) or (any(current_rap[-1] not in sublist for sublist in rap_jobs_taken)):
            if form.accept_job.data != '':
                try:
                    if int(request.form.get('accept_job')) <= len(request_info):
                        index = int(request.form.get('accept_job')) -1
                        request_info[index][-1] = 'Mechanic found'
                        rap_jobs[index][-1] = current_rap[-1] + " has taken this job"
                        # format of rap_jobs_taken: clients email, problem, location of client, plate number, car model, progress, current mechanic online
                        rap_jobs_taken.append([rap_jobs[index][0], rap_jobs[index][1], rap_jobs[index][2], rap_jobs[index][3], rap_jobs[index][4], rap_jobs[index][5], current_rap[-1]])
                    else:
                        flash(f'You have entered an invalid job ID, please try again', category='danger')
                except ValueError as e:
                    flash(f'Please enter a whole integer (e.g. 1)', category='danger')
            
            if form.decline_job.data != '':
                try:
                    if int(request.form.get('decline_job')) <= len(request_info):
                        index = int(request.form.get('decline_job')) -1
                        rap_jobs.pop(index)
                    else:
                        flash(f'You have entered an invalid job ID, please try again', category='danger')
                except ValueError as e:
                    flash(f'Please enter a whole integer (e.g. 1)', category='danger')

        elif (len(rap_jobs_taken) > 0) and (any(current_rap[-1] in sublist for sublist in rap_jobs_taken)):
            flash(f'You have already accepted a job, you cannot take more than one job at a time', category='danger')
        
    return render_template('viewRequests.html', entries=request_info, jobs=rap_jobs, title='View Requests', form=form)

@app.route('/currentJobs', methods=['POST', 'GET'])
def currentJobs():
    return render_template('currentJobs.html', current=rap_jobs_taken, current_rap=current_rap, title='Current Jobs')

@app.route('/startJob', methods=['POST', 'GET'])
def startJob():
    start_form = StartJobForm()
    if request.method == "POST":
        job_started.append([request.form.get('distance'), request.form.get('location'), request.form.get('time'), request.form.get('name')])
        for i in rap_jobs_taken:
            if i[-1] == current_rap[-1]:
                client_notifications.append([i[0], request.form.get('distance'), request.form.get('location'), request.form.get('time'), request.form.get('name')])
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
    
    return render_template('jobProgress.html', current=rap_jobs_taken, arrival=arrival, client_notifications=client_notifications, title='Progress of current job', arrived=arrived, finish=finish)


@app.route('/jobComplete', methods=['POST', 'GET'])
def jobComplete():
    jobCompleted= completeJobForm()
    if jobCompleted.validate_on_submit():
        # job_completed consists of the client's email, client's problem, the client's location, client's plate number, client's model, final report submitted, rating, and current mechanic online
        job_completed.append([rap_jobs_taken[0][0], rap_jobs_taken[0][1], rap_jobs_taken[0][2], rap_jobs_taken[0][3],  rap_jobs_taken[0][4], request.form.get('report'), 'No rating submited', current_rap[-1]])

        requests_completed.append([rap_jobs_taken[0][0], rap_jobs_taken[0][1], rap_jobs_taken[0][2], rap_jobs_taken[0][3], rap_jobs_taken[0][4], request.form.get('report'), 'No rating submited', rap_jobs_taken[0][-1]])
        
        if any(current_rap[-1] in sublist for sublist in job_completed) and any(current_rap[-1] in sublist for sublist in rap_jobs_taken):
            # for finished job(s) in the jobs completed by the mechanic
            for finished_job in job_completed:
                # for requests jobs in which the mechanic has accepted
                for job_accepted in rap_jobs_taken:
                    # if finished job equals the job accepted by the mecahnic
                    # what could be the problem: finished_job and job_accepted have different elements so they will never be equal, try to compare the individual elements
                    if (finished_job[0] == job_accepted[0]) and (finished_job[1] == job_accepted[1]) and (finished_job[2] == job_accepted[2]) and (finished_job[2] == job_accepted[2]) and (finished_job[3] == job_accepted[3]) and (finished_job[4] == job_accepted[4]) and (finished_job[-1] == current_rap[-1]):
                        rap_jobs_taken.remove(job_accepted)
        
        if any(current_client[-1] in sublist for sublist in requests_completed) and any(current_client[-1] in sublist for sublist in request_info):
            pass
            for request_ in request_info:
                for completed_request in requests_completed:
                    if (request_[0]==completed_request[0]) and (request_[1]==completed_request[1]) and (request_[2]==completed_request[2]) and (request_[3]==completed_request[3]) and (request_[4]==completed_request[4]):
                        request_info.remove(request_)


        flash(f'You have completed this job, good job. Please check History of jobs to check information of your recent job(s).', category='success')
    return render_template('jobComplete.html', current=rap_jobs_taken, title='Job complete', jobCompleted=jobCompleted)

@app.route('/historyOfRequests', methods=['POST', 'GET'])
def historyOfRequests():
    return render_template('historyOfRequests.html', requests_completed=requests_completed, current_client=current_client, request_info=request_info, title='History of requests')

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
            try:
                if rating.give_rating.data != '':
                    if int(request.form.get('job_number')) <= len(requests_completed):
                        index = int(request.form.get('job_number')) -1
                        if requests_completed[index][0] == current_client[-1]:
                            requests_completed[index][-2] = request.form.get('give_rating')
                            job_completed[index][-2] = request.form.get('give_rating')
                        else:
                            flash(f'You have entered an invalid job ID, please try again', category='danger')
                    elif int(request.form.get('job_number')) > len(requests_completed):
                        flash(f'You have entered an invalid job ID, please try again', category='danger')
            except ValueError as e:
                    flash(f'Please enter a whole integer (e.g. 1)', category='danger')
    return render_template('ratings.html', requests_completed=requests_completed, title='Ratings page', rating=rating)

@app.route('/download', methods=['POST', 'GET'])
def download():
    download_ = downloadForm()
    if download_.validate_on_submit():
        flash(f'You have downloaded a txt file.', category='success')
    return render_template('download.html', requests_completed=requests_completed, title='Download page', download_=download_)