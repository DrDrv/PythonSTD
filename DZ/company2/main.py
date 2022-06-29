from get_gata import get_data_from_user
from application import app_eqal
from log_of_app import Evalution

peremennaya = get_data_from_user()
Evalution(peremennaya)
print(Evalution(app_eqal(str(peremennaya))))