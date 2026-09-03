from fastapi import FastAPI, HTTPException, Query, Path
from app.service.products import (
    add_product, 
    get_all_products, 
    remove_product, 
    change_product,
)
from app.schema.product import Product, ProductUpdate
from uuid import UUID, uuid4
from datetime import datetime


# Create the FastAPI application instance used by the development server.
app = FastAPI()


@app.get("/")
def root():
    """Return a simple health message for the root endpoint."""
    return {"message": "Welcome to FastAPI"}


@app.get("/products")
def list_products(
    name: str | None = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search products by name (case insensitive)",
        example="Hp"
    ),

    sort_by_price: bool = Query(
        default=False,
        description="Sort products by price",
    ),

    order: str = Query(
        default="asc",
        description="Sort order: 'asc' for ascending, 'desc' for descending",
    ),

    limit: int = Query(
        default=5,
        ge=1,
        le=100,
        description="Limit the number of products returned (1-100)",
    ),

    offset: int = Query(
        default=0,
        ge=0,
        description="Offset for pagination (0 or greater)",
    )
):
    """Return products with optional name filtering, sorting, and pagination."""
    products = get_all_products()
    total = len(products)

    # Apply filtering before sorting and pagination so total reflects the search.
    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]
        total = len(products)

        if not products:
            raise HTTPException(
                status_code=404,
                detail=f"No products found matching the name={name}",
            )

    # Sorting is optional; ascending order is the default for invalid order values.
    if sort_by_price:
        if order == "desc":
            products = sorted(products, key=lambda p: p.get("price", 0), reverse=True)
        else:
            products = sorted(products, key=lambda p: p.get("price", 0))

    # Slice after filtering and sorting to provide predictable pagination.
    if limit:
        products = products[offset : offset + limit]

    return {"total": total, "products": products}

@app.get("/products/{product_id}")
def get_product_by_id(

    product_id: str = Path(
        ...,
        min_length=36,
        max_length=36,
        description='The ID of the product to retrieve',
        example='24a9d4f3-d78c-4a1e-b516-5c50c46fc1be',
    )
):
    """Return one product that matches the requested identifier."""
    products = get_all_products()
    product = next((p for p in products if p.get("id") == product_id), None)

    if not product:
        raise HTTPException(status_code=404, detail=f"Product with id={product_id} not found")
    return product

@app.post("/products", status_code=201)
def create_product(product: Product):
    """Validate and persist a new product with a generated UUID."""
    product_dict = product.model_dump(mode="json")
    product_dict["id"] = str(uuid4())
    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return product.model_dump(mode="json")

@app.delete("/products/{product_id}")
def delete_product(
    product_id: UUID = Path(
        ...,
        description='Product UUID',
    )
):
    """Delete and return the product identified by the supplied UUID."""
    try:
        res = remove_product(str(product_id))
        return res
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/products/{product_id}")
def update_product(product_id: UUID = Path(..., description='Product UUID'),
    payload: ProductUpdate = ...,
):
    """Apply the supplied fields to an existing product."""
    try:
        update_product = change_product(str(product_id), payload.model_dump(mode="json", exclude_unset=True))
        return update_product
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))