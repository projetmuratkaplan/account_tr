from num2words import num2words
from odoo import tools


# Single digits in Turkish
single = (u'SIFIR', u'BİR', u'İKİ', u'ÜÇ', u'DÖRT', u'BEŞ', u'ALTI', u'YEDİ', u'SEKİZ', u'DOKUZ')

# Tens in Turkish
tens = ('', u'ON', u'YİRMİ', u'OTUZ', u'KIRK', u'ELLİ', u'ALTMIŞ', u'YETMİŞ', u'SEKSEN', u'DOKSAN')

# Denominations in Turkish
denom = ('', u'BİN', 'MİLYON', 'MİLYAR', 'TRİLYON', 'KATRİLYON',
         'KENTİLYON', 'SEKSİLYON', 'SEPTİLYON', 'OKTİLYON', 'NONİLYON',
         'DESİLYON', 'UNDESİLYON', 'DODESİLYON', 'TREDESİLYON', 'KATIRDESİLYON',
         'KENDESİLYON', 'SEKSDESİLYON', 'SEPTENDESİLYON', 'OKTODESİLYON', 'NOVEMDESİLYON', 'VİGİNTİLYON')


# Convert a three-digit number to Turkish words
def _convert_nnn_tr(val):
    word = ''
    digits = list(int(d) for d in "{0:03d}".format(val))
    if val == 0:
        return single[0]
    if digits[2] > 0:
        word = single[digits[2]]
    if digits[1] > 0:
        if word == '':
            word = tens[digits[1]]
        else:
            word = tens[digits[1]] + '' + word
    if digits[0] > 0:
        if word == '':
            word = u'YÜZ'
        else:
            word = u'YÜZ' + '' + word
    if digits[0] > 1:
        word = single[digits[0]] + '' + word
    return word


# Convert a number to Turkish words
def turkish_number(val):
    if val < 1000:
        return _convert_nnn_tr(val)
    if val < 2000:
        return u'BİN' + _convert_nnn_tr(val % 1000)
    for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom))):
        if dval > val:
            mod = 1000 ** didx
            l = val // mod
            r = val - (l * mod)
            ret = _convert_nnn_tr(l) + '' + denom[didx]
            if r > 0:
                ret = ret + '' + turkish_number(r)
            return ret


# Convert an amount to its Turkish text representation
def amount_to_text_tr(number, currency):
    number = '%.2f' % number
    units_name = currency
    if currency == 'TRY':
        units_name = 'Türk Lirası'
    list = str(number).split('.')
    start_word = turkish_number(abs(int(list[0])))
    end_word = turkish_number(int(list[1]))
    cents_name = (currency == 'TRY') and u'Kuruş' or u'Sent'
    if end_word == 'SIFIR':
        final_result = start_word + ' ' + units_name
    else:
        final_result = start_word + ' ' + units_name + ' ' + end_word + ' ' + cents_name
    return final_result


# Translation functions based on language
_translate_funcs = {'tr': amount_to_text_tr}


# Convert an integer to its textual representation
def amount_to_text(nbr, lang='tr', currency='TL'):
    """ Converts an integer to its textual representation, using the language set in the context if any.

        Example::

            1654: mille six cent cinquante-quatre.
    """
    #    if nbr > 1000000:
    ##TODO: use logger
    #        print "WARNING: number too large '%d', can't translate it!" % (nbr,)
    #        return str(nbr)


    # Check if translation function exists for the language
    if lang not in _translate_funcs:
        return tools.ustr(' {amt_value} {amt_word}').format(
            amt_value=num2words(nbr, lang=lang),
            amt_word=currency,
        )

    # Default language to Turkish if not found
    lang = 'tr'
    return _translate_funcs[lang](abs(nbr), currency)