from fastapi import APIRouter
from view.items.itemsRouter import items_router
from view.calc.calcRouter import calc_router
from view.hello.helloRouter import hello_router
from view.user.userRouter import user_router

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(items_router)
main_api_router.include_router(calc_router)
main_api_router.include_router(hello_router)
main_api_router.include_router(user_router)

