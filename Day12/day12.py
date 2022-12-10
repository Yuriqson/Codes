import random, string
def get_random_user_id(length):

    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    random_id = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(1)])
    print(result_str+random_id)
get_random_user_id(3)
