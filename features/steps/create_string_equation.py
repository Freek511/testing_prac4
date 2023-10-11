from behave import *
from functions import *



@given("коэффициенты {a0}, {a1}, {a2} и степень {power}, которые ввел пользователь")
def set_coeff(context, a0, a1, a2, power):
    context.a0 = a0
    context.a1 = a1
    context.a2 = a2
    context.power = power


@when(u'функция обработает данные коэффициенты')
def create_expression(context):
    context.res = ''
    coef = [context.a0, context.a1, context.a2]
    for i in range(int(context.power) + 1):
        context.res = create_string_equation(context.res, coef[i], i)


@then(u'пользователь увидит сгенерированное выражение {expected}')
def check_expression(context, expected):
    assert context.res == expected

