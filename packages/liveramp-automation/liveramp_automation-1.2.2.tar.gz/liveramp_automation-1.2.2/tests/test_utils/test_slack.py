import base64
from unittest.mock import Mock

import pytest
from liveramp_automation.utils.slack import SlackHTMLParser, WebhookResponse, SlackWebhook, SlackBot

WEBHOOK_URL = "aHR0cHM6Ly9ob29rcy5zbGFjay5jb20vc2VydmljZXMvVDI4SkVROVJWL0IwM0xURFg3WlFTL3dNaE5TOFpyS3hQQWthQ0VIcW9YazhDbw=="
# BOT_USER = "eG94Yi03NjYyNjgyNTg3OS0zMzU3MjM2MjU5MzkyLTAzYlBDMmZleUhIa21Gc3ExNXc5dzFocw=="
BOT_USER = "eG94Yi03NjYyNjgyNTg3OS0yNTMzNjM0MzU3MzE0LWhtbVlRbWV2aHBrRHpZVnVEd3M4TEJ6RA=="

CHANNEL_NAME = "qe_test"
CHANNEL_ID = "C02N5KK61GR"
TEST_MESSAGE = "This is an test message"
TEST_MESSAGE_REPLY = "This is another test message"
MESSAGE_SIZE = 2

html_string_sample = '''
    <p>
        Here <i>is</i> a <strike>paragraph</strike> with a <b>lot</b> of formatting.
    </p>
    <br>
    <code>Code sample</code> & testing escape.
    <ul>
        <li>
            <a href="https://www.google.com">Google</a>
        </li>
        <li>
            <a href="https://www.amazon.com">Amazon</a>
        </li>
    </ul>
'''
blocks_sample = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "New request"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Type:*\nPaid Time Off"
            },
            {
                "type": "mrkdwn",
                "text": "*Created by:*\n<example.com|Fred Enriquez>"
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*When:*\nAug 10 - Aug 13"
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "<https://example.com|View request>"
        }
    }
]

attachments_sample = [
    {
        "fallback": "Plain-text summary of the attachment.",
        "color": "#2eb886",
        "pretext": "Optional text that appears above the attachment block",
        "author_name": "Bobby Tables",
        "author_link": "https://flickr.com/bobby/",
        "author_icon": "https://flickr.com/icons/bobby.jpg",
        "title": "Slack API Documentation",
        "title_link": "https://api.slack.com/",
        "text": "Optional text that appears within the attachment",
        "fields": [
            {
                "title": "Priority",
                "value": "High",
                "short": False
            }
        ],
        "image_url": "https://my-website.com/path/to/image.jpg",
        "thumb_url": "https://example.com/path/to/thumb.png",
        "footer": "Slack API",
        "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
        "ts": 123456789
    }
]


@pytest.fixture
def slack_client():
    return SlackWebhook(url=base64.b64decode(WEBHOOK_URL).decode())


@pytest.fixture
def slack_bot_instance():
    return SlackBot(token=base64.b64decode(BOT_USER).decode(), timeout=15)


@pytest.fixture
def slack_mock():
    slack_mock = Mock()
    slack_mock.url = 'https://liveramp.com/careers/'
    slack_mock.title = 'Liveramp'
    return slack_mock


def assert_res(res: WebhookResponse):
    assert 200 == res.status_code
    assert 'ok' == res.body


def test_send_message(slack_client):
    res = slack_client.send(message="test")
    assert_res(res)


def test_send_parsed_html(slack_client):
    parser = SlackHTMLParser()
    parsed_message = parser.parse(html_string_sample)
    res = slack_client.send(message=parsed_message)
    assert_res(res)


def test_send_block(slack_client):
    res = slack_client.send(message="blocks", blocks=blocks_sample)
    assert_res(res)


def test_send_attachments(slack_client):
    res = slack_client.send(message="attachments", attachments=attachments_sample)
    assert_res(res)


def test_send_message_with_slackbot(slack_bot_instance):
    result = slack_bot_instance.send_message(CHANNEL_ID, TEST_MESSAGE)
    assert result == (True, "")


def test_get_latest_n_messages(slack_bot_instance):
    result = slack_bot_instance.get_latest_n_messages(CHANNEL_ID, limit=MESSAGE_SIZE)
    assert result['ok']
    assert len(result['messages']) == MESSAGE_SIZE


def test_reply_latest_message(slack_bot_instance):
    result = slack_bot_instance.reply_latest_message(CHANNEL_ID, TEST_MESSAGE_REPLY)
    assert result is True


def test_send_message_to_channels(slack_bot_instance):
    result = slack_bot_instance.send_message_to_channels([CHANNEL_ID], TEST_MESSAGE)
    assert result
