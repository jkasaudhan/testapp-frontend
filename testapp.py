#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The MIT License (MIT)
# Copyright (c) 2016 Nikola Kovacevic

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from operator import itemgetter

from flask import Flask, render_template, request, abort, jsonify

app = Flask(__name__)

MOCK_DATA = [
    {"id": 1, "gender": "Female", "first_name": "Carol", "last_name": "Ward", "email": "carol@example.com", "job_title": "Human Resources Manager"},
    {"id": 2, "gender": "Male", "first_name": "Pepe", "last_name": "Silvia", "email": "psilvia@web.org", "job_title": "Financial Advisor"},
    {"id": 3, "gender": "Male", "first_name": "Charlie", "last_name": "Kelley", "email": "dayman@paddys.com", "job_title": "Environmental Specialist"},
    {"id": 4, "gender": "Female", "first_name": "Lori", "last_name": "Lopez", "email": "llopez3@acquirethisname.com", "job_title": "Registered Nurse"},
    {"id": 5, "gender": "Male", "first_name": "Robert", "last_name": "Lopez", "email": "rlopez4@uol.com.br", "job_title": "Health Coach I"},
    {"id": 6, "gender": "Male", "first_name": "Nicholas", "last_name": "White", "email": "nwhite5@google.com", "job_title": "Help Desk Technician"},
    {"id": 7, "gender": "Male", "first_name": "Joe", "last_name": "Robertson", "email": "jrobertson6@google.fr", "job_title": "Safety Technician IV"},
    {"id": 8, "gender": "Female", "first_name": "Marie", "last_name": "Burton", "email": "mburton7@wired.com", "job_title": "Database Administrator II"},
    {"id": 9, "gender": "Male", "first_name": "Justin", "last_name": "Vasquez", "email": "jvasquez8@hibu.com", "job_title": "Automation Specialist II"},
    {"id": 10, "gender": "Male", "first_name": "Edward", "last_name": "Lee", "email": "elee9@cargocollective.com", "job_title": "Environmental Tech"},
    {"id": 11, "gender": "Male", "first_name": "Sean", "last_name": "Wheeler", "email": "swheelera@mail.ru", "job_title": "Internal Auditor"},
    {"id": 12, "gender": "Female", "first_name": "Judy", "last_name": "Hunt", "email": "jhuntb@opera.com", "job_title": "Assistant Professor"},
    {"id": 13, "gender": "Male", "first_name": "Russell", "last_name": "Kelly", "email": "rkellyc@e-recht24.de", "job_title": "Civil Engineer"},
    {"id": 14, "gender": "Female", "first_name": "Sharon", "last_name": "Owens", "email": "sowensd@tamu.edu", "job_title": "Research Associate"},
    {"id": 15, "gender": "Male", "first_name": "Joseph", "last_name": "Gilbert", "email": "jgilberte@sitemeter.com", "job_title": "Programmer IV"},
    {"id": 16, "gender": "Female", "first_name": "Nicole", "last_name": "Holmes", "email": "nholmesf@jalbum.net", "job_title": "Web Designer II"},
    {"id": 17, "gender": "Male", "first_name": "Roy", "last_name": "Brown", "email": "rbrowng@guardian.co.uk", "job_title": "Human Resources Manager"},
    {"id": 18, "gender": "Male", "first_name": "Todd", "last_name": "Stevens", "email": "tstevensh@ovh.net", "job_title": "Teacher"},
    {"id": 19, "gender": "Male", "first_name": "Willie", "last_name": "Crawford", "email": "wcrawfordi@nationalgeographic.com", "job_title": "VP Marketing"},
    {"id": 20, "gender": "Male", "first_name": "Billy", "last_name": "Webb", "email": "bwebbj@europa.eu", "job_title": "Sales Representative"},
    {"id": 21, "gender": "Female", "first_name": "Denise", "last_name": "Sanders", "email": "dsandersk@booking.com", "job_title": "Product Engineer"},
    {"id": 22, "gender": "Male", "first_name": "Jonathan", "last_name": "Willis", "email": "jwillisl@google.com.hk", "job_title": "Information Systems Manager"},
    {"id": 23, "gender": "Female", "first_name": "Joan", "last_name": "Greene", "email": "jgreenem@trellian.com", "job_title": "Marketing Assistant"},
    {"id": 24, "gender": "Female", "first_name": "Sandra", "last_name": "Larson", "email": "slarsonn@wordpress.org", "job_title": "Sales Associate"},
    {"id": 25, "gender": "Female", "first_name": "Janice", "last_name": "Arnold", "email": "jarnoldo@webnode.com", "job_title": "Programmer I"},
]


@app.route('/')
def home():
    return render_template("home.html", users=MOCK_DATA)


@app.route('/view/<int:person_id>')
def view_person(person_id):
    for person in MOCK_DATA:
        if person['id'] == person_id:
            return render_template("view.html", person=person)

    abort(404)


def __sort_list(unsorted_list, request):
    """
    Internal function for sorting a list of items, separted
    so that we can apply the same logic to search function.
    :param unsorted_list: list to be sorted
    :param request: request with the necessary arguments
    :return: response
    """
    available_keys_to_sort = MOCK_DATA[0].keys()
    if not request.args or 'sort_by' not in request.args:
        abort(400)

    if request.args['sort_by'] not in available_keys_to_sort:
        abort(400)

    order = 'asc'
    if 'order' in request.args:
        if request.args['order'] not in ['asc', 'desc']:
            abort(400)
        order = request.args['order']

    sorted_list = sorted(unsorted_list, key=itemgetter(request.args['sort_by']))

    if order == 'desc':
        sorted_list.reverse()

    return jsonify({'results': sorted_list})


@app.route('/api/v1/search/', methods=['GET'])
def get_results():
    """
    This is a very basic implementation of a search function that will
    go over all attributes of the person and if the attribute contains
    the search query in it the object will be appended to the ist of results
    at the end the jsonified list is returned

    Example:
        > $ http GET http://127.0.0.1:5000/api/v1/search/ query=Carol
        HTTP/1.0 200 OK
        Content-Length: 225
        Content-Type: application/json
        Date: Sat, 11 Jun 2016 14:40:52 GMT
        Server: Werkzeug/0.11.10 Python/2.7.11

        {
            "results": [
                {
                    "email": "cward0@techcrunch.com",
                    "first_name": "Carol",
                    "gender": "Female",
                    "id": 1,
                    "job_title": "Physical Therapy Assistant",
                    "last_name": "Ward"
                }
            ]
        }

    :rtype: dict
    """
    if not request.args or 'query' not in request.args:
        abort(400)

    query = request.args['query']
    result_list = []
    for person in MOCK_DATA:
        for person_attribute in person.values():

            if type(person_attribute) == int:
                # To allow us to search by ID which is an int
                person_attribute = str(person_attribute)

            if query.lower() in person_attribute.lower():
                result_list.append(person)
                break

    if 'sort_by' in request.args:
        return __sort_list(result_list, request)

    return jsonify({'results': result_list})


@app.route('/api/v1/sort/', methods=['GET'])
def sort_table():
    """
    Example:
        > $ http GET http://127.0.0.1:5000/api/v1/sort/ sort_by="id" order="desc"
        HTTP/1.0 200 OK
        Content-Length: 4956
        Content-Type: application/json
        Date: Sat, 11 Jun 2016 15:54:16 GMT
        Server: Werkzeug/0.11.10 Python/2.7.11

        {
            "results": [
                {
                    "email": "jarnoldo@webnode.com",
                    "first_name": "Janice",
                    "gender": "Female",
                    "id": 25,
                    "job_title": "Programmer I",
                    "last_name": "Arnold"
                },
                ...
            ]
        }

    :return:
    """
    return __sort_list(MOCK_DATA, request)


if __name__ == '__main__':
    app.run()
