# e-writer
An e-reader based .ek3 injector for Pokemon Ruby/Sapphire

Inject one dotcode, speak to Norman, then repeat with the other dotcode

```
METAGROSS (shiny), 
adamant, 
lvl 100, 
no item, 
31/31/31/7/31/31, 
128/252/0/0/0/128, 
meteor mash/earthquake/rock slide/explosion, 
all 32 ribbons, 
Revvy/57690/24422
```

__todo__

Throw the script into a *single* dotcode, as opposed to two

Create a program to change the pokemon that gets injected

## How to build

* Download [nedcmake](https://www.caitsith2.com/ereader/tools/nedcmake.rar) from [caitsith2.com E-Reader Development Tools](https://www.caitsith2.com/ereader/devtools.htm)

To run in an emulator: generate `RAW`:
```
nedcmake.exe -i <card>.z80 -o us -type 1 -region 1 -raw
```

To run on real hardware: generate `BMP`:
```
nedcmake.exe -i <card>.z80 -o us -type 1 -region 1 -bmp
```

