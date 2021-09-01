from functools import lru_cache

from pydantic import BaseModel

from Excecoes.MongoExceptions import MongoFindException1, MongoFindException2
from Model.Questao import Questao
from Repositorio.Mongo.Configuracao.MongoSetupAssincrono import MongoSetupAssincrono
from Repositorio.Mongo.Configuracao.MongoSetupSincrono import MongoSetupSincrono


class QuestaoRepository:

    @staticmethod
    async def aprocura_um(_id: str):
        """
        método para recuperar do banco model do tipo usuario
        Args:
            _id: string de identificacao

        Returns:
            model usuario
        """
        resultado_bd: dict = await MongoSetupAssincrono.db_client['usuario'].find_one({'_id': _id})
        return Questao(**resultado_bd)

    @staticmethod
    def find_one(_id: str):
        """
        método para recuperar do banco o model especificada
        Args:
            i: string de identificacao

        Returns:
            model usuario
        """

        resultado_bd: dict = MongoSetupSincrono \
            .db_client['questao'] \
            .find_one({'_id': _id})

        if resultado_bd is None:
            raise MongoFindException2()
        return Questao(**resultado_bd)

    @staticmethod
    def make_teste(quantidade: int):
        """
        método para recuperar do banco o model especificada
        Args:
            i: string de identificacao

        Returns:
            model usuario
        """

        resultado_bd: dict = MongoSetupSincrono \
            .db_client['questao'] \
            .find(limit=quantidade)

        if resultado_bd is None:
            raise MongoFindException2()
        return [Questao(**questao) for questao in resultado_bd]
