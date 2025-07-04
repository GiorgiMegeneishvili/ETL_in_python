import pandas as pd
from utils.config import engine_POSTGRESQL
from utils.logger import get_logger

logger = get_logger(__name__)

def load_data_into_Postgresql(final_df):
    if final_df is None:
        return 'No data'
    try:
        final_df.to_sql("final_df", engine_POSTGRESQL, if_exists='replace', index=False)
        logger.info("Data has been loaded successfully")
        print(final_df)
    except Exception as e:
        logger.error(f'Error: {e}')
