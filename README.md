![Antistasi Phone Book Logo](/ressources/misc/Antistasi_PhoneBook256.png)
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

after downloading the release, extract the folder and run "configurator.exe". afterwards run "Antistasi_PhoneBook_tool.exe" and select rebuild Database form the toolbar.

### 1.2.1. planned stages of development to 1.0

1. [X] python code to get all functions and files
2. [X] python code to interface with SQLite
3. [X] SQLite DB to store the caller list and query items
4. [X] GUI interface for all that (tkinter?)

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

almost feature complete

### 1.2.3. Dependencies

none

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

- Icons made by <http://www.doublejdesign.co.uk/>

***
---

## 1.5. Authors

Giddi

## 1.6. License

TODO
