sample_text = '''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers.
'''

import textwrap
print(textwrap.fill(text=sample_text,
                    width=70))
