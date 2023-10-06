import unittest
from num2words import num2words
from odoo import tools

class TestTurkishNumber(unittest.TestCase):

    def test_convert_nnn_tr(self):
        self.assertEqual(_convert_nnn_tr(0), 'SIFIR')
        self.assertEqual(_convert_nnn_tr(1), 'BİR')
        self.assertEqual(_convert_nnn_tr(10), 'ON')
        self.assertEqual(_convert_nnn_tr(100), 'YÜZ')
        self.assertEqual(_convert_nnn_tr(123), 'YÜZYİRMİÜÇ')

    def test_turkish_number(self):
        self.assertEqual(turkish_number(0), 'SIFIR')
        self.assertEqual(turkish_number(1), 'BİR')
        self.assertEqual(turkish_number(1000), 'BİN')
        self.assertEqual(turkish_number(123456789), 'YÜZYİRMİÜÇMİLYONDÖRTYEDİBİNALTIDOKUZYÜZSEKSENSEKİZ')

    def test_amount_to_text_tr(self):
        self.assertEqual(amount_to_text_tr(0, 'TRY'), 'SIFIR Türk Lirası')
        self.assertEqual(amount_to_text_tr(1, 'TRY'), 'BİR Türk Lirası')
        self.assertEqual(amount_to_text_tr(1.5, 'TRY'), 'BİR Türk Lirası ELLİ Kuruş')
        self.assertEqual(amount_to_text_tr(1234.56, 'TRY'), 'BİN İKİYÜZOTUZDÖRT Türk Lirası ELLİALTIBES Kuruş')

    def test_amount_to_text(self):
        self.assertEqual(amount_to_text(0, 'tr', 'TL'), 'SIFIR TL')
        self.assertEqual(amount_to_text(1, 'tr', 'TL'), 'BİR TL')
        self.assertEqual(amount_to_text(1.5, 'tr', 'TL'), 'BİR TL ELLİ Kuruş')
        self.assertEqual(amount_to_text(1234.56, 'tr', 'TL'), 'BİN İKİYÜZOTUZDÖRT TL ELLİALTIBES Kuruş')
        self.assertEqual(amount_to_text(1234.56, 'en', 'USD'), 'ONE THOUSAND TWO HUNDRED THIRTY-FOUR USD')

if __name__ == '__main__':
    unittest.main()