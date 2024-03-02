class TyradexError(Exception):
    pass


class DataNotExistError(TyradexError):
    pass


class DataNotFoundError(TyradexError):
    pass


class ServerError(TyradexError):
    pass
