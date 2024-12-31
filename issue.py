from pymilvus import CollectionSchema, FieldSchema
from pymilvus import Collection
from pymilvus import connections
from pymilvus import DataType
from pymilvus import Partition
from pymilvus import utility
import json
import random
import numpy as np

connections.connect(host="10.102.9.91", port="19530")

dim = 128
int64_field = FieldSchema(name="int64", dtype=DataType.INT64, is_primary=True)
double_field = FieldSchema(name="nullableFid", dtype=DataType.FLOAT, nullable=True)
# int32_field = FieldSchema(name="int32", dtype=DataType.FLOAT, default_value=np.float32(3.0))
#array_field = FieldSchema(name="array", dtype=DataType.ARRAY, element_type=DataType.INT32, max_capacity=100, nullable=True)
float_vector = FieldSchema(name="float_vector", dtype=DataType.FLOAT_VECTOR, dim=dim, nullable=False)
schema = CollectionSchema(fields=[int64_field, double_field, float_vector])
utility.drop_collection("testlxg")
collection = Collection("testlxg", schema=schema)
res = collection.schema
print(res)



index = "HNSW"
params = {"M": 32, "efConstruction": 360}
default_index = {"index_type": index, "params": params, "metric_type": "COSINE"}

nb = 10
vectors = [[random.random() for _ in range(dim)] for _ in range(nb)]
# null_field_data = [float(i) for i in range(int(nb/2))] + [None for _ in range(int(nb/2))]
null_field_data = [0.0, 1.0, 2.0, 3.0, 4.0, None, None, None, None, None]
data = [[i for i in range(nb)], null_field_data, vectors]

collection.insert(data=data)
# collection.flush()
collection.create_index("float_vector", default_index, index_name="index_name_1")
collection.load()
res = collection.num_entities
print(res)
default_search_params = {"metric_type": "COSINE", "params": {"ef": 64}}
limit = 10
nq = 2
import time
start = time.time()
res1 = collection.search(vectors[:nq], "float_vector", default_search_params, limit, expr="is_not_null(float_vector)", output_fields=["nullableFid"])
end = time.time() - start
print(res1)
print("search successfully in %f s" % end)
start = time.time()
# res = collection.query("is_not_null(nullableFid)", output_fields=["nullableFid","int64"])
# end = time.time() - start
# print(res)
# print("query successfully in %f s" % end)