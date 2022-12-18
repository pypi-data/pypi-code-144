DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

DEFAULT_CLIENT_SERVICE_URLS = (
    'translate.googleapis.com',
)

DEFAULT_SERVICE_URLS = ('translate.google.ac', 'translate.google.ad', 'translate.google.ae',
                        'translate.google.al', 'translate.google.am', 'translate.google.as',
                        'translate.google.at', 'translate.google.az', 'translate.google.ba',
                        'translate.google.be', 'translate.google.bf', 'translate.google.bg',
                        'translate.google.bi', 'translate.google.bj', 'translate.google.bs',
                        'translate.google.bt', 'translate.google.by', 'translate.google.ca',
                        'translate.google.cat', 'translate.google.cc', 'translate.google.cd',
                        'translate.google.cf', 'translate.google.cg', 'translate.google.ch',
                        'translate.google.ci', 'translate.google.cl', 'translate.google.cm',
                        'translate.google.cn', 'translate.google.co.ao', 'translate.google.co.bw',
                        'translate.google.co.ck', 'translate.google.co.cr', 'translate.google.co.id',
                        'translate.google.co.il', 'translate.google.co.in', 'translate.google.co.jp',
                        'translate.google.co.ke', 'translate.google.co.kr', 'translate.google.co.ls',
                        'translate.google.co.ma', 'translate.google.co.mz', 'translate.google.co.nz',
                        'translate.google.co.th', 'translate.google.co.tz', 'translate.google.co.ug',
                        'translate.google.co.uk', 'translate.google.co.uz', 'translate.google.co.ve',
                        'translate.google.co.vi', 'translate.google.co.za', 'translate.google.co.zm',
                        'translate.google.co.zw', 'translate.google.com.af', 'translate.google.com.ag',
                        'translate.google.com.ai', 'translate.google.com.ar', 'translate.google.com.au',
                        'translate.google.com.bd', 'translate.google.com.bh', 'translate.google.com.bn',
                        'translate.google.com.bo', 'translate.google.com.br', 'translate.google.com.bz',
                        'translate.google.com.co', 'translate.google.com.cu', 'translate.google.com.cy',
                        'translate.google.com.do', 'translate.google.com.ec', 'translate.google.com.eg',
                        'translate.google.com.et', 'translate.google.com.fj', 'translate.google.com.gh',
                        'translate.google.com.gi', 'translate.google.com.gt', 'translate.google.com.hk',
                        'translate.google.com.jm', 'translate.google.com.kh', 'translate.google.com.kw',
                        'translate.google.com.lb', 'translate.google.com.ly', 'translate.google.com.mm',
                        'translate.google.com.mt', 'translate.google.com.mx', 'translate.google.com.my',
                        'translate.google.com.na', 'translate.google.com.ng', 'translate.google.com.ni',
                        'translate.google.com.np', 'translate.google.com.om', 'translate.google.com.pa',
                        'translate.google.com.pe', 'translate.google.com.pg', 'translate.google.com.ph',
                        'translate.google.com.pk', 'translate.google.com.pr', 'translate.google.com.py',
                        'translate.google.com.qa', 'translate.google.com.sa', 'translate.google.com.sb',
                        'translate.google.com.sg', 'translate.google.com.sl', 'translate.google.com.sv',
                        'translate.google.com.tj', 'translate.google.com.tr', 'translate.google.com.tw',
                        'translate.google.com.ua', 'translate.google.com.uy', 'translate.google.com.vc',
                        'translate.google.com.vn', 'translate.google.com', 'translate.google.cv',
                        'translate.google.cz', 'translate.google.de', 'translate.google.dj',
                        'translate.google.dk', 'translate.google.dm', 'translate.google.dz',
                        'translate.google.ee', 'translate.google.es', 'translate.google.eu',
                        'translate.google.fi', 'translate.google.fm', 'translate.google.fr',
                        'translate.google.ga', 'translate.google.ge', 'translate.google.gf',
                        'translate.google.gg', 'translate.google.gl', 'translate.google.gm',
                        'translate.google.gp', 'translate.google.gr', 'translate.google.gy',
                        'translate.google.hn', 'translate.google.hr', 'translate.google.ht',
                        'translate.google.hu', 'translate.google.ie', 'translate.google.im',
                        'translate.google.io', 'translate.google.iq', 'translate.google.is',
                        'translate.google.it', 'translate.google.je', 'translate.google.jo',
                        'translate.google.kg', 'translate.google.ki', 'translate.google.kz',
                        'translate.google.la', 'translate.google.li', 'translate.google.lk',
                        'translate.google.lt', 'translate.google.lu', 'translate.google.lv',
                        'translate.google.md', 'translate.google.me', 'translate.google.mg',
                        'translate.google.mk', 'translate.google.ml', 'translate.google.mn',
                        'translate.google.ms', 'translate.google.mu', 'translate.google.mv',
                        'translate.google.mw', 'translate.google.ne', 'translate.google.nf',
                        'translate.google.nl', 'translate.google.no', 'translate.google.nr',
                        'translate.google.nu', 'translate.google.pl', 'translate.google.pn',
                        'translate.google.ps', 'translate.google.pt', 'translate.google.ro',
                        'translate.google.rs', 'translate.google.ru', 'translate.google.rw',
                        'translate.google.sc', 'translate.google.se', 'translate.google.sh',
                        'translate.google.si', 'translate.google.sk', 'translate.google.sm',
                        'translate.google.sn', 'translate.google.so', 'translate.google.sr',
                        'translate.google.st', 'translate.google.td', 'translate.google.tg',
                        'translate.google.tk', 'translate.google.tl', 'translate.google.tm',
                        'translate.google.tn', 'translate.google.to', 'translate.google.tt',
                        'translate.google.us', 'translate.google.vg', 'translate.google.vu',
                        'translate.google.ws')

SPECIAL_CASES = {
    'ee': 'et',
}

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}

LANGUAGES_TRANSLATED = {
    'af': 'afrikaans',
    'sq': 'shqip',
    'am': 'አማርኛ',
    'ar': 'عربى',
    'hy': 'հայերեն',
    'az': 'azərbaycanlı',
    'eu': 'euskalduna',
    'be': 'беларускі',
    'bn': 'বাংলা',
    'bs': 'bosanski',
    'bg': 'български',
    'ca': 'català',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': '简体中文）',
    'zh-tw': '中國傳統的）',
    'co': 'corsu',
    'hr': 'hrvatski',
    'cs': 'čeština',
    'da': 'dansk',
    'nl': 'nederlands',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'eestlane',
    'tl': 'pilipino',
    'fi': 'suomalainen',
    'fr': 'français',
    'fy': 'frysk',
    'gl': 'galego',
    'ka': 'ქართველი',
    'de': 'deutsch',
    'el': 'ελληνικά',
    'gu': 'ગુજરાતી',
    'ht': 'kreyol ayisyen',
    'ha': 'hausa',
    'haw': 'ʻōlelo hawaiʻi',
    'iw': 'עִברִית',
    'he': 'עִברִית',
    'hi': 'हिन्दी',
    'hmn': 'hmoob',
    'hu': 'magyar',
    'is': 'íslensku',
    'ig': 'igbo',
    'id': 'bahasa indonesia',
    'ga': 'gaeilge',
    'it': 'italiano',
    'ja': '日本',
    'jw': 'basa jawa',
    'kn': 'ಕನ್ನಡ',
    'kk': 'қазақ',
    'km': 'ខ្មែរ',
    'ko': '한국어',
    'ku': 'kurdî (kurmancî)',
    'ky': 'кыргызча',
    'lo': 'ລາວ',
    'la': 'latin',
    'lv': 'latviski',
    'lt': 'lietuvis',
    'lb': 'lëtzebuergesch',
    'mk': 'македонски',
    'mg': 'malagasy',
    'ms': 'melayu',
    'ml': 'മലയാളം',
    'mt': 'malti',
    'mi': 'maori',
    'mr': 'मराठी',
    'mn': 'монгол',
    'my': 'မြန်မာ (ဗမာ)',
    'ne': 'नेपाली',
    'no': 'norsk',
    'or': 'ଓଡିଆ',
    'ps': 'پښتو',
    'fa': 'فارسی',
    'pl': 'polskie',
    'pt': 'português',
    'pa': 'ਪੰਜਾਬੀ',
    'ro': 'română',
    'ru': 'русский',
    'sm': 'samoa',
    'gd': 'gàidhlig na h-alba',
    'sr': 'српски',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'سنڌي',
    'si': 'සිංහල',
    'sk': 'slovenčina',
    'sl': 'slovenščina',
    'so': 'somaliyeed',
    'es': 'español',
    'su': 'basa sunda',
    'sw': 'kiswahili',
    'sv': 'svenska',
    'tg': 'тоҷикӣ',
    'ta': 'தமிழ்',
    'te': 'తెలుగు',
    'th': 'แบบไทย',
    'tr': 'türk',
    'uk': 'українська',
    'ur': 'اردو',
    'ug': 'uyghur',
    'uz': "o'zbek",
    'vi': 'tiếng việt',
    'cy': 'cymraeg',
    'xh': 'isixhosa',
    'yi': 'ייִדיש',
    'yo': 'yoruba',
    'zu': 'zulu',
}

LANGCODES = dict(map(reversed, LANGUAGES.items()))
DEFAULT_RAISE_EXCEPTION = False
DUMMY_DATA = [[["", None, None, 0]], None, "en", None,
              None, None, 1, None, [["en"], None, [1], ["en"]]]
