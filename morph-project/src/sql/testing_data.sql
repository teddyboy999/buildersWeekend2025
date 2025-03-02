{{
    config(
        name = "testing_data_iowa_housing_prices",
        connection = "DUCKDB"
    )
}}

select
    SquareFeet as SquareFeet,
    SalePrice as SalePrice
from
    read_csv_auto("./data/IowaHousingPrices.csv")