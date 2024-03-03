
import contextlib
import io
import pathlib
import unittest

from boilerplates.packaging_tests import run_module

from encrypted_config.crypto import encrypt
from encrypted_config.main import main

_HERE = pathlib.Path(__file__).parent


class Tests(unittest.TestCase):

    def test_basic(self):
        sio = io.StringIO()
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stdout(sio):
                main(['-h'])
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stderr(sio):
                main(['test'])

    @unittest.expectedFailure
    def test_encrypt(self):
        public_key_path = pathlib.Path(_HERE, 'test_id_rsa.pub.pem')
        secret = encrypt('1234', public_key_path)
        sio = io.StringIO()
        with contextlib.redirect_stdout(sio):
            main(['encrypt', '--key', str(public_key_path),
                  '--json', '{"login": "1234"}', '--login'])
        self.assertIn('"secure:login": "{}"'.format(secret), sio.getvalue())

    def test_decrypt(self):
        public_key_path = pathlib.Path(_HERE, 'test_id_rsa.pub.pem')
        private_key_path = pathlib.Path(_HERE, 'test_id_rsa')
        secret = encrypt('1234', public_key_path)
        sio = io.StringIO()
        with contextlib.redirect_stdout(sio):
            main(['decrypt', '--key', str(private_key_path),
                  '--json', '{{"secure:login": "{}"}}'.format(secret)])
        self.assertIn('"login": "1234"', sio.getvalue())

    def test_as_script(self):
        sio = io.StringIO()
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stdout(sio):
                run_module('encrypted_config', '-h')
        run_module('encrypted_config', '-h', run_name='not_main')
