## Plattshacks : Docker In Action

Code for Docker In Action. Instructions to build and run this image

Build the image
```sh
docker build -t your-tag-name .
```
Spawn the container
```sh
docker run -e GIF=batman -p 7070:7070 your-tag-name
```

