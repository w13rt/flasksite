from flaks import Blueprint

bp = Blueprint('api',__name__)

from app.api import users, erros, tokens
