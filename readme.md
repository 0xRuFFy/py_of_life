# Py of Life
## Conway's Game of Life in Python
### <span style="text-decoration: underline">Konstantin Opora</span>

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): graphical implementation in python using pyglet.
> developed in Python 3.10.0

## Resources
- [Wiki_en](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Wiki_de](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens)
- [Black](https://github.com/psf/black)

### Black command
```shell 
> black . -t py310 -l 100
```

## TODOs:
- [ ] create a selection tool for cells
    - [ ] create group selections for cells
    - [ ] deletion of selected cells
    - [ ] copy / paste selections
- [ ] create presets to use
- [x] make simulation values (width, height, cellsize, etc.) modifiable
- [x] add suport for different worlds -> input shorthand version (e.q.: 23/3, 3/3, 13/3, 1357/1357)
- [ ] add display for simulation info : Generation, Population, etc.
- [ ] optimize code -> increase performance

## How to use
### To play the game with:
```shell
> python3 src/py_of_life.py
```

### While runnig
- You can <span style="text-decoration: underline">place cells</span> by pressing/dragging the **left mousebutton**
- You can <span style="text-decoration: underline">remove cells</span> by pressing/dragging the **right mousebutton**
- You can <span style="text-decoration: underline">remove all cells</span> by pressing the **Backspace**
- You can <span style="text-decoration: underline">start the simulation</span> by pressing **SPACE**
- You can <span style="text-decoration: underline">stop the simulation</span> by pressing **SPACE**

> You can only modify cell while the simulation is not running
