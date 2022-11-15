``` 
Last updated:   11/14/2022 
Authors:        Joshua Miller
```

## How to start:
1. Download Visual Studio Code - Software for building code for the robot (IDE): [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Install Python - Programming Language used for the robot: [https://www.python.org/](https://www.python.org/)
3. Install Git - How we will share our code: [https://git-scm.com/downloads](https://git-scm.com/downloads)
4. Open Visual Studio Code
5. On the left pane, select Extensions: ![Extensions button](readme-assets/extensions.png)
6. Install the plugins: Make sure the author is correct!
 * ev3dev-browser: Allows us to communicate to the robot
   * Author:     ev3dev
   * Version:    > 1.0.4
   * Image:      ![ev3dev-browser](readme-assets/rv3dev-browser-plugin.png)
 * GitHub Pull Requests and Issues: Allows for the access to the code
   * Author:     GitHub
   * Image:      ![GitHub Pull Requests and Issues](readme-assets/github-plugin.png)
7. Open a Terminal: One is included in Visual Studio Code
8. Enter the following command: ```pip install python-ev3dev```
   * Installs the ev3dev libraries so you can get better syntax highlighting. (And remove the library not found error)
9. Connect to the robot: [Connecting to the robot](#connecting-to-the-robot)


## Connecting to the robot
1. Have the robot charged
2. Turn on the robot
3. Wait for the robot to startup
4. 