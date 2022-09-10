import random
import string

def password(size=6, chars=string.ascii_lowercase+string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

