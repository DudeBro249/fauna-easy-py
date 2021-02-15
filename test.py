import fauna_easy
from fauna_easy.base_model import FaunaEasyBaseModel
from pydantic import BaseModel

if __name__ == '__main__':
    class NewPost(BaseModel):
        title: str
        content: str

    fauna_easy.use('YOUR_CLIENT_SECRET')

    Post = FaunaEasyBaseModel('posts', NewPost)

    created_document = Post.create({
        'title': 'my post title',
        'content': 'my post content'
    })

    print('document created: ')
    print(created_document.data)
    print(created_document.ref.id())

    print(Post.find_by_id(created_document.ref.id()))

    updated_document = Post.update({
        'title': 'my updated title',
        'content': 'my post content',
    }, id=created_document.ref.id())
    print('document created: ')
    print(updated_document.data)
    print(updated_document.ref.id())

    deleted_document = Post.delete(created_document.ref.id())
    print('document deleted: ')
    print(deleted_document.data)

    documents = Post.query_by_index('posts_by_content', ['my post content'])
    print(documents.dict())
