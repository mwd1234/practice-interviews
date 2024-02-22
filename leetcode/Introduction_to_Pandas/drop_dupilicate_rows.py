import pandas as pd

def drop_duplicate_emails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email')
    