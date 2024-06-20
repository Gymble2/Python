# TODO: define the 'EXPECTED_BAKE_TIME' constant.
def EXPECTED_BAKE_TIME(a=40):
    return a


def bake_time_remaining(a=30):
    real_time = EXPECTED_BAKE_TIME() - a
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return real_time


# TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes():
    camadas = int(input(f"Quantas camadas de lasanha você gostaria de adicionar?"))
    cama = 0

    if camadas != 0:
        cama = 2 * camadas

    PREPARATION_TIME = bake_time_remaining() + cama

    return PREPARATION_TIME


# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

print(preparation_time_in_minutes(), bake_time_remaining())
