import time

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432


def article_vote(conn, user, article):
    cutoff = time.time() - ONE_WEEK_IN_SECONDS

    if conn.zscore('time:', article) < cutoff:
        return

    article_id = article.partition(':')[-1]
    if conn.sadd(f'voted:{article_id}', user):
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)


# Posting and fetching articles
def post_article(conn, user, title, link):
    article_id = str(conn.incr('article:'))
    voted = f'voted:{article_id}'
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = f'article:{article_id}'
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1,
    })
    conn.zadd('score:', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)

    return article_id


ARTICLES_PER_PAGE = 25


def get_articles(conn, page, order='score'):
    start = (page-1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1
    ids = conn.zrevrange(order, start, end)
    articles = []
    for id in ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)
    return articles


def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
    article = f'article:{article_id}'
    for group in to_add:
        conn.sadd(f'group:{group}', article)
    for group in to_remove:
        conn.srem(f'group:{group}', article)


def get_group_articles(conn,
                       group,
                       page,
                       order='score:'):
    key = f'{order}{group}'
    if not conn.exists(key):
        conn.zinterstore(
            key,
            [f'group:{group}', order],
            aggregate='max'
        )
        conn.expire(key, 60)

    return get_articles(conn, page, key)


from flask import Flask
from .Redis import Redis


app = Flask(__name__)
redis = Redis(host='redis').conn


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )
