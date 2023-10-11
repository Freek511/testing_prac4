from behave import given, when, then
from functions import transpose_matrix


@given("Матрица: {m}, которая введена пользователем.")
def set_matrix(context, m):
    context.m = eval(m)


@when("Матрица будет транспонирована")
def transpose(context):
    try:
        context.res = transpose_matrix(context.m)
    except AssertionError as e:
        context.error = str(e)


@then("Пользователь получит в результате матрицу: {expected}.")
def check_matrix(context, expected):
    assert context.res == eval(expected)


@then("Пользователь получит ошибку.")
def get_error(context):
    assert context.error is not None
