import fauna_easy
from fauna_easy.base_model import FaunaEasyBaseModel
from pydantic import BaseModel

if __name__ == '__main__':
    class NewPost(BaseModel):
        title: str
        content: str

    fauna_easy.use('YOUR_CLIENT_SECRET')

    Post = FaunaEasyBaseModel('posts', NewPost)
    Post.create({
        'title': 'my post title',
        'content': 'my post content',
    })
