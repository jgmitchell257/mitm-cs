def compound_interest(principal: int, interest: float, periods: int) -> float:
    """
    Calculates the total return on a standard deposit and interest rate every period.

    Args
        principal: amount to be deposited every period
        interest: expressed in decimal 3% = .03
        periods: the number of periods to calculate for
    """
    value = 0
    total_value = 0
    periods = periods

    while periods > 0:
        value = principal * ((1 + interest)**periods)
        total_value = total_value + value
        periods -= 1
    
    return total_value


def simple_compound_interest(principal: int, interest: float, periods: int) -> float:
    """
    Calculates the total return on a single deposit with compounding interest

    Args
        principal: amount to be deposited
        interest: expressed in decimal 3% = .03
        periods: the number of periods to calculate for
    """
    total_value = principal * ((1 + interest)**periods)
    return total_value


def quarterly_compound_interest(p: int, i: float, n: int) -> float:
    """
    Calculates the total return on a standard deposit and interest rate every period.

    Args
        principal: amount to be deposited every period
        interest: expressed in decimal 3% = .03
        periods: the number of periods to calculate for
    """

    value = 0
    total_value = 0
    periods = n

    while periods > 0:
        value = p * (1 + i)**periods
        total_value = total_value + value
        periods -= 4
        print(value, total_value)
    
    return total_value