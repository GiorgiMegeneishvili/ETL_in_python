import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

def transform_data(customers, orders, employees, order_details, products):
    try:
        # Step 1: Join Customers with Orders
        merged_df = pd.merge(customers, orders, on='CustomerID', how='inner')

        # Rename now to ensure the 'Country' column is preserved correctly
        merged_df.rename(columns={
            'CompanyName': 'CustomerName',
            'ContactName': 'CustomerContact',
            'Country': 'CustomerCountry',
            'ContactTitle': 'ContactTitle'  # just keep as-is
        }, inplace=True)

        # Step 2: Join with Employees
        merged_df = pd.merge(merged_df, employees, on='EmployeeID', how='inner')
        merged_df.rename(columns={
            'FirstName': 'EmployeeFirstName',
            'LastName': 'EmployeeLastName',
            'Title': 'EmployeeTitle'
        }, inplace=True)

        # Step 3: Rename order_details before merge
        order_details_renamed = order_details.rename(columns={
            'UnitPrice': 'OrderDetail_UnitPrice',
            'Discount': 'OrderDetail_Discount',
            'Quantity': 'OrderDetail_Quantity'
        })
        merged_df = pd.merge(merged_df, order_details_renamed, on='OrderID', how='inner')

        # Step 4: Join with Products
        merged_df = pd.merge(merged_df, products, on='ProductID', how='inner')

        # Step 5: Calculate TotalAmount
        merged_df['TotalAmount'] = (
            merged_df['OrderDetail_UnitPrice'] *
            merged_df['OrderDetail_Quantity'] *
            (1 - merged_df['OrderDetail_Discount'])
        )

        # Step 6: Final selection and renaming
        final_df = merged_df[[
            'CustomerID', 'CustomerName', 'CustomerContact', 'ContactTitle',
            'CustomerCountry', 'OrderID', 'OrderDate', 'ShippedDate',
            'EmployeeID', 'EmployeeFirstName', 'EmployeeLastName', 'EmployeeTitle',
            'ProductID', 'ProductName',
            'OrderDetail_UnitPrice', 'OrderDetail_Quantity', 'OrderDetail_Discount',
            'TotalAmount'
        ]].copy()

        # Rename columns for output clarity
        final_df.rename(columns={
            'OrderDetail_UnitPrice': 'UnitPrice',
            'OrderDetail_Quantity': 'Quantity',
            'OrderDetail_Discount': 'Discount'
        }, inplace=True)

        # Step 7: Sort
        final_df.sort_values(by=['OrderDate', 'CustomerCountry', 'ProductName'],
                         ascending=[False, True, True], inplace=True)
        logger.info("Data has been transformed successfully")
        return final_df
    except Exception as e:
        logger.error(f"Error: {e}")
        return None
