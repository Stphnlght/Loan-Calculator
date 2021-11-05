"""credit calculator"""
import argparse
from annuity import Annuity
from differentiate import Diff


def main():
    # parser object
    parser = argparse.ArgumentParser(
        description="This is the Differentiate Loan Payment Calculator. \
                    It accepts optional CLI arguments for computation.")

    # add optional CLI arguments
    parser.add_argument("--type", default="annuity", choices=["annuity", "diff"],
                        help="this is the type of payment options. \
                              Supply either 'annuity' for Annuity or \
                                'diff' for Differentiate.")
    parser.add_argument("--payment", type=int,
                        help="(Annuity only) this is the monthly payment amount.")
    parser.add_argument("--principal", type=int,
                        help="this is the principal loan total.")
    parser.add_argument("--periods", type=int,
                        help="this is the total number of payments.")
    parser.add_argument("--interest", type=float,
                        help="this is the agreed interest rate.")

    # parse the arguments
    cli = parser.parse_args()

    # compile arguments into a collection
    compute_type = cli.type
    args = {
        "payment": cli.payment,
        "principal": cli.principal,
        "periods": cli.periods,
        "interest": cli.interest
    }

    # count and check if argument is valid (non-negative)
    nargs = len(args)  # number of CLI arguments
    for a in args:
        if args[a] and args[a] < 0:
            print("Incorrect parameters")  # negative value
            return
        nargs -= 1 if args[a] is None else 0  # count the number of arguments

    # compute if passed validity check
    if compute_type == 'annuity':
        if nargs < 3:  # excluding the compute type, valid nargs for annuity is 3
            print("Incorrect parameters")  # wrong number of args
            return
        Annuity.calculator(args['principal'],
                           args['payment'],
                           args['periods'],
                           args['interest'])

    elif compute_type == 'diff':
        Diff.calculator(args['principal'],
                        args['periods'],
                        args['interest'])


if __name__ == "__main__":
    main()
