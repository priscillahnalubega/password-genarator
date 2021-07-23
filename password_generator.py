import random
import string

def get_password(upper_count=2, digits_count=2,lower_count=2,symbols_count=2,):
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    upper = ''.join((random.choice(string.ascii_uppercase)for i in range(upper_count)))
    lower = ''.join((random.choice(string.ascii_lowercase)for i in range(lower_count)))
    symbols = ''.join((random.choice(string.punctuation)for i in range(symbols_count)))
    

    # Convert resultant string to list and shuffle it to mix letters and digits

    sample_list = list( digits + upper + lower + symbols)
    random.shuffle(sample_list)

    # convert list to string

    final_password = ''.join(sample_list)
    print('Random password with',upper_count ,'uppercase_letters', lower_count,'lowercase_letters',symbols_count,'symbols', 'and', digits_count, 'digits', 'is:', final_password)

get_password()


