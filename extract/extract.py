from utils.config import engine_for_SQL_SERVER
from utils.logger import get_logger

logger = get_logger(__name__)

def get_data_from_sql_server():
    try:
        customers = pd.read_sql("SELECT * FROM Customers", engine_for_SQL_SERVER)
        orders = pd.read_sql("SELECT * FROM Orders", engine_for_SQL_SERVER)
        employees = pd.read_sql("SELECT * FROM Employees", engine_for_SQL_SERVER)
        order_details = pd.read_sql("SELECT * FROM [Order Details]", engine_for_SQL_SERVER)
        products = pd.read_sql("SELECT * FROM Products", engine_for_SQL_SERVER)
        logger.info("Data has been extracted successfully")
        return customers,orders,employees,order_details,products

    except Exception as e:
        logger.error(f"Error: {e}")
        return None
