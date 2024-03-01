from typing import Annotated, List

from fastapi import APIRouter, Depends

from auth import get_current_active_user
from models.products import OfferCategory, SelectedCategory
from models.users import User
from schemas.categories import (
    OfferCategoriesRequest,
    OfferCategoryData,
    OfferCategoryRequest,
    SelectedCategoryData,
    SelectedCategoryDelRequest,
    SelectedCategoryRequest,
)
from schemas.statuses import ResponseStatus
from utils import send_mail

router = APIRouter(prefix="/categories")


@router.post("/offer-category", dependencies=[Depends(get_current_active_user)])
async def offer_category(
    data_request: OfferCategoryRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    await OfferCategory.create(
        title=data_request.title,
        user=current_user,
        explanation=data_request.explanation,
    )

    admin_emails = [admin.email for admin in await User.filter(is_admin=True)]
    await send_mail(admin_emails, "New offer add category", "New offer add category")
    return ResponseStatus(status=True, message="Offer added")


@router.get("/offer-categories", dependencies=[Depends(get_current_active_user)])
async def offer_categories(
    status: OfferCategoriesRequest.Statuses,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> List[OfferCategoryData]:
    statuses = (
        (
            OfferCategoriesRequest.Statuses.new.value,
            OfferCategoriesRequest.Statuses.accepted.value,
            OfferCategoriesRequest.Statuses.rejected.value,
        )
        if status == OfferCategoriesRequest.Statuses.all
        else [status.value]
    )

    if current_user.is_admin:
        return [
            OfferCategoryData(
                id=offer.id,
                title=offer.title,
                explanation=offer.explanation,
                user_email=offer.user.email,
                status=offer.status,
                answer=offer.answer,
            )
            for offer in await OfferCategory.filter(
                status__in=statuses
            ).prefetch_related("user")
        ]
    else:
        return [
            OfferCategoryData(
                id=offer.id,
                title=offer.title,
                explanation=offer.explanation,
                user_email=offer.user.email,
                status=offer.status,
                answer=offer.answer,
            )
            for offer in await OfferCategory.filter(
                status__in=statuses, user=current_user
            ).prefetch_related("user")
        ]


@router.post("/select-category", dependencies=[Depends(get_current_active_user)])
async def select_category(
    data_request: SelectedCategoryRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    await SelectedCategory.create(**data_request.model_dump(), user=current_user)

    return ResponseStatus(status=True, message="Category selected")


@router.get("/select-categories", dependencies=[Depends(get_current_active_user)])
async def select_categories(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> List[SelectedCategoryData]:
    categories = [
        SelectedCategoryData(id=cat.id, category=cat.category.title, type=cat.type)
        for cat in await SelectedCategory.filter(user=current_user).prefetch_related(
            "category"
        )
    ]

    return categories


@router.post("/del-selected-category", dependencies=[Depends(get_current_active_user)])
async def del_selected_category(
    data_request: SelectedCategoryDelRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    selected_category = await SelectedCategory.get_or_none(id=data_request.id)

    if not selected_category or current_user != (await selected_category.user):
        return ResponseStatus(status=False, message="Object not found")
    await selected_category.delete()
    return ResponseStatus(status=True, message="Object deleted")
