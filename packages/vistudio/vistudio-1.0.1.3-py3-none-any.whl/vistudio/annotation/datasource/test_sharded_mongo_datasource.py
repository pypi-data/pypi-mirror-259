import sharded_mongo_datasource
import uuid
import ray
from ray.data.read_api import read_datasource
from pymongoarrow.api import Schema
import pyarrow as pa

uri = "mongodb://root:mongo123#@10.27.240.45:8719"
db_name = "lyw"
collection_name = "test"

def init_mongo():
    import pymongo

    client = pymongo.MongoClient(uri)
    test = client[db_name][collection_name]
    test.delete_many({})

    # # Inject 5 test docs.
    docs = [{"name": uuid.uuid4().hex, "float_field": 2.0 * val, "int_field": val} for val in range(10000)]
    test.insert_many(docs)


@ray.remote
def start():
    """Example for using ShardedMongoDatasource."""
    def read(item):
        name = item["name"]
        float_field = item["float_field"]
        int_field = item["int_field"]
        print(f"name: {name}, float_field: {float_field}, int_field: {int_field}")

        return {
            "name": name,
            "float_field": float_field,
            "int_field": int_field
        }

    uri = "mongodb://root:mongo123#@10.27.240.45:8719"
    db_name = "lyw"
    collection_name = "test"
    schema = Schema({"name": pa.string(), "float_field": pa.float64(), "int_field": pa.int32()})

    source = sharded_mongo_datasource.ShardedMongoDatasource(
        uri=uri,
        database=db_name,
        collection=collection_name,
        schema=schema)
    ds = read_datasource(source, parallelism=10)

    ds = ds.map(read)
    ds.show(1)


if __name__ == "__main__":
    ray.init(address="ray://10.27.240.45:8887")
    ray.get(start.remote())
    ray.shutdown()