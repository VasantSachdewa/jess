JOB_DETAIL_DATA = {
    "job_id": "random_id",
    "page_url": "https://www.random.com",
    "salary_min": None,
    "salary_max": None,
    "currency": None,
    "job_title": "Software Engineer",
    "company": "Random limited",
    "post_date": "2021-07-03T17:57:44.942851+07:00",
    "job_description": [
        "Best developer in the world",
        "C++ programmer," "DevOps Experience",
    ],
    "job_requirements": [
        "Build new features on Apple webpage",
        "Build" " features on Siri",
        "Work on security features",
    ],
    "benefits": [
        "Best salary in the world",
        "200 days paid holiday",
        "Cover dentist charges",
    ],
    "industry": "Technology",
}

LAMBDA_PAYLOAD = {
    'Records': [{
        'EventSource': 'aws:sns',
    'EventVersion': '1.0',
    'EventSubscriptionArn': 'arn:aws:sns:ap-southeast-1:640734209900:new_jobs:2403f760-9459-4320-8dd4-5f71b7f4c68f',
    'Sns': {'Type': 'Notification',
        'MessageId': 'b2151019-26cd-528d-9086-4976b6aa51fd',
        'TopicArn': 'arn:aws:sns:ap-southeast-1:640734209900:new_jobs',
        'Subject': None,
        'Message': '{"vendor_id": 1, "message": ["this is a test message"]}',
        'Timestamp': '2021-07-19T14:37:27.451Z',
        'SignatureVersion': '1',
        'Signature': 'lkbXTq/bTz1rSkIPVrk+837yb0D7WLysS9bXCklG10mj9b0ZalY5qXMKmFDhswbX+930yiqf2qUdmbSDwpGPbJ+bUzIPQO0ZqM+tkTVvG2Ze/NQj+NsPerdEbaI9QghCNI9CEoGwGFTreEwDfBfvN0Q8txJbfMSDmAAIb1IyZGJHSW5X/Iuqd16M9UpOWMYNZGbnFIMDZVy62Gk6FsOGuOK+MFtaIfC49uhL05iWIEE4fk9OHnFmBcZugdnVLIe+KwiEvRbYZ2caXbgnfYXI96i3F80+dLK1OaFU1HkCsTbtku3PiBF3DE5242MjuqWUwGgSUqqgZa+yUUgVIaxnXg==',
        'SigningCertUrl': 'https://sns.ap-southeast-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem',
        'UnsubscribeUrl': 'https://sns.ap-southeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-1:640734209900:new_jobs:2403f760-9459-4320-8dd4-5f71b7f4c68f',
        'MessageAttributes': {}}}
    ]
}