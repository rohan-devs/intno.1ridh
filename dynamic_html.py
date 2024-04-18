from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
data = {
    'property_name': 'Spacious Studio in City Center',
    'num_bed': 1,
    'num_bath': 1,
    'phone': '123-456-7890',
    'price': 1500,
    'agent_name': 'Rohan Shah',
    'requested_timeslot': [{
        '2022-12-01': '10:00 AM-2:00 PM',
        '2022-12-02': '11:00 AM-3:00 PM'
    }],
    'email_id': 'rohanshah6982@gmail.com',
    'requested_timeslot_date': '26th of March',
    'status': 'Declined by agent',
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
