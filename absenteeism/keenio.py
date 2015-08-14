import os
from keen.client import KeenClient

def get_keen_client():
    return KeenClient(
        project_id = os.getenv('KEEN_PROJECT_ID'),
        write_key = os.getenv('KEEN_WRITE_KEY'),
        read_key = os.getenv('KEEN_READ_KEY'),
        master_key = os.getenv('KEEN_MASTER_KEY')
    )
