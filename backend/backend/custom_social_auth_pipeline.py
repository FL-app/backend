# USER_FIELDS = ['username', 'email', 'password']
#
#
# def allowed_email(password):
#     return password == None
#
#
# def create_user(strategy, details, backend, user=None, *args, **kwargs):
#     if user:
#         return {'is_new': False}
#
#     fields = dict((name, kwargs.get(name, details.get(name)))
#                   for name in backend.setting('USER_FIELDS', USER_FIELDS))
#
#     if not fields:
#         return
#
#     if fields['password'] == None:
#         fields['password'] = "E5ZsitvpVOj"
#
#     return {
#         'is_new': True,
#         'user': strategy.create_user(**fields)
#     }
