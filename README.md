# Selenium test in Docker

# URLs

## local
- [Selenium Hub UI](http://localhost:4444/)
- [noVNC Address](http://localhost:7901/?autoconnect=1&resize=scale&password=secret)

## resources
- [noVNC](https://novnc.com/info.html)
- [docker-selenium](https://github.com/SeleniumHQ/docker-selenium)
- [Pytest generate tests](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html)
- [Concurrent Pytest Package: pytest-xdist](https://pypi.org/project/pytest-xdist/)
- [How-to-connect-selenium-grid-with-python](https://medium.com/@ethan.han.qa/how-to-connect-selenium-grid-with-python-35bb460803f4)

# Commands
```bash
# start all containers
docker compose up -d 

# stop and remove all container
docker compose down

# stop and remove test container and recreate it
docker compose rm -sf test && docker compose up -d --build test --no-recreate

# see test logs and follow it
docker compose logs -f test

# clear danling images
docker image prune
```