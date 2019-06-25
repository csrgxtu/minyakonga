## API doc

### Data model
```Python
class Config(object):
    id = IntField()
    site_title = StringField()
    fav_img = StringField()
    ctime = IntField()
    mtime = IntField()
    operator = StringField()


class Article(object):
    id = IntField()
    fav_img = StringField()
    title = StringField()
    body = StringField()
    tags = ListField(IntField)
    ctime = IntField()
    mtime = IntField()
    operator = StringField()


class Tag(object):
    id = IntField()
    name = StringField()
    ctime = IntField()
    mtime = IntField()
    operator = StringField()
```

### Config API doc

#### 1st, create config
only allow create one config
```bash
POST /api/v1/config/
```

Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| site_title  | string  | body  | yes  | None  |  title of site  |
| fav_img | string | body | yes | None | fav image for site|

Response:
http status code: 200, application/json
```javascript
{
    'id': int
}
```

or
```javascript
{
    'err_code': 1002000,
    'err_msg': 'CONFIG_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1002001,
    'err_msg': 'CONFIG_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1002002,
    'err_msg': 'CONFIG_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1002003,
    'err_msg': 'CONFIG_GAE_QUOTE_EXCEED'
}
```

#### 2nd, get config
```bash
GET /api/v1/config/
```

Params:

Responses:
http status code: 200, application/json
```javascript
{
    Config
}
```

or
```javascript
{
    'err_code': 1002000,
    'err_msg': 'CONFIG_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1002001,
    'err_msg': 'CONFIG_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1002002,
    'err_msg': 'CONFIG_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1002003,
    'err_msg': 'CONFIG_GAE_QUOTE_EXCEED'
}
```


### Tag API doc

#### 1st, create tag
```bash
POST /api/v1/tag/
```

Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| name  | string  | query  | yes  | None  |  tag name  |

Response:  
http status code: 200, application/json
```javascript
{
    'id': int
}
```

or
```javascript
{
    'err_code': 1001000,
    'err_msg': 'TAG_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1001001,
    'err_msg': 'TAG_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1001002,
    'err_msg': 'TAG_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1001003,
    'err_msg': 'TAG_GAE_QUOTE_EXCEED'
}
```

#### 2nd, get tags
```bash
GET /api/v1/tag/
```

Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| page_idx  | int  | query  | yes  | 1  | page number  |
| page_size  | int  | query  | yes  | 10  | page size  |
| keyword | string | query | no | None | use keyword search tag|

Response:  
http status code: 200, application/json
```javascript
{
    'total': int,
    'page_idx': int,
    'page_size': int,
    'keyword': string,
    'tags': [
        Tag
    ]
}
```

or
```javascript
{
    'err_code': 1001000,
    'err_msg': 'TAG_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1001002,
    'err_msg': 'TAG_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1001003,
    'err_msg': 'TAG_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1001004,
    'err_msg': 'TAG_GAE_QUOTE_EXCEED'
}
```

#### 3rd, update tag
```bash
PUT /api/v1/tag/<tag_id>/
```

Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| tag_id  | int  | path  | yes  | None  | article id  |
| name  | string  | query  | yes  | None  |  tag name  |

Response:  
http status code: 200, application/json
```javascript
{
    'id': int
}
```
or
```javascript
{
    'err_code': 1001000,
    'err_msg': 'TAG_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1001002,
    'err_msg': 'TAG_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1001003,
    'err_msg': 'TAG_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1001004,
    'err_msg': 'TAG_GAE_QUOTE_EXCEED'
}
```

#### 4th, delete tag
```bash
DELETE /api/v1/tag/<tag_id>/
```
Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| tag_id  | int  | path  | yes  | None  | article id  |

Response:    
http status code: 200, application/json
```javascript
{
    'id': int
}
```
or
```javascript
{
    'err_code': 1001000,
    'err_msg': 'TAG_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1001002,
    'err_msg': 'TAG_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1001003,
    'err_msg': 'TAG_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1001004,
    'err_msg': 'TAG_GAE_QUOTE_EXCEED'
}
```

### Article API doc

#### 1st,  batch get articles
```bash
GET /api/v1/article/
```
Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| page_idx  | int  | query  | yes  | 1  | page number  |
| page_size  | int  | query  | yes  | 10  | page size  |
| keyword | string | query | no | None | use keyword search article|

Response:  
http status code: 200, application/json
```javascript
{
    'total': int,
    'page_idx': int,
    'page_size': int,
    'keyword': string,
    'articles': [
        Article
    ]
}
```

or
```javascript
{
    'err_code': 1000001,
    'err_msg': 'ARTICLE_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1000002,
    'err_msg': 'ARTICLE_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1000003,
    'err_msg': 'ARTICLE_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1000004,
    'err_msg': 'ARTICLE_GAE_QUOTE_EXCEED'
}
```

#### 2nd, get article detail
```bash
GET /api/v1/article/<article_id>/
```
Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| article_id  | int  | path  | yes  | None  | article id  |

Response:  
http status code: 200, application/json
```javascript
{
    Article
}
```

or
```javascript
{
    'err_code': 1000001,
    'err_msg': 'ARTICLE_NOT_ALLOWED'
}
```
or
```javascript
{
    'err_code': 1000002,
    'err_msg': 'ARTICLE_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1000003,
    'err_msg': 'ARTICLE_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1000004,
    'err_msg': 'ARTICLE_GAE_QUOTE_EXCEED'
}
```

#### 3rd, create article
```bash
POST /api/v1/article/
```

Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| title  | string  | body  | yes  |   | title  |
| body | string | body | yes |  | article body |
| fav_img | string | body | yes | | fav image |
| tags | list[int] | body | yes | [] | tags |

Response:  
http status code: 200 application/json
```javascript
{
    'id': int
}
```

or
```javascript
{
    'err_code': 1000001,
    'err_msg': 'ARTICLE_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1000002,
    'err_msg': 'ARTICLE_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1000003,
    'err_msg': 'ARTICLE_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1000004,
    'err_msg': 'ARTICLE_GAE_QUOTE_EXCEED'
}
```

#### 4th, update article
```bash
PUT /api/v1/article/<article_id>/
```

Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| article_id  | int  | path  | yes  | None  | article id  |
| title| string | body | optional | None | title |
| body | string | body | optional | None | body |
| fav_img | string | body | optional | None | fav image |
| tags | list[int] | body | optional | [] | tags |

Response:  
http status code: 200 application/json
```javascript
{
    'id': int
}
```

or
```javascript
{
    'err_code': 1000001,
    'err_msg': 'ARTICLE_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1000002,
    'err_msg': 'ARTICLE_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1000003,
    'err_msg': 'ARTICLE_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1000004,
    'err_msg': 'ARTICLE_GAE_QUOTE_EXCEED'
}
```

#### 5th, delete article
```bash
DELETE /api/v1/article/<article_id>/
```
Params:

| name  |  type | location  | required  |  default | description  |
|---|---|---|---|---|---|
| article_id  | int  | path  | yes  | None  | article id  |

Response:  
http status code: 200, application/json
```javascript
{
  'id': int
}
```

or
```javascript
{
    'err_code': 1000001,
    'err_msg': 'ARTICLE_NOT_ALLOWED'
}
```

or
```javascript
{
    'err_code': 1000002,
    'err_msg': 'ARTICLE_INVALID_PARAM'
}
```

or
```javascript
{
    'err_code': 1000003,
    'err_msg': 'ARTICLE_INTERNAL_ERROR'
}
```

or
```javascript
{
    'err_code': 1000004,
    'err_msg': 'ARTICLE_GAE_QUOTE_EXCEED'
}
```
