#### `The Assignmnent has two tasks. Both the tasks kept under project directory with two sub directory.` 

##ngnixStaticHtml: 
####Deploy a Static HTML Website as a Container.

Dokcer image location: https://hub.docker.com/r/kalinga/
kalinga/mywebsite

__Run Steps:__
```docker pull kalinga/mywebsite:v0.1```
```docker run -d --name="kalinga.com" -p 8082:80  kalinga/mywebsite:v0.1```

__Validation:__
```chromium-browser http://localhost:8082/iamkalinga.html```

--------------------------------------II--------------------------------------
##node.js:
####Deploy a Node.js application within a container.

This tasks involve creation of two docker images (gninx, node)
Dokcer image location: https://hub.docker.com/r/kalinga/
kalinga/nodeapp
kalinga/nodeapp_nginx

__Run Steps:__

```docker pull kalinga/nodeapp:v0.1```
```docker pull kalinga/nodeapp_nginx:v0.1```
```docker run -d --name="nodejs" -p 8081:8081 kalinga/nodeapp:v0.1```
```docker run -d --name="nodeapp_nginx" -p 8080:80 --link nodejs:nodejs kalinga/nodeapp_nginx:v0.1```


__Validation:__
```chromium-browser http://localhost:8080/iamkalinga.html```

Click on the on at the bottom /nodeApp interacts with Node.js server hosted in a separate container.
OR Directly enter the URLhttp://localhost:8080/nodeApp as from browser

__Future Work:__
Introducing own index.html, now the default Ngnix pages appears.
Combining two images/containers
Explore more on node.js
Little More refinement of the UI