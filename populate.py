import redis

conn = redis.Redis()

target = open('repairs.txt', 'w')
target.truncate()
target.close()

# adds to redis line by line from websites.txt
with open('websites.txt', 'r') as fp:
  for line in fp:
    line = line.strip()
    conn.sadd('websites', line)

# counts number of websites added to redis
num_lines = sum(1 for line in open('websites.txt'))
print num_lines, "websites added to Redis key: 'websites'."
