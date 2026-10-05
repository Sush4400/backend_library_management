from fastapi import APIRouter

from app.routes.endpoints.author_routes import router as author_router
from app.routes.endpoints.book_routes import router as book_router
from app.routes.endpoints.category_routes import router as category_router
from app.routes.endpoints.fine_routes import router as fine_router
from app.routes.endpoints.loan_routes import router as loan_router
from app.routes.endpoints.member_routes import router as member_router
from app.routes.endpoints.publisher_routes import router as publisher_router
from app.routes.endpoints.user_routes import router as user_router



api_router = APIRouter(prefix="/api/v1")

api_router.include_router(author_router)
api_router.include_router(book_router)
api_router.include_router(category_router)
api_router.include_router(fine_router)
api_router.include_router(loan_router)
api_router.include_router(member_router)
api_router.include_router(publisher_router)
api_router.include_router(user_router)