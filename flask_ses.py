from __future__ import absolute_import
__version__ = '0.1.0'

import boto

class Ses(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.aws_access_key_id = self.app.config.get("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = self.app.config.get("AWS_SECRET_ACCESS_KEY")

    def send_email(self, from_address, subject, body, recipient_list, **kwargs):
        conn = boto.connect_ses(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key)
        return conn.send_email(from_address, subject, body, recipient_list, **kwargs)
