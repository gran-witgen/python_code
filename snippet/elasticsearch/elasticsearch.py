from elasticsearch import Elasticsearch

#create instance from elasticsearch
es = Elasticsearch()

# get data from elasticsearch
def get_data(index,doc_type,query):
    res = es.index(index=index,doc_type=doc_type,body=query)
    print(res)
    return res
    
#define index,doc_type,query
index = "catalog"
doc_type = "product"
query = {
    "query":{
        "match_all":{}
    }
}

#execute function
get_data(index,doc_type,query)


#create data from python client to elasticsearch
def create_data(index,doc_type,query):
    res = es.index(index=index,doc_type=doc_type,body=query)
    return res

#define index,doc_type,query
index = "testcase"
doc_type = "doc"
query = {
    "mappings":{
        "doc":{
            "properties":{
                "name":{
                    "type":"text"
                }
            }
        }
    }
}

#execute function
create_data(index,doc_type,query)   

