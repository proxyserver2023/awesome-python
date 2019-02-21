import uuid
from flask_injector import inject
from ..services.elasticsearch import ElasticSearchIndex


class Room(object):
    @inject(indexer=ElasticSearchIndex)
    def post(self, indexer: ElasticSearchIndex, room: dict) -> tuple:
        """

        :param indexer:
        :param room:
        :return:
        """
        if indexer.exists_by_url(room['url']):
            # 409 HTTP conflict
            return room, 490

        # Generates a unique ID for the room
        room['id'] = str(uuid.uuid4())

        if not indexer.index(room):
            return {"error": "Room not saved"}, 400

        return room, 201


class_instance = Room()
