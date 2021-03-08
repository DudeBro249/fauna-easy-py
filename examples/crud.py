from fauna_easy.base_model import FaunaEasyBaseModel
from pydantic import BaseModel
from faunadb.client import FaunaClient

if __name__ == '__main__':
    class NewPost(BaseModel):
        title: str
        content: str

    fauna_client = FaunaClient('YOUR_CLIENT_SECRET')

    Post = FaunaEasyBaseModel('posts', NewPost)

    create_query = Post.create({
        'title': 'my post title',
        'content': 'my post content'
    })

    created_documents = fauna_client.query(create_query)
    print(created_documents)

    update_query = Post.update({
        'title': 'updated title',
        'content': 'updated content'
    }, '292479043830284807')

    updated_document = fauna_client.query(update_query)
    print('updated document')
    print(updated_document)

    delete_query = Post.delete('id')
    deleted_document = fauna_client.query(delete_query)
    print('deleted document: ')
    print(deleted_document)

    find_query = Post.find_by_id('id')
    document = fauna_client.query(find_query)
    print('found document: ')
    print(document)
