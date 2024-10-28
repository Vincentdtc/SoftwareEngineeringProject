from Import_data import parse_data
from Process_data import process_data
from visualise import create_fig

raw_data = parse_data()
processed_data = process_data(raw_data)
create_fig(processed_data)