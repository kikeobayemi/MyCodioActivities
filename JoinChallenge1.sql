USE blog;

SELECT posts.user_id, users.name, posts.body 
FROM posts
RIGHT OUTER JOIN users ON
posts.user_id = users.id;