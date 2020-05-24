
---

- [Antistasi PhoneBook tool](#antistasi-phonebook-tool)
  - [Description](#description)

  - [How](#how)
    - [planned stages of development to 1.0](#planned-stages-of-development-to-10)
      - [maybe](#maybe)

    - [Status](#status)
    - [Dependencies](#dependencies)
  - [Contributing to the mod](#contributing-to-the-mod)
  - [External Resources](#external-resources)
    - [General Links](#general-links)

  - [Authors](#authors)
  - [License](#license)

# 1. Antistasi PhoneBook tool

> by Broca Dilettante Studio Models [BDSM]

*I am an fan of the Antistasi mod and not an Admin or dev or in any other way connected, this is fan made.* **THIS IS NOT AN OFFICIAL ANTISTASI PROJECT!**

## 1.1. Description

The goal of this Project is to make a tool that can tell the Dev team of the Antistasi mod, which files call on which functions and also if you provide a file, show which other files rely on it.
Secondary it should make a Graphviz graph to visually show the Antistasi function network.

***
---

> ## Why
>
> From the outside it seems that many bugs in the development of the Mod are due to unknown reliances on a file that got changed or unintended consequences of a function call.
> Even if these will not be cleaned up, this tool should at least make devs aware of most dangers regarding that and also help make bughunting not reliant on an personal memory of the code structure.
> lastly if it is possible the graph could identify possible redundancies or inefficent paths.
>

***
---

## 1.2. How to use currently

Currently only the base functionality is implemented, and as there is a module that isn't on pip in here, it would be hard to describe that whole process. Especially if the GUI and freeze are almost done.
If you still want to try:

- you need this external module: armaclass see <https://github.com/overfl0/Armaclass> (the module, gid_land is my own and is already in the files you download)
- open the "user_config.ini" and either change the paths under DEFAULT to your own, or put them as entries under "from_user" with exactly the same name as in "DEFAULT"
- to build the DB run "DB_initiated.py", this can take up to two minutes sadly (because of 2 regex serches I had to implement)
- afterward you can use "query_from_fnc.py" when you provide a function name and the tool will tell you all files that are calling it
- Or you can use "query_from_file.py" when you want to provide a filename and the tool will tell you all files that call the function that is representing the file.

### 1.2.1. planned stages of development to 1.0

1. [X] python code to get all functions and files
2. [X] python code to interface with SQLite
3. [X] SQLite DB to store the caller list and query items
4. [~] GUI interface for all that (tkinter?)

#### 1.2.1.1. maybe

stuff that I see as advantages, but currently know to little to implement or even know if it is possible:
>
> * travis integration
> * IDE integration as Plugin
> * changes to work with any ArmA 3 project

***

***
---

### 1.2.2. Status

finishing first python scripts

### 1.2.3. Dependencies

- currently python re module
- SQLite
- Graphviz

***

## 1.3. Contributing to the mod

**Note:** General Github help is always needed as this is also a new world for me.

Feel free to contribute as I honestly will need all the help I can get!

***

> ## A word on the quality and style
>
> I never learned to program or modeling, my education is purely in medicine and everyone knows how tech literate Doctors, Nurses and other medical personnel are :wink:.
> I literally am starting out in programming and especially python.
>
> What I want to say with all that is, I know that my code is most likely not as efficient as it could be, but I am happy and open for input regarding that.
> Every form of constructive criticism and advice is more than appreciated!
>
> Thanks
> Giddi

***

## 1.4. External Resources

### 1.4.1. General Links

- [Antistasi Github](https://github.com/official-antistasi-community/A3-Antistasi)

***
---

## 1.5. Authors

Giddi

## 1.6. License

TODO
