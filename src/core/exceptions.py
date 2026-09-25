from uuid import UUID


class CategoryError(Exception):
    pass


class CategoryNotFoundError(CategoryError):
    def __init__(self, category_id: UUID | None = None, title: str | None = None) -> None:
        if category_id:
            super().__init__(f"Category with ID '{category_id}' was not found.")
        elif title:
            super().__init__(f"Category with title '{title}' was not found.")
        else:
            super().__init__("Category not found.")


class CategoryAlreadyExistsError(CategoryError):
    def __init__(self, title: str | None) -> None:
        super().__init__(f"Category with title '{title}' already exists.")


class ArchiveError(Exception):
    pass


class ArchiveNotFoundError(ArchiveError):
    def __init__(self, archive_id: UUID | None = None, title: str | None = None) -> None:
        if archive_id:
            super().__init__(f"Archive with ID '{archive_id}' was not found.")
        elif title:
            super().__init__(f"Archive with title '{title}' was not found.")
        else:
            super().__init__("Archive not found.")
