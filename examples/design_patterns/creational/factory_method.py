
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""*What is this pattern about?
The Factory Method pattern can be used to create an interface for a
method, leaving the implementation to the class that gets
instantiated.
*What does this example do?
The code shows a way to localize words in two languages: English and
Greek. "getLocalizer" is the factory method that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "get" will be called
in the same way independently of the language.
*Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django:
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns For
example, in a contact form of a web page, the subject and the message
fields are created using the same form factory (CharField()), even
though they have different implementations according to their
purposes.
*References:
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
https://fkromer.github.io/python-pattern-references/design/#factory-method
https://sourcemaking.com/design_patterns/factory_method
*TL;DR80
Creates objects without having to specify the exact class.
"""

TYPE = dict(
    ENGLISH="English",
    GREEK="Greek"
)


class GreekGetter(object):
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)


def get_localizer(lang):
    """
    The Factory Method
    :param lang:
    :return:
    """
    languages = {
        TYPE['ENGLISH']: EnglishGetter,
        TYPE['GREEK']: GreekGetter
    }
    return languages[lang]()


if __name__ == "__main__":
    e, g = get_localizer(lang=TYPE['ENGLISH']), get_localizer(lang=TYPE['GREEK'])
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid), g.get(msgid))
