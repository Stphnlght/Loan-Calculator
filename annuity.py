"""calculator class for Annuity Loan Payments"""
import math


class Annuity:
    """
    This class is used to compute the values in Annuity Loan Payments.
    """

    @staticmethod
    def nominal(interest):
        """Compute the nominal (interest) rate"""
        return (interest / 100) / 12

    @staticmethod
    def option_n(principal=None, monthly=None, interest=None):
        """When the user enters 'n'; \
            computes the numbers of months required."""
        def get_periods():
            i = Annuity.nominal(interest)
            tmp = monthly / (monthly - i * principal)
            return math.ceil(math.log(tmp, i + 1))

        def get_year_month():
            periods = get_periods()
            y = periods // 12
            m = periods - (y * 12)
            return y, m

        if principal is None and monthly is None and interest is None:
            principal = int(input("Enter the loan principal:"))
            monthly = int(input("Enter the monthly payment:"))
            interest = float(input("Enter the loan interest:"))
        y, m = get_year_month()
        print(f"It will take {y} years and {m} months to repay this loan!")
        print(f"Overpayment = {monthly * get_periods() - principal}")

    @staticmethod
    def option_a(principal=None, periods=None, interest=None):
        """When the user enters 'a'; computes the monthly payment."""
        if principal is None and periods is None and interest is None:
            principal = int(input("Enter the loan principal:"))
            periods = int(input("Enter the number of periods:"))
            interest = float(input("Enter the loan interest:"))

        def get_monthly():
            i = Annuity.nominal(interest)
            return (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)

        a_monthly = int(math.ceil(principal * get_monthly()))
        print(f"Your monthly payment = {a_monthly}!")

    @staticmethod
    def option_p(monthly=None, periods=None, interest=None):
        """When the user enters 'p'; computes the total (principal) loan."""

        def get_principal():
            i = Annuity.nominal(interest)
            temp = (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
            return monthly / temp

        if monthly is None and periods is None and interest is None:
            monthly = float(input("Enter the annuity payment:"))
            periods = int(input("Enter the number of periods:"))
            interest = float(input("Enter the loan interest:"))
            principal = get_principal()
            print(f"Your loan principal = {principal}")
            return

        principal = get_principal()
        print(f"Your loan principal = {principal}")
        print(f"Overpayment = {monthly * periods - principal}")

    @staticmethod
    def calculator(principal=None, monthly=None, periods=None, interest=None):
        """Entry point function; asks user to select which option to compute."""
        option = None
        if principal is None and monthly is None and periods is None and interest is None:
            print("What do you want to calculate?")
            print("type \"n\" for number of monthly payments,")
            print("type \"a\" for annuity monthly payment amount,")
            print("type \"p\" for loan principal:")
            if option == "n":
                Annuity.option_n()
            if option == "a":
                Annuity.option_a()
            if option == "p":
                Annuity.option_p()
        else:
            if principal and monthly and interest:
                Annuity.option_n(principal, monthly, interest)
                return
            if principal and periods and interest:
                Annuity.option_a(principal, periods, interest)
                return
            if monthly and periods and interest:
                Annuity.option_p(monthly, periods, interest)
                return
