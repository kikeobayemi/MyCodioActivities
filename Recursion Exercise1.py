def recursive_sum(num1):
    """Recursively calculate sum from 0 to the parameter"""
    if num1 == 0:
        return 0
    else:
        return num1 + recursive_sum(num1 - 1)
        
recursive_sum(15)