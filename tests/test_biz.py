from protobuf2pydantic.biz import pb2_to_pydantic


class TestPb2ToPydantic:
    def test_with_celery_task(self):
        from . import celery_task_pb2
        pb2_to_pydantic(celery_task_pb2)

    def test_with_test(self):
        from . import test_pb2
        pb2_to_pydantic(test_pb2)

    def test_with_map(self):
        from . import test_map_pb2
        pb2_to_pydantic(test_map_pb2)
