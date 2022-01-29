# e-writer
An e-reader based .ek3 injector for Pokemon Ruby/Sapphire

Replaces the first Pokemon in your party with a user-generated .ek3.


## Usage

Generate a .ek3 file using [PKHeX](https://projectpokemon.org/home/files/file/1-pkhex/), rename it to `input.ek3`, and run `inject.py`.

This will generate `card.z80`, which can then be built into a functioning dotcode.

The included `input.ek3` will inject the following Pokemon:


```
METAGROSS (shiny)
adamant
lvl 100
no item
31/31/31/7/31/31
128/252/0/0/0/128
meteor mash/earthquake/rock slide/explosion
all 32 ribbons
Revvy/57690/24422
```


## How to build

* Download [nedcmake](https://www.caitsith2.com/ereader/tools/nedcmake.rar) from [caitsith2.com E-Reader Development Tools](https://www.caitsith2.com/ereader/devtools.htm)

To run in an emulator: generate `RAW`:
```
nedcmake.exe -i card.z80 -o us -type 1 -region 1 -raw
```

To run on real hardware: generate `BMP`:
```
nedcmake.exe -i card.z80 -o us -type 1 -region 1 -bmp
```

## Thanks

[Hatschky, for their checksum calculation script](https://github.com/hatschky/pokecarde/blob/master/scripts/checksum.py)
