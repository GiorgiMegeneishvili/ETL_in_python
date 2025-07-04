from extraxt import extract
from Load import load
from transfrom import transform
from utils.logger import get_logger


logger = get_logger(__name__)


def etl():
    try:
        customers,orders,employees,order_details,products = extract.get_data_from_sql_server()
        transfrom1 = transform.transform_data(customers, orders, employees, order_details, products)
        load1 = load.load_data_into_Postgresql(transfrom1)
        logger.info("ETL has been executed successfully")
        return load1
    except Exception as e:
        logger.error(f"Error running ETL: {e}")
        return None


if __name__ == '__main__':
    etl()
