
---
# Antistasi PhoneBook tool 
> by Broca Dilettante Studio Models [BDSM]

*I am an fan of the Antistasi mod and not an Admin or dev or in any other way connected, this is fan made.* **THIS IS NOT AN OFFICIAL ANTISTASI PROJECT!**

## Description

The goal of this Project is to make a tool that can tell the Dev team of the Antistasi mod, which files call on which functions and also if you provide a file, show which other files rely on it.
Secondary it should make a Graphviz graph to visually show the Antistasi function network.

***
---

> ## Why?
>
> From the outside it seems that many bugs in the development of the Mod are due to unknown reliances on a file that got changed or unintended consequences of a function call.
> Even if these will not be cleaned up, this tool should at least make devs aware of most dangers regarding that and also help make bughunting not reliant on an personal memory of the code structure.
> lastly if it is possible the graph could identify possible redundancies or inefficent paths.
>

***
---

## How?

Currently it is written in python and intendet to interface with a tiny SQLite DB to speed up the standard process of asking for the calls. 

### planned stages of development to 1.0
1. [ ] python code to get all functions and files
2. [ ] python code to interface with SQLite
3. [ ] SQLite DB to store the caller list and query items
4. [ ] GUI interface for all that (tkinter?)

#### maybe?
stuff that I see as advantages, but currently know to little to implement or even know if it is possible:
> * travis integration
> * IDE integration as Plugin
> * changes to work with any ArmA 3 project

***




***
---



### Status

finishing first python scripts

### Dependencies

- currently python re module
- SQLite
- Graphviz

***

## Contributing to the mod

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


## External Resources


### General Links
- [Antistasi Github](https://github.com/official-antistasi-community/A3-Antistasi)


***
---

## Authors

Giddi

## License

TODO

