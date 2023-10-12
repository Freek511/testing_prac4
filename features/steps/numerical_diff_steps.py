from behave import given, when, then
from functions import *


@given('функция f(x) "{f}", точка x "{x}" и шаг h "{h}"')
def step_impl(context, f, x, h):
    context.f = eval(f)
    context.x = float(x)
    context.h = float(h)


@when('я вычисляю производную в этой точке')
def step_impl(context):
    context.result = numerical_diff(context.f, context.x, context.h)


@then('я получаю значение близкое к "{expected_result}"')
def step_impl(context, expected_result):
    assert abs(context.result - float(expected_result)) < 1e-6
