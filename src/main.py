from fastapi import FastAPI, Depends, Query, HTTPException
from sqlmodel import Session, select
from src.database.connection import get_snowflake_connection, get_session
from typing import List, Optional
from src.models.financial import SILVER_BALANCE_SHEET, SILVER_INCOME_STATEMENT, FinancialStatementResponse

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World!"}

@app.get("/income-statement", response_model=List[FinancialStatementResponse])
async def get_income_statements(
    limit: Optional[int] = Query(100, description="Number of records to return"),
    session: Session = Depends(get_session)
):
    statement = select(SILVER_INCOME_STATEMENT).limit(limit)
    results = session.exec(statement).all()
    return results

@app.get("/income-statement/{index}", response_model=FinancialStatementResponse)
async def get_income_statement_by_index(
    index: str, 
    session: Session = Depends(get_session)
):
    result = session.get(SILVER_INCOME_STATEMENT, index)
    if not result:
        raise HTTPException(status_code=404, detail="Income statement record not found")
    return result

@app.get("/income-statement/year/{year}", response_model=List[dict])
async def get_income_statement_by_year(
    year: int,
    limit: Optional[int] = Query(100, description="Number of records to return"),
    session: Session = Depends(get_session)
):
    column_name = f"YEAR_{year}"
    if not hasattr(SILVER_INCOME_STATEMENT, column_name):
        raise HTTPException(status_code=400, detail=f"Year {year} data not available")
    statement = select(SILVER_INCOME_STATEMENT.INDEX, getattr(SILVER_INCOME_STATEMENT, column_name)).limit(limit)
    results = session.exec(statement).all()
    return [{"INDEX": row[0], column_name: row[1]} for row in results]
