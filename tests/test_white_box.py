# -*- coding: utf-8 -*-

# domi comment

"""
White-box unit testing examples.
"""
import sys
import unittest
from io import StringIO
from itertools import product

from white_box import (
    BankingSystem,
    DocumentEditingSystem,
    ElevatorSystem,
    Product,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or
        equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater
        or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is
        greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


# 1


class TestCheckNumberStatus(unittest.TestCase):
    """
    Unit test class for function check_number_status.
    """

    def test_check_number_status_positive(self):
        """
        Checks if the function correctly identifies positive numbers.
        """
        self.assertEqual(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if the function correctly identifies negative numbers.
        """
        self.assertEqual(check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if the function correctly identifies zero.
        """
        self.assertEqual(check_number_status(0), "Zero")


# 2


class TestValidatePassword(unittest.TestCase):
    """
    Unit test class for function validate_password.
    """

    def test_validate_password_short(self):
        """
        Checks if the function correctly identifies short passwords.
        """
        self.assertFalse(validate_password("Ab1!"))

    def test_validate_password_no_uppercase(self):
        """
        Checks if the function correctly identifies
        passwords without uppercase letters.
        """
        self.assertFalse(validate_password("abcdefg1!"))

    def test_validate_password_no_lowercase(self):
        """
        Checks if the function correctly identifies
        passwords without lowercase letters.
        """
        self.assertFalse(validate_password("ABCDEFG1!"))

    def test_validate_password_no_digit(self):
        """
        Checks if the function correctly identifies passwords without digits.
        """
        self.assertFalse(validate_password("ABCDEFGh!"))

    def test_validate_password_no_special(self):
        """
        Checks if the function correctly identifies
        passwords without special characters.
        """
        self.assertFalse(validate_password("ABCDEFGh1"))

    def test_validate_password_valid(self):
        """
        Checks if the function correctly identifies valid passwords.
        """
        self.assertTrue(validate_password("Abcdefg1!"))


# 3


class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Unit test class for function calculate_total_discount.
    """

    def test_calculate_total_discount_less_than_100(self):
        """
        Checks if the function correctly calculates the
        discount for total amounts less than 100.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_between_100_and_500(self):
        """
        Checks if the function correctly calculates
        the discount for total amounts between 100 and 500.
        """
        self.assertEqual(calculate_total_discount(200), 20)

    def test_calculate_total_discount_greater_than_500(self):
        """
        Checks if the function correctly calculates
        the discount for total amounts greater than 500.
        """
        self.assertEqual(calculate_total_discount(600), 120)


# 4


class TestCalculateOrderTotal(unittest.TestCase):
    """
    Unit test class for function calculate_order_total.
    """

    def test_calculate_order_total_empty(self):
        """
        Checks if the function correctly calculates total for an empty order.
        """
        self.assertEqual(calculate_order_total([]), 0)

    def test_calculate_order_total_single_item_no_discount(self):
        """
        Checks if the function correctly calculates total for a single item with no discount.
        """
        self.assertEqual(
            calculate_order_total([{"quantity": 1, "price": 100}]), 100
        )

    def test_calculate_order_total_single_item_5_percent_discount(self):
        """
        Checks if the function correctly calculates total for a single item with 5% discount.
        """
        self.assertEqual(
            calculate_order_total([{"quantity": 6, "price": 100}]),
            569.9999999999999,
        )

    def test_calculate_order_total_single_item_10_percent_discount(self):
        """
        Checks if the function correctly calculates total for a single item with 10% discount.
        """
        self.assertEqual(
            calculate_order_total([{"quantity": 11, "price": 100}]), 990
        )

    def test_calculate_order_total_multiple_items(self):
        """
        Checks if the function correctly calculates total for multiple items with different discounts.
        """
        items = [
            {"quantity": 1, "price": 100},
            {"quantity": 6, "price": 100},
            {"quantity": 11, "price": 100},
        ]
        self.assertEqual(calculate_order_total(items), 1660)


# 5


class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    Unit test class for function calculate_items_shipping_cost.
    """

    def test_calculate_items_shipping_cost_standard_weight_less_than_equal_5(
        self,
    ):
        """
        Checks if the function correctly calculates standard shipping cost for total weight <= 5.
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_weight_between_5_and_10(
        self,
    ):
        """
        Checks if the function correctly calculates standard shipping cost for 5 < total weight <= 10.
        """
        items = [{"weight": 3}, {"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_weight_greater_than_10(
        self,
    ):
        """
        Checks if the function correctly calculates standard shipping cost for total weight > 10.
        """
        items = [{"weight": 6}, {"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_weight_less_than_equal_5(
        self,
    ):
        """
        Checks if the function correctly calculates express shipping cost for total weight <= 5.
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_weight_between_5_and_10(
        self,
    ):
        """
        Checks if the function correctly calculates express shipping cost for 5 < total weight <= 10.
        """
        items = [{"weight": 3}, {"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_weight_greater_than_10(self):
        """
        Checks if the function correctly calculates express shipping cost for total weight > 10.
        """
        items = [{"weight": 6}, {"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_invalid_shipping_method(self):
        """
        Checks if the function raises a ValueError for an invalid shipping method.
        """
        items = [{"weight": 2}, {"weight": 3}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "invalid")


# 6


class TestValidateLogin(unittest.TestCase):
    """
    Unit test class for function validate_login.
    """

    def test_validate_login_successful(self):
        """
        Checks if the function correctly validates a successful login.
        """
        self.assertEqual(
            validate_login("username", "password123"), "Login Successful"
        )

    def test_validate_login_failed_short_username(self):
        """
        Checks if the function correctly identifies short usernames.
        """
        self.assertEqual(validate_login("user", "password123"), "Login Failed")

    def test_validate_login_failed_long_username(self):
        """
        Checks if the function correctly identifies long usernames.
        """
        self.assertEqual(
            validate_login("thisisaverylongusername", "password123"),
            "Login Failed",
        )

    def test_validate_login_failed_short_password(self):
        """
        Checks if the function correctly identifies short passwords.
        """
        self.assertEqual(validate_login("username", "pass"), "Login Failed")

    def test_validate_login_failed_long_password(self):
        """
        Checks if the function correctly identifies long passwords.
        """
        self.assertEqual(
            validate_login("username", "thisisaverylongpassword"),
            "Login Failed",
        )


# 7


class TestVerifyAge(unittest.TestCase):
    """
    Unit test class for function verify_age.
    """

    def test_verify_age_eligible(self):
        """
        Checks if the function correctly identifies eligible ages.
        """
        self.assertEqual(verify_age(30), "Eligible")

    def test_verify_age_not_eligible_younger(self):
        """
        Checks if the function correctly identifies ages that are too young to be eligible.
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_not_eligible_older(self):
        """
        Checks if the function correctly identifies ages that are too old to be eligible.
        """
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_verify_age_eligible_edge_case_young(self):
        """
        Checks if the function correctly identifies the edge case of the youngest eligible age.
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_eligible_edge_case_old(self):
        """
        Checks if the function correctly identifies the edge case of the oldest eligible age.
        """
        self.assertEqual(verify_age(65), "Eligible")


# 8


class TestCategorizeProduct(unittest.TestCase):
    """
    Unit test class for function categorize_product.
    """

    def test_categorize_product_category_a(self):
        """
        Checks if the function correctly categorizes products in Category A.
        """
        self.assertEqual(categorize_product(25), "Category A")

    def test_categorize_product_category_b(self):
        """
        Checks if the function correctly categorizes products in Category B.
        """
        self.assertEqual(categorize_product(75), "Category B")

    def test_categorize_product_category_c(self):
        """
        Checks if the function correctly categorizes products in Category C.
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_categorize_product_category_d(self):
        """
        Checks if the function correctly categorizes products in Category D.
        """
        self.assertEqual(categorize_product(250), "Category D")


# 9


class TestValidateEmail(unittest.TestCase):
    """
    Unit test class for function validate_email.
    """

    def test_validate_email_valid(self):
        """
        Checks if the function correctly identifies valid emails.
        """
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_validate_email_short(self):
        """
        Checks if the function correctly identifies emails that are too short.
        """
        self.assertEqual(validate_email("a@b.c"), "Valid Email")

    def test_validate_email_long(self):
        """
        Checks if the function correctly identifies emails that are too long.
        """
        self.assertEqual(validate_email("a" * 46 + "@b.com"), "Invalid Email")

    def test_validate_email_no_at(self):
        """
        Checks if the function correctly identifies emails without '@'.
        """
        self.assertEqual(validate_email("test.example.com"), "Invalid Email")

    def test_validate_email_no_dot(self):
        """
        Checks if the function correctly identifies emails without '.'.
        """
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")


# 10


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    Unit test class for function celsius_to_fahrenheit.
    """

    def test_celsius_to_fahrenheit_zero(self):
        """
        Checks if the function correctly converts 0 Celsius to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_positive(self):
        """
        Checks if the function correctly converts positive Celsius to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(30), 86)

    def test_celsius_to_fahrenheit_negative(self):
        """
        Checks if the function correctly converts negative Celsius to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(-20), -4)

    def test_celsius_to_fahrenheit_boundary_low(self):
        """
        Checks if the function correctly converts the lowest valid Celsius temperature to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(-100), -148)

    def test_celsius_to_fahrenheit_boundary_high(self):
        """
        Checks if the function correctly converts the highest valid Celsius temperature to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_invalid_low(self):
        """
        Checks if the function correctly handles temperatures below the valid Celsius range.
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_invalid_high(self):
        """
        Checks if the function correctly handles temperatures above the valid Celsius range.
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


# 11


class TestValidateCreditCard(unittest.TestCase):
    """
    Unit test class for function validate_credit_card.
    """

    def test_validate_credit_card_valid_length(self):
        """
        Checks if the function correctly validates a card number of valid length.
        """
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_invalid_length_short(self):
        """
        Checks if the function correctly identifies card numbers that are too short.
        """
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_invalid_length_long(self):
        """
        Checks if the function correctly identifies card numbers that are too long.
        """
        self.assertEqual(
            validate_credit_card("12345678901234567"), "Invalid Card"
        )

    def test_validate_credit_card_non_digit(self):
        """
        Checks if the function correctly identifies card numbers that contain non-digit characters.
        """
        self.assertEqual(validate_credit_card("1234567890123A"), "Invalid Card")


# 12


class TestValidateDate(unittest.TestCase):
    """
    Unit test class for function validate_date.
    """

    def test_validate_date_valid(self):
        """
        Checks if the function correctly validates a valid date.
        """
        self.assertEqual(validate_date(2000, 12, 31), "Valid Date")

    def test_validate_date_invalid_year_low(self):
        """
        Checks if the function correctly identifies years below the valid range.
        """
        self.assertEqual(validate_date(1899, 12, 31), "Invalid Date")

    def test_validate_date_invalid_year_high(self):
        """
        Checks if the function correctly identifies years above the valid range.
        """
        self.assertEqual(validate_date(2101, 12, 31), "Invalid Date")

    def test_validate_date_invalid_month_low(self):
        """
        Checks if the function correctly identifies months below the valid range.
        """
        self.assertEqual(validate_date(2000, 0, 31), "Invalid Date")

    def test_validate_date_invalid_month_high(self):
        """
        Checks if the function correctly identifies months above the valid range.
        """
        self.assertEqual(validate_date(2000, 13, 31), "Invalid Date")

    def test_validate_date_invalid_day_low(self):
        """
        Checks if the function correctly identifies days below the valid range.
        """
        self.assertEqual(validate_date(2000, 12, 0), "Invalid Date")

    def test_validate_date_invalid_day_high(self):
        """
        Checks if the function correctly identifies days above the valid range.
        """
        self.assertEqual(validate_date(2000, 12, 32), "Invalid Date")


# 13


class TestCheckFlightEligibility(unittest.TestCase):
    """
    Unit test class for function check_flight_eligibility.
    """

    def test_check_flight_eligibility_in_age_range(self):
        """
        Checks if the function correctly identifies passengers within the age range.
        """
        self.assertEqual(
            check_flight_eligibility(30, False), "Eligible to Book"
        )

    def test_check_flight_eligibility_frequent_flyer(self):
        """
        Checks if the function correctly identifies passengers who are frequent flyers.
        """
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_check_flight_eligibility_not_eligible(self):
        """
        Checks if the function correctly identifies passengers who are not eligible.
        """
        self.assertEqual(
            check_flight_eligibility(17, False), "Not Eligible to Book"
        )
        self.assertEqual(
            check_flight_eligibility(66, False), "Not Eligible to Book"
        )


# 14


class TestValidateUrl(unittest.TestCase):
    """
    Unit test class for function validate_url.
    """

    def test_validate_url_valid_http(self):
        """
        Checks if the function correctly validates a valid http URL.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https(self):
        """
        Checks if the function correctly validates a valid https URL.
        """
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_invalid_protocol(self):
        """
        Checks if the function correctly identifies URLs with invalid protocol.
        """
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_validate_url_invalid_length(self):
        """
        Checks if the function correctly identifies URLs exceeding 255 characters.
        """
        long_url = "http://" + "a" * 250 + ".com"
        self.assertEqual(validate_url(long_url), "Invalid URL")


# 15


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    Unit test class for function calculate_quantity_discount.
    """

    def test_calculate_quantity_discount_no_discount(self):
        """
        Checks if the function correctly identifies quantities that should not receive a discount.
        """
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_5_percent(self):
        """
        Checks if the function correctly identifies quantities that should receive a 5% discount.
        """
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_10_percent(self):
        """
        Checks if the function correctly identifies quantities that should receive a 10% discount.
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(calculate_quantity_discount(20), "10% Discount")


# 16


class TestCheckFileSize(unittest.TestCase):
    """
    Unit test class for function check_file_size.
    """

    def test_check_file_size_valid(self):
        """
        Checks if the function correctly identifies valid file sizes.
        """
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_check_file_size_invalid_large(self):
        """
        Checks if the function correctly identifies file sizes that are too large.
        """
        self.assertEqual(check_file_size(2000000), "Invalid File Size")

    def test_check_file_size_invalid_negative(self):
        """
        Checks if the function correctly identifies negative file sizes.
        """
        self.assertEqual(check_file_size(-500), "Invalid File Size")

    def test_check_file_size_zero(self):
        """
        Checks if the function correctly identifies a file size of zero as valid.
        """
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_max(self):
        """
        Checks if the function correctly identifies the maximum file size as valid.
        """
        self.assertEqual(check_file_size(1048576), "Valid File Size")


# 17
# Python


class TestCheckLoanEligibility(unittest.TestCase):
    """
    Unit test class for function check_loan_eligibility.
    """

    def test_check_loan_eligibility_not_eligible(self):
        """
        Checks if the function correctly identifies when a person is not eligible for a loan.
        """
        self.assertEqual(check_loan_eligibility(25000, 650), "Not Eligible")

    def test_check_loan_eligibility_standard_loan_low_income_high_credit(self):
        """
        Checks if the function correctly identifies when a person is eligible for a standard loan due to low income but high credit score.
        """
        self.assertEqual(check_loan_eligibility(35000, 710), "Standard Loan")

    def test_check_loan_eligibility_secured_loan(self):
        """
        Checks if the function correctly identifies when a person is eligible for a secured loan due to low income and low credit score.
        """
        self.assertEqual(check_loan_eligibility(35000, 650), "Secured Loan")

    def test_check_loan_eligibility_premium_loan(self):
        """
        Checks if the function correctly identifies when a person is eligible for a premium loan due to high income and high credit score.
        """
        self.assertEqual(check_loan_eligibility(65000, 760), "Premium Loan")

    def test_check_loan_eligibility_standard_loan_high_income_low_credit(self):
        """
        Checks if the function correctly identifies when a person is eligible for a standard loan due to high income but low credit score.
        """
        self.assertEqual(check_loan_eligibility(65000, 740), "Standard Loan")


# 18


class TestCalculateShippingCost(unittest.TestCase):
    """
    Unit test class for function calculate_shipping_cost.
    """

    def test_calculate_shipping_cost_small_package(self):
        """
        Checks if the function correctly calculates the shipping cost for small packages.
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_medium_package(self):
        """
        Checks if the function correctly calculates the shipping cost for medium packages.
        """
        self.assertEqual(calculate_shipping_cost(2, 15, 15, 15), 10)

    def test_calculate_shipping_cost_large_package(self):
        """
        Checks if the function correctly calculates the shipping cost for large packages.
        """
        self.assertEqual(calculate_shipping_cost(6, 31, 31, 31), 20)

    def test_calculate_shipping_cost_weight_boundary(self):
        """
        Checks if the function correctly calculates the shipping cost for packages on the weight boundary.
        """
        self.assertEqual(calculate_shipping_cost(1, 11, 11, 11), 20)

    def test_calculate_shipping_cost_dimension_boundary(self):
        """
        Checks if the function correctly calculates the shipping cost for packages on the dimension boundary.
        """
        self.assertEqual(calculate_shipping_cost(2, 10, 10, 10), 20)


# 19


class TestGradeQuiz(unittest.TestCase):
    """
    Unit test class for function grade_quiz.
    """

    def test_grade_quiz_pass(self):
        """
        Checks if the function correctly identifies a passing grade.
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_grade_quiz_conditional_pass(self):
        """
        Checks if the function correctly identifies a conditional pass grade.
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_grade_quiz_fail(self):
        """
        Checks if the function correctly identifies a failing grade.
        """
        self.assertEqual(grade_quiz(4, 4), "Fail")
        self.assertEqual(grade_quiz(6, 4), "Fail")


# 20


class TestAuthenticateUser(unittest.TestCase):
    """
    Unit test class for function authenticate_user.
    """

    def test_authenticate_user_admin(self):
        """
        Checks if the function correctly authenticates the admin user.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_valid_user(self):
        """
        Checks if the function correctly authenticates a valid user.
        """
        self.assertEqual(authenticate_user("user123", "password123"), "User")

    def test_authenticate_user_invalid_username(self):
        """
        Checks if the function correctly identifies invalid usernames.
        """
        self.assertEqual(authenticate_user("usr", "password123"), "Invalid")

    def test_authenticate_user_invalid_password(self):
        """
        Checks if the function correctly identifies invalid passwords.
        """
        self.assertEqual(authenticate_user("user123", "pwd"), "Invalid")

    def test_authenticate_user_invalid_credentials(self):
        """
        Checks if the function correctly identifies invalid credentials.
        """
        self.assertEqual(authenticate_user("usr", "pwd"), "Invalid")


# 21


class TestGetWeatherAdvisory(unittest.TestCase):
    """
    Unit test class for function get_weather_advisory.
    """

    def test_get_weather_advisory_high_temp_and_humidity(self):
        """
        Checks if the function correctly identifies high temperature and humidity.
        """
        self.assertEqual(
            get_weather_advisory(35, 75),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_low_temp(self):
        """
        Checks if the function correctly identifies low temperature.
        """
        self.assertEqual(
            get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!"
        )

    def test_get_weather_advisory_no_specific_advisory(self):
        """
        Checks if the function correctly identifies conditions that do not require a specific advisory.
        """
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")


# 22


class TestVendingMachine(unittest.TestCase):
    """
    Unit test class for VendingMachine.
    """

    def setUp(self):
        """
        Set up a new VendingMachine instance before each test.
        """
        self.machine = VendingMachine()

    def test_initial_state(self):
        """
        Test if the initial state of the vending machine is "Ready".
        """
        self.assertEqual(self.machine.state, "Ready")

    def test_insert_coin_in_ready_state(self):
        """
        Test if the state changes to "Dispensing" and returns the correct message when a coin is inserted in "Ready" state.
        """
        response = self.machine.insert_coin()
        self.assertEqual(response, "Coin Inserted. Select your drink.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_insert_coin_in_dispensing_state(self):
        """
        Test if the state remains "Dispensing" and returns the correct message when a coin is inserted in "Dispensing" state.
        """
        self.machine.insert_coin()  # Change state to "Dispensing"
        response = self.machine.insert_coin()
        self.assertEqual(response, "Invalid operation in current state.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_select_drink_in_dispensing_state(self):
        """
        Test if the state changes to "Ready" and returns the correct message when a drink is selected in "Dispensing" state.
        """
        self.machine.insert_coin()  # Change state to "Dispensing"
        response = self.machine.select_drink()
        self.assertEqual(response, "Drink Dispensed. Thank you!")
        self.assertEqual(self.machine.state, "Ready")

    def test_select_drink_in_ready_state(self):
        """
        Test if the state remains "Ready" and returns the correct message when a drink is selected in "Ready" state.
        """
        response = self.machine.select_drink()
        self.assertEqual(response, "Invalid operation in current state.")
        self.assertEqual(self.machine.state, "Ready")


# 23


class TestTrafficLight(unittest.TestCase):
    """
    Unit test class for TrafficLight.
    """

    def setUp(self):
        """
        Set up a TrafficLight instance for testing.
        """
        self.traffic_light = TrafficLight()

    def test_initial_state(self):
        """
        Test the initial state of the traffic light.
        """
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_state_change(self):
        """
        Test the state change of the traffic light.
        """
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_multiple_state_changes(self):
        """
        Test multiple state changes of the traffic light.
        """
        for _ in range(10):
            self.traffic_light.change_state()
        # After 10 changes, the state should be "Green" again.

        self.assertEqual(self.traffic_light.get_current_state(), "Green")


# 24


class TestUserAuthentication(unittest.TestCase):
    """
    Unit test class for UserAuthentication.
    """

    def setUp(self):
        """
        Set up a UserAuthentication instance for testing.
        """
        self.user_auth = UserAuthentication()

    def test_initial_state(self):
        """
        Test that the initial state is "Logged Out".
        """
        self.assertEqual(self.user_auth.state, "Logged Out")

    def test_login_from_logged_out_state(self):
        """
        Test that a user can login from a "Logged Out" state.
        """
        self.assertEqual(self.user_auth.login(), "Login successful")
        self.assertEqual(self.user_auth.state, "Logged In")

    def test_login_from_logged_in_state(self):
        """
        Test that a user cannot login from a "Logged In" state.
        """
        self.user_auth.state = "Logged In"
        self.assertEqual(
            self.user_auth.login(), "Invalid operation in current state"
        )

    def test_logout_from_logged_in_state(self):
        """
        Test that a user can logout from a "Logged In" state.
        """
        self.user_auth.state = "Logged In"
        self.assertEqual(self.user_auth.logout(), "Logout successful")
        self.assertEqual(self.user_auth.state, "Logged Out")

    def test_logout_from_logged_out_state(self):
        """
        Test that a user cannot logout from a "Logged Out" state.
        """
        self.assertEqual(
            self.user_auth.logout(), "Invalid operation in current state"
        )


# 25


class TestDocumentEditingSystem(unittest.TestCase):
    """
    Unit test class for DocumentEditingSystem.
    """

    def setUp(self):
        """
        Set up a new instance of DocumentEditingSystem for each test.
        """
        self.doc_system = DocumentEditingSystem()

    def test_initial_state(self):
        """
        Checks if the initial state is "Editing".
        """
        self.assertEqual(self.doc_system.state, "Editing")

    def test_save_document_in_editing_state(self):
        """
        Checks if the document can be saved in "Editing" state.
        """
        self.assertEqual(
            self.doc_system.save_document(), "Document saved successfully"
        )
        self.assertEqual(self.doc_system.state, "Saved")

    def test_save_document_in_saved_state(self):
        """
        Checks if the document can't be saved in "Saved" state.
        """
        self.doc_system.state = "Saved"
        self.assertEqual(
            self.doc_system.save_document(),
            "Invalid operation in current state",
        )

    def test_edit_document_in_saved_state(self):
        """
        Checks if the document can be edited in "Saved" state.
        """
        self.doc_system.state = "Saved"
        self.assertEqual(self.doc_system.edit_document(), "Editing resumed")
        self.assertEqual(self.doc_system.state, "Editing")

    def test_edit_document_in_editing_state(self):
        """
        Checks if the document can't be edited in "Editing" state.
        """
        self.assertEqual(
            self.doc_system.edit_document(),
            "Invalid operation in current state",
        )


# 26


class TestElevatorSystem(unittest.TestCase):
    """
    Unit test class for ElevatorSystem.
    """

    def setUp(self):
        """
        Set up a new ElevatorSystem instance before each test.
        """
        self.elevator = ElevatorSystem()

    def test_initial_state(self):
        """
        Test that the initial state of the elevator is "Idle".
        """
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_from_idle(self):
        """
        Test that the elevator can move up from the "Idle" state.
        """
        self.assertEqual(self.elevator.move_up(), "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_up_from_non_idle(self):
        """
        Test that the elevator cannot move up from a non-"Idle" state.
        """
        self.elevator.state = "Moving Down"
        self.assertEqual(
            self.elevator.move_up(), "Invalid operation in current state"
        )

    def test_move_down_from_idle(self):
        """
        Test that the elevator can move down from the "Idle" state.
        """
        self.assertEqual(self.elevator.move_down(), "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_down_from_non_idle(self):
        """
        Test that the elevator cannot move down from a non-"Idle" state.
        """
        self.elevator.state = "Moving Up"
        self.assertEqual(
            self.elevator.move_down(), "Invalid operation in current state"
        )

    def test_stop_from_moving(self):
        """
        Test that the elevator can stop from the "Moving Up" or "Moving Down" state.
        """
        self.elevator.state = "Moving Up"
        self.assertEqual(self.elevator.stop(), "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

        self.elevator.state = "Moving Down"
        self.assertEqual(self.elevator.stop(), "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_from_idle(self):
        """
        Test that the elevator cannot stop from the "Idle" state.
        """
        self.assertEqual(
            self.elevator.stop(), "Invalid operation in current state"
        )


# 27


class TestElevatorSystem(unittest.TestCase):
    """
    Unit test class for ElevatorSystem.
    """

    def setUp(self):
        """
        Set up a new ElevatorSystem instance before each test.
        """
        self.elevator = ElevatorSystem()

    def test_initial_state(self):
        """
        Test that the initial state of the elevator is "Idle".
        """
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_from_idle(self):
        """
        Test that the elevator can move up from the "Idle" state.
        """
        self.assertEqual(self.elevator.move_up(), "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_up_from_non_idle(self):
        """
        Test that the elevator cannot move up from a non-"Idle" state.
        """
        self.elevator.state = "Moving Down"
        self.assertEqual(
            self.elevator.move_up(), "Invalid operation in current state"
        )

    def test_move_down_from_idle(self):
        """
        Test that the elevator can move down from the "Idle" state.
        """
        self.assertEqual(self.elevator.move_down(), "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_down_from_non_idle(self):
        """
        Test that the elevator cannot move down from a non-"Idle" state.
        """
        self.elevator.state = "Moving Up"
        self.assertEqual(
            self.elevator.move_down(), "Invalid operation in current state"
        )

    def test_stop_from_moving(self):
        """
        Test that the elevator can stop from the "Moving Up" or "Moving Down" state.
        """
        self.elevator.state = "Moving Up"
        self.assertEqual(self.elevator.stop(), "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

        self.elevator.state = "Moving Down"
        self.assertEqual(self.elevator.stop(), "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_from_idle(self):
        """
        Test that the elevator cannot stop from the "Idle" state.
        """
        self.assertEqual(
            self.elevator.stop(), "Invalid operation in current state"
        )


class TestBankingSystem(unittest.TestCase):
    """
    Unit test class for BankingSystem.
    """

    def setUp(self):
        """
        Set up a BankingSystem instance for testing.
        """
        self.banking_system = BankingSystem()

    def test_authenticate_valid(self):
        """
        Test if the authenticate function works with valid credentials.
        """
        self.assertTrue(self.banking_system.authenticate("user123", "pass123"))

    def test_authenticate_invalid(self):
        """
        Test if the authenticate function works with invalid credentials.
        """
        self.assertFalse(
            self.banking_system.authenticate("user123", "wrongpass")
        )

    def test_authenticate_already_logged_in(self):
        """
        Test if the authenticate function works when the user is already logged in.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.authenticate("user123", "pass123"))

    def test_transfer_money_not_authenticated(self):
        """
        Test if the transfer_money function works when the sender is not authenticated.
        """
        self.assertFalse(
            self.banking_system.transfer_money(
                "user123", "receiver", 100, "regular"
            )
        )

    def test_transfer_money_invalid_transaction_type(self):
        """
        Test if the transfer_money function works with an invalid transaction type.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(
            self.banking_system.transfer_money(
                "user123", "receiver", 100, "invalid"
            )
        )

    def test_transfer_money_insufficient_funds(self):
        """
        Test if the transfer_money function works when the sender has insufficient funds.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(
            self.banking_system.transfer_money(
                "user123", "receiver", 2000, "regular"
            )
        )

    def test_transfer_money_successful(self):
        """
        Test if the transfer_money function works when the transaction should be successful.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(
            self.banking_system.transfer_money(
                "user123", "receiver", 500, "regular"
            )
        )


# 28


class TestProduct(unittest.TestCase):
    """
    Unit test class for class Product.
    """

    def setUp(self):
        """
        Set up a product instance for use in tests.
        """
        self.product = Product("Test Product", 100)

    def test_product_initialization(self):
        """
        Test the initialization of the Product class.
        """
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100)

    def test_view_product(self):
        product = Product("Test Product", 100)
        stdout_original = sys.stdout
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        product.view_product()
        sys.stdout = stdout_original
        self.assertEqual(
            salida_capturada.getvalue().strip(),
            "The product Test Product has a price of 100",
        )


if __name__ == "__main__":
    unittest.main()
