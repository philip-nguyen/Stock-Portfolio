# Stock-Portfolio
Using 5 different investment strategies, determine how much to invest in certain stocks. This is implemented using PyQt GUI library and yfinance API.

**GUI form and info popup**

![pyqt-ui-image](https://user-images.githubusercontent.com/55335418/102582235-001c9c80-40b7-11eb-9823-96cab9e8d318.png)


**Stock Calculation Output**

![stock calculation](https://user-images.githubusercontent.com/55335418/105804886-b5176400-5f55-11eb-9f41-b3e98fd205f5.png)


## Installation
Make sure to install the dependencies

**PyQt5**
`pip install PyQt5==5.9.2`

**yfinance**
`pip install yfinance`

## Git workflow
**Create your own branch**

`git pull main`

`git checkout -b name-component_name`

for example: `git checkout -b philip-value_investing`

**After making changes and have a working component:** 

`git add .`

`git commit -m 'commit message'`

`git push origin branch-name`

**Merging to main:**

`git checkout main`

`git pull origin main`

`git merge branch-name`

`git push origin main`
