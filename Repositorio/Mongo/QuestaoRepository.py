from Model.Questao import Questao
from Repositorio.Mongo.Configuracao.MongoSetupAssincrono import MongoSetupAssincrono
from Repositorio.Mongo.Configuracao.MongoSetupSincrono import MongoSetupSincrono

class QuestaoRepository:

    @staticmethod
    async def aprocura_um(_id: str):
        """
        método para recuperar do banco objeto do tipo questao
        Args:
            _id: string de identificacao

        Returns:
            objeto questao
        """
        resultado_bd: dict = await MongoSetupAssincrono.db_client['questao'].find_one({'_id': _id})
        return Questao(**resultado_bd)

    @staticmethod
    def sprocura_um(_id: str):
        """
        método para recuperar do banco objeto do tipo questao
        Args:
            _id: string de identificacao

        Returns:
            objeto questao
        """

        return MongoSetupSincrono.db_client['questao'].find_one({'_id': _id})