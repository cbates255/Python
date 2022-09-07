import boto3
dynamodb=boto3.client("dynamodb")

response = dynamodb.batch_write_item(
    RequestItems={
        'Player_list': [
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jones',
                        },
                        'Number': {
                            'N': '1',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jackson',
                        },
                        'Number': {
                            'N': '2',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Johnson',
                        },
                        'Number': {
                            'N': '3',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jeffs',
                        },
                        'Number': {
                            'N': '4',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jerry',
                        },
                        'Number': {
                            'N': '5',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Joel',
                        },
                        'Number': {
                            'N': '6',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jeudy',
                        },
                        'Number': {
                            'N': '7',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jorge',
                        },
                        'Number': {
                            'N': '8',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jack',
                        },
                        'Number': {
                            'N': '9',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Player': {
                            'S': 'Jill',
                        },
                        'Number': {
                            'N': '10',
                        },
                    },
                },
            },
        ],
    },
)
