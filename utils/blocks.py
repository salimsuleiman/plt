

def generateBlockStatement(amount, sender, date,  receiver, message)->str:
    """_summary_

    Args:
        amount (Decimal): _description_
        sender (String): _description_
        date (DateTime): _description_
        receiver (_type_): _description_
        message (_type_): _description_

    Returns:
        str: full statement of the transaction::block 
    """
    return f"on {date.day}/{date.month}/{date.year}, wallet with address:{sender} sends PLTC with amount: {amount} to wallet:{receiver}"