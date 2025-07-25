from sqlmodel import Field, SQLModel, Column
from snowflake.sqlalchemy.custom_types import VARIANT
from typing import Optional
from pydantic import BaseModel

class SILVER_INCOME_STATEMENT(SQLModel, table=True):
    INDEX: str = Field(default=None, primary_key=True)
    YEAR_2024: float = Field(default=None)
    YEAR_2023: float = Field(default=None)
    YEAR_2022: float = Field(default=None)
    YEAR_2021: float = Field(default=None)
    YEAR_2020: float = Field(default=None)
    YEAR_2019: float = Field(default=None)
    YEAR_2018: float = Field(default=None)
    YEAR_2017: float = Field(default=None)
    YEAR_2016: float = Field(default=None)
    YEAR_2015: float = Field(default=None)

class SILVER_BALANCE_SHEET(SQLModel, table=True):
    INDEX: str = Field(default=None, primary_key=True)
    YEAR_2024: float = Field(default=None)
    YEAR_2023: float = Field(default=None)
    YEAR_2022: float = Field(default=None)
    YEAR_2021: float = Field(default=None)
    YEAR_2020: float = Field(default=None)
    YEAR_2019: float = Field(default=None)
    YEAR_2018: float = Field(default=None)
    YEAR_2017: float = Field(default=None)
    YEAR_2016: float = Field(default=None)
    YEAR_2015: float = Field(default=None)
    
    
class FinancialStatementResponse(BaseModel):
    INDEX: str
    YEAR_2024: Optional[float] = None
    YEAR_2023: Optional[float] = None
    YEAR_2022: Optional[float] = None
    YEAR_2021: Optional[float] = None
    YEAR_2020: Optional[float] = None
    YEAR_2019: Optional[float] = None
    YEAR_2018: Optional[float] = None
    YEAR_2017: Optional[float] = None
    YEAR_2016: Optional[float] = None
    YEAR_2015: Optional[float] = None
