EXISTING_CHANNEL = 'existing-channel'

MESSAGES = [
    'some string',
    123,
    3.14,
    {'a': 1, 'b': 2, 'c': 3},
    None,
]
CHANNEL_NAMES = [
    EXISTING_CHANNEL,
    # 'new-channel',
]


def gen_test_mk_msg_broker_args():
    for msg in MESSAGES:
        for queue in CHANNEL_NAMES:
            yield (msg, queue)
