import Lab2

def test_find_min_max():
    input_arr = [5,67,32]
    test_arr = [5.0,67.0]
    result = Lab2.find_min_max(input_arr)
    assert(result == test_arr)


def test_calc_average():
    input_arr = [5,67,32]
    testAvg = 34.67
    result = Lab2.calc_average(input_arr)
    assert(result == testAvg)


def test_calc_median_temperature():
    input_arr = [5, 67, 32]
    median = 32.0
    result = Lab2.calc_median_temperature(input_arr)
    assert (result == median)