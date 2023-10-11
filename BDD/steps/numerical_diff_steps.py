from behave import given, when, then
from function import numerical_diff
import math

@given('функция f(x) "{f}", точка x "{x:d}" и шаг h "{h:e}"')
def step_impl(context, f, x, h):
    context.f = f
    context.x = x
    context.h = h

@when('я вычисляю производную в этой точке')
def step_impl(context):
    context.result = numerical_diff(context.f, context.x, context.h)

@then('я получаю значение близкое к "{expected_result:f}"')
def step_impl(context, expected_result):
    assert abs(context.result - expected_result) < 1e-6
