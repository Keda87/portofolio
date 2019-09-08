from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    experience = (datetime.now() - datetime(year=2014, month=10, day=1)).days
    experience = int(experience / 360)
    list_experience = [
        {
            'year_info': 'Mar 2019-Present',
            'company': 'Tanihub',
            'role': 'Software Engineer',
            'description': ('Having fun with Go, NodeJS and React')
        },
        {
            'year_info': 'Mar 2017-Mar 2019',
            'company': '88Spares.com',
            'role': 'Backend Engineer',
            'description': ('- Building web API\n'
                            '- Improve and refactor the current codebase.\n'
                            '- Implement automated testing from the legacy project that had 0 coverage into around 70% coverage.\n'
                            '- Building several support services API such us (notification, shipping, payment, logging)\n'
                            '- Managing pull request and staging deployment\n'
                            '- Managing sentry and distributing bug ticket\n'
                            '- Currently, extract current monolith architecture into microservices.')
        },
        {
            'year_info': 'Jan 2016-Feb 2017',
            'company': 'Oprent.com',
            'role': 'Backend Engineer',
            'description': ('Building web API, internal tools for analytic '
                            'dashboard and third party integration to main '
                            'platform.')
        },
        {
            'year_info': 'Nov 2015-Jan 2016',
            'company': 'Kargo.co.id',
            'role': 'Backend & Android Developer',
            'description': ('Provide MVP product for backend service and '
                            'android client both for driver and customer.')
        },
        {
            'year_info': 'Oct 2014-Jan 2016',
            'company': 'PT. Polatic Informatika Indonesia',
            'role': 'Software Engineer',
            'description': ('Responsible to develop backend system, improvement,'
                            ' optimization and bug fixing to a project from '
                            'various clients.')
        },
        {
            'year_info': 'Aug 2012-Jan 2014',
            'company': 'Telkom University',
            'role': 'Practicum Assistant',
            'description': ('Assigned to be practicum assistant of Java Object '
                            'Oriented Programming course on 3rd semester and '
                            'assigned as Java EE practicum assistant on 5th '
                            'semester.')
        },
        {
            'year_info': 'May 2013-Jul 2013',
            'company': 'PT. Neuronworks Indonesia',
            'role': 'Intern',
            'description': ('Tester and Bug fixing in business process and user '
                            'interface on EOFFICE Online Memo web based '
                            'application.')
        }
    ]

    context = {
        'experience': experience,
        'list_experience': list_experience,
    }
    return render_template('civic/index.html', **context)
