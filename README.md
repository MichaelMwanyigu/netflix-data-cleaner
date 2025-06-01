# Netflix Data Cleaner
A real world ETL project for cleaning and analyizing netflix watch logs

# Author
Built with Love By
Michael Mwanyigu
Software Integration Engineer @ Vodacom Tanzania



## Features
- Validated and cleans malformed json logs
- Extract play and pause events to compute watch duration
- Outputs clean csv file data for downstream Machine learning task
- Include a testsuite with pytest

## Tech Stack
- python 3
- pytest
- pandas
- pydantic

## Project Structure
netflix-data-cleaner/
├── data/
│   └── raw_log.json
├── src/
│   ├── cleaner.py
│   └── utils.py
├── output/
│   └── watch_duration.csv
├── tests/
│   └── test_cleaner.py
├── README.md
└── requirements.txt


## How to run
python src/cleaner.py

## Run test
pytest
