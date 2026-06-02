from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product
from app.utils.file_upload import save_file

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/")

def create_product(
    name: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    filename = save_file(image)

    product = Product(
        name=name,
        description=description,
        image=filename
    )

    db.add(product)

    db.commit()

    db.refresh(product)

    return product


@router.get("/")

def get_products(
    db: Session = Depends(get_db)
):
    return db.query(Product).all()


@router.get("/{id}")

def get_product(
    id: int,
    db: Session = Depends(get_db)
):
    return db.query(Product)\
        .filter(Product.id == id)\
        .first()


@router.put("/{id}")

def update_product(
    id: int,
    name: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):

    product = db.query(Product)\
        .filter(Product.id == id)\
        .first()

    product.name = name
    product.description = description

    db.commit()

    return product


@router.delete("/{id}")

def delete_product(
    id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product)\
        .filter(Product.id == id)\
        .first()

    db.delete(product)

    db.commit()

    return {"message":"Deleted"}