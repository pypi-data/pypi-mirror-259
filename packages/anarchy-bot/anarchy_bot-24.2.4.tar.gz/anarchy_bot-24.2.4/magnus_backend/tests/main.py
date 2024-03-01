import asyncio
import os
import sys
from pathlib import Path

from fastapi.testclient import TestClient


app_path = Path(__file__).parent.parent.resolve()
src_path = app_path / "src"
tests_path = app_path / "tests"
errors_path = app_path / "magnus_backend_data" / "errors"

sys.path.remove(str(tests_path))
sys.path += [
    str(src_path),
    str(app_path),
]


import src.db
import src.main
import src.common
import src.core.config
import tests.auth
import tests.common
import tests.pyright_test
import tests.outdated_packages
from tests.cabinet import (admin, orders, products, user, requisites, employees, warehouses,
                           categories as select_categories, basket, organizations)
from tests.cabinet.admin import categories, delivery_methods, payment_methods, users, notifications

do_tests = tests.common.DoTests(
    errors_path,
)


async def main():
    tests.common.console.log(
        src.core.config.config.system_info
    )
    await src.db.init()
    client = TestClient(
        src.main.app,
    )
    auth_test = tests.auth.AuthTest(client)
    user_cabinet_test = user.UserCabinetTest(client)
    admin_cabinet_test = admin.AdminCabinetTest(client)
    no_argument_methods = [
        *auth_test.methods_to_test,
        *user_cabinet_test.methods_to_test,
        admin_cabinet_test.register_admin,
    ]
    methods_with_arguments = [
        users.check_get_users,
        users.check_del_user,
        users.check_lock_user,
        categories.check_create_category,
        categories.check_update_category,
        categories.check_delete_category,
        delivery_methods.check_create_delivery_company,
        delivery_methods.check_delete_delivery_company,
        payment_methods.check_create_payment_method,
        payment_methods.check_update_payment_method,
        payment_methods.check_delete_payment_method,
        products.check_add_product,
        products.check_update_product,
        products.check_get_products,
        products.check_del_product,
        products.check_create_product_structure,
        products.check_upload_price,
        products.check_add_update_delete_list_minimum_quantity_goods,
        notifications.check_create_notification,
        requisites.check_create_props,
        requisites.check_update_props,
        requisites.check_delete_props,
        employees.check_create_employee,
        employees.check_employees,
        employees.check_delete_employee,
        warehouses.check_add_warehouse,
        warehouses.check_update_warehouse,
        warehouses.check_warehouses,
        warehouses.check_del_warehouse,
        employees.check_on_board_employee,
        user.check_offer_category,
        user.check_offer_categories,
        select_categories.check_select_category,
        select_categories.check_select_categories,
        select_categories.check_del_selected_category,
        basket.check_add_to_basket,
        basket.check_basket_items,
        basket.check_update_to_basket,
        basket.check_del_from_basket,
        basket.check_checkout,
        warehouses.check_add_delivery_company_point,
        warehouses.check_del_delivery_company_point,
        organizations.check_add_delivery_service,
        organizations.check_get_delivery_services,
        organizations.check_del_delivery_service
    ]
    do_tests.do_tests(no_argument_methods)
    do_tests.do_tests(
        methods_with_arguments,
        admin_cabinet_test,
    )
    await orders.init_order_data()  # TODO: move it upper
    methods_with_arguments_2 = [  # TODO: merge this with "methods_with_argumenrs" list
        orders.check_create_order,
        orders.check_change_order_status,
        orders.check_update_order,
        orders.check_order_add_item,
        orders.check_order_del_item
    ]
    do_tests.do_tests(  # TODO: delete it
        methods_with_arguments_2,
        admin_cabinet_test,
    )
    tests.pyright_test.main(do_tests)
    tests.outdated_packages.main(do_tests)
    os._exit(do_tests.exit_code)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        os._exit(0)
