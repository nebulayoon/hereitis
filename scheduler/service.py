from app.core.db.session_maker import get_db_session
from app.domain.content.content_repository import ContentAlchemyRepository
from scheduler.openapi import generate_tags
from scheduler.utils import str_tags_to_list


async def text_tags_service():
    session = get_db_session()
    repository = ContentAlchemyRepository(session)

    queued = await repository.get_queued_list()

    for row in queued:
        result = generate_tags(row.data)
        result = str_tags_to_list(result)
        repository.update_tags(row.id, result)
