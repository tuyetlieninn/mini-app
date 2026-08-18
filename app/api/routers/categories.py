from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)
from app.services.category_service import (
    list_categories,
    get_category,
    create_category,
    update_category,
    delete_category,
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("", response_model=list[CategoryResponse])
def list_all_categories(db: Session = Depends(get_db)):
    return list_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return get_category(db, category_id)


@router.post("", response_model=CategoryResponse, status_code=201)
def create_new_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, payload)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_existing_category(
    category_id: int,
    payload: CategoryUpdate,
    db: Session = Depends(get_db),
):
    return update_category(db, category_id, payload)


@router.delete("/{category_id}", status_code=204)
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    delete_category(db, category_id)
