# Markdown Syntax
## Basics
**Headings.**   Use certain number (from 1 to 6) of '#' to create headings of different levels.  

**Changing lines.** Use two *spaces* and an *enter* to change a line.  

**Changing paragraphs.** Use an empty line to separate two paragraphs.
## Text Decorations
| Rendered Output | Source Code |
| :-----: | :-----: |
| **bold** | `**bold** or __bold__` |  
| *italics* | `*italics* or _italics_` |   
| ~~cross off~~ | `~~cross off~~` |  
| <mark>highlight</mark> | `<mark>highlight</mark>` |   
| text<sup>superscript</sup> | `text<sup>superscript</sup>` |  
| text<sub>subscript</sub>  | `text<sub>subscript</sub>` |    
## Code
### One line code
Add a *backtick* to both the beginning and end of the code.  

### Multiple lines of code  
Add three *backticks* to both the beginning and end of the code.  

If you add the language of the code, such as *cpp*, *py* and *js*, behind the first three *backticks*, it will give you syntax highlighting for the given language.

> Note: If the "triple *backticks* way" does not work (beacause it is only part of the extended specification), you can render something out as code by indenting it essentially really far (usually at least four spaces before it).
## Links
[learn Markdown by clicking this](https://youtu.be/_PPWWRV6gbA?si=kBW3GMjiXP_YA6Nt)
```
[learn Markdown by clicking this](https://youtu.be/_PPWWRV6gbA?si=kBW3GMjiXP_YA6Nt)
```
Here is the template:
```
[something you want to render out as link](the URL path)
```
If the text rendered out as link is the URL path of the link itself, you can write your code like this `<the URL path>` .
## Images Importing
![Crayon Shin-chan](https://miro.medium.com/0*I32LiwMMYY16sPAB.jpg)
```
![Crayon Shin-chan](https://miro.medium.com/0*I32LiwMMYY16sPAB.jpg)
```
Here is the template:
```
![Alt Text](the URL path of the image)
```
## Block Quotes
> You can write block quotes like this.  
>> You can also write nested block quotes like this.
```
> You can write block quotes like this.  
>> You can write nested block quotes like this.
```
The text in the block quotes also supports most of the Markdown syntax, such as how to change lines, how to change paragraphs and even writing block quotes itself (namely nested block quotes).
## Horizontal Lines
text above the horizontal line

***

text below the horizontal line
```
text above the horizontal line

*** or --- or ___

text below the horizontal line
```
Make sure you have space before and after the `*** or --- or ___` line, otherwise it might be recognized as bolding or italics sometimes. So it is recommended that you leave an empty line before and after that line.
## Lists
### ordered list
1. item 1  
2. item 2
3. item 3
```
1. item 1                    1. item 1
2. item 2  or  <arbitrary num>. item 2
3. item 3      <arbitrary num>. item 3
```
### unordered list
* item 1
* item 2
* item 3
```
* item 1      + item 1     - item 1
* item 2  or  + item 2  or - item 2
* item 3      + item 3     - item 3
```
### nested list
* homework
    1. homework 1
    2. homework 2
* project
    * hog
    * cats
    * ants
    * scheme
```
* homework
    1. homework 1
    2. homework 2
* project
    * hog
    * cats
    * ants
    * scheme
```
Use four *spaces* or a *tab* to nest lists.
## Tables
| Col 1   | Col 2 |
| -----   | ----- |
| This    |  is   |
|  a      | table |
| with    | two   |
| columns |  .    |
```
| Col 1   | Col 2 |
| -----   | ----- |
| This    |  is   |
|  a      | table |
| with    | two   |
| columns |  .    |
```
Use `|` to separate colomns, the `|` in different rows don't have to line up, but your code can be easier to read if you make them line up.

In each colomn, between the first row and other rows, use a line of several `-` (at least three) as a divider, which tells that the row above is the header and rows below are normal rows.

Your can change the alignment of the items in certain colonm by adding colon(s) to the `---` line in that column, details are shown in the table below.
| Alignment | Source Code |
| :---: | :---: |
| left aligned (default) | `---` or `:---` | 
| right aligned | `---:` |
| center aligned | `:---:` |
## Static Checkboxs
- [ ] unchecked checkbox
- [x] checked checkbox
```
- [ ] unchecked checkbox
- [x] checked checkbox
```
The letter `x` can be in lowercase or uppercase.