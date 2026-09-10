import requests
def test_get_posts():
    r=requests.get("https://jsonplaceholder.typicode.com/posts")
    assert r.status_code==200
    assert len(r.json())==100

def test_get_single_post():
    r=requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert r.status_code==200
    data=r.json()
    assert "userId" in data
    assert "title" in data
    assert  "id" in data
    assert "body" in data
    assert  data['id']==1

def test_get_nothing():
    r=requests.get("https://jsonplaceholder.typicode.com/posts/999")
    assert r.status_code==404
def test_create_post():
    url="https://jsonplaceholder.typicode.com/posts"
    payload={
        "title":'foo',
        "body":'bar',
        "userId":1
    }
    r=requests.post(url,json=payload)
    assert r.status_code==201
    data=r.json()
    assert data['title']=='foo'
    assert data['body']=='bar'

def test_update_post():
    url="https://jsonplaceholder.typicode.com/posts/1"
    payload={
        "title":'foo1',
    }
    r=requests.patch(url,json=payload)
    assert r.status_code==200
    data=r.json()
    assert 'id' in data
    assert data['title']=='foo1'

def test_delete_post():
    url="https://jsonplaceholder.typicode.com/posts/1"
    r=requests.delete(url)
    assert r.status_code in [200,204]

def test_filter_comments():
    url="https://jsonplaceholder.typicode.com/comments"
    params={"postId":1}
    r=requests.get(url,params=params)
    assert r.status_code==200
    data=r.json()
    assert len(data)>0
    for comment in data:
        assert comment["postId"]==1

def test_response_time():
    url="https://jsonplaceholder.typicode.com/posts"
    r=requests.get(url)
    assert r.status_code==200
    assert r.elapsed.total_seconds()<2