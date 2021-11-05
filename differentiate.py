"""calculator class for Differentiate Loan Payments"""
import math


class Diff:
    """
    This class is used to compute values in Differentiate Loan Payments.
    """
    @staticmethod
    def nominal(interest):
        """Compute the nominal (interest) rate"""
        return (interest / 100) / 12

    @staticmethod
    def calculator(principal, periods, interest):
        P = principal
        i = Diff.nominal(interest)
        n = periods
        total = 0
        for m in range(1, n+1):
            d = int(math.ceil(P / n + i * (P - (P * (m - 1) / n))))
            # d = math.ceil(principal / n) + math.ceil(i * (principal - (principal * (m - 1)) / 10))
            print(f"Month {m}: payment is {int(d)}")  # \t\t principal={principal}, i={i}, n={n}")
            total += d

        print(f"Overpayment = {total - principal}")
