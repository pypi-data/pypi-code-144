from httpx import Response


class Base:
    def __init__(self, response: Response = None):
        self._response = response


class Translated(Base):
    """Translate result object

    :param src: source language (default: auto)
    :param dest: destination language (default: en)
    :param origin: original text
    :param text: translated text
    :param pronunciation: pronunciation
    """

    def __init__(self, src, text, origin, extra_data=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.src = src
        self.text = str(text)
        self.origin=origin
        self.extra_data = extra_data

    def __str__(self):  # pragma: nocover
        return self.__unicode__()

    def __unicode__(self):  # pragma: nocover
        return (
            u'Translated(src={src}, text={text}, '
            u'extra_data={extra_data})'.format(
                src=self.src, text=self.text,
                extra_data='"' + repr(self.extra_data)[:10] + '..."'
            )
        )


class Detected(Base):
    """Language detection result object

    :param lang: detected language
    :param confidence: the confidence of detection result (0.00 to 1.00)
    """

    def __init__(self, lang, confidence, **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.confidence = confidence

    def __str__(self):  # pragma: nocover
        return self.__unicode__()

    def __unicode__(self):  # pragma: nocover
        return u'Detected(lang={lang}, confidence={confidence})'.format(
            lang=self.lang, confidence=self.confidence)
