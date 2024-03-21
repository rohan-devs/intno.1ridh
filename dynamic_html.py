from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
data = {
    'title': 'Confirm your email address',
    'property_name': 'Spacious Studio in City Center',
    'num_bed': 1,
    'num_bath': 1,
    'price': 1500,
    'agent_name': 'Rohan Shah',
    'requested_timeslot': {
        '2022-12-01': ['09:00', '10:00'],
        '2022-12-02': ['11:00', '14:00'],
    },
    'email_id': 'rohanshah6982@gmail.com',
    'requested_timeslot': '2:00pm',
    'requested_timeslot_date': '26th of March',
    'status': 'Awaiting Confirmation',
    'reason': 'reason given by the landlord',
    'confirmed_time': '10:00 AM',
    'lockbox_info': 'Code: 12345, Location: Front door',
    'remarks': 'Please bring a valid ID and proof of income.',
    'cta_link': 'https://example.com/cancel-showing'
}


template = env.get_template('template.html')


output = template.render(data)


file = open('output.html', 'w')

file.write(output)

file.close()
